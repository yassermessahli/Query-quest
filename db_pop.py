"""
Database Population Tool for Assessment Platform
A command-line utility to populate a MySQL database with questions and teams for a DataCamp-like assessment website. Reads data from JSON files and
inserts it into the appropriate database tables.

Usage:
    python db_pop.py -q questions.json -t teams.json
Arguments:
    -q, --questions: Path to JSON file with question data
    -t, --teams: Path to JSON file with team data
    --dry-run: Validate data without database insertion
    --clear-existing: Clear existing data before insertion
Environment:
    Requires a `.env` file in the server directory with database credentials (DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME)
"""

from mysql import connector
from datetime import datetime
from dotenv import load_dotenv
import argparse
import json
import sys
import random
import string
import os
import logging




DOT_ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'server', '.env') # edit this when needed



def getid(way: str = 'M'):
    if way == 'D':
        characters = string.digits
    elif way == 'C':
        characters = string.ascii_lowercase + string.ascii_uppercase
    elif way == 'M':
        characters = string.digits + string.ascii_lowercase
    else:
        raise ValueError("Invalid way argument")

    question_id = ''.join(random.choice(characters) for _ in range(8))
    return question_id

def connect_to_database():
    """Establish connection to MySQL database"""
    try:
        load_dotenv(DOT_ENV_PATH)
        required_vars = ['DB_HOST', 'DB_PORT', 'DB_USER', 'DB_PASSWORD', 'DB_NAME']
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
            
        connection = connector.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            # Enable SSL connection
            ssl_ca=os.getenv('DB_SSL_CA'),
        )
        return connection
    except connector.Error as err:
        print(f"Database connection error: {err}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


def load_json_file(file_path):
    """Load and parse JSON file"""
    with open(file_path, 'r') as file:
        return json.load(file)

def validate_question(question):
    """Validate question data"""
    required_fields = ['statement', 'task']
    for field in required_fields:
        if not question.get(field):
            return False, f"Missing required field: {field}"
    return True, None

def question_exists(cursor, question_id):
    """Check if a question with the given ID already exists"""
    query = "SELECT COUNT(*) FROM app_question_table WHERE id = %s"
    cursor.execute(query, (question_id,))
    count = cursor.fetchone()[0]
    return count > 0

def insert_questions(cursor, questions_data):
    """Insert questions into the database"""
    question_query = """
    INSERT INTO app_question_table 
    (number, id, secret, duration, statement, task, exp_output, 
     typical_answer, created_at, updated_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    current_time = datetime.now()
    
    inserted_count = 0
    skipped_count = 0
    
    for question in questions_data:
        is_valid, error_msg = validate_question(question)
        if not is_valid:
            print(f"Skipping invalid question: {error_msg}")
            continue
            
        question_id = question.get('id', getid())
        
        if question_exists(cursor, question_id):
            logging.warning(f"Question with ID {question_id} already exists. Skipping.")
            skipped_count += 1
            continue
            
        values = (
            question.get('number', None),  # default NULL if not specified
            question_id,
            question.get('secret', getid('D')),  # empty string if not specified
            question.get('duration', 120),  # default 120 if not specified
            question.get('statement', ''),
            question.get('task', ''),
            question.get('expected_output', ''),
            question.get('typical_answer', ''),
            current_time,
            current_time
        )
        cursor.execute(question_query, values)
        inserted_count += 1
    
    logging.info(f"Questions inserted: {inserted_count}, skipped: {skipped_count}")

def insert_teams(cursor, teams_data):
    """Insert teams into the database"""
    team_query = """
    INSERT INTO app_team_table 
    (code, name, token, question_id, created_at, updated_at)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    
    current_time = datetime.now()
    
    for team in teams_data:
        values = (
            team.get('code', getid('D')),  # random id string if not specified
            team.get('name', ''),
            team.get('token', getid('M')*4),  # empty string if not specified
            team.get('question', 1),  # default to 1 if not specified
            current_time,
            current_time
        )
        cursor.execute(team_query, values)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Populate database with questions and/or teams from JSON files')
    parser.add_argument('-q', '--questions', help='Path to questions JSON file', type=str)
    parser.add_argument('-t', '--teams', help='Path to teams JSON file', type=str)
    parser.add_argument('--dry-run', action='store_true', help='Validate data without inserting into database')
    parser.add_argument('--clear-existing', action='store_true', help='Clear existing data before insertion')
    return parser.parse_args()

def setup_logging():
    """Set up logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("db_population.log"),
            logging.StreamHandler()
        ]
    )

def main():
    setup_logging()
    logging.info("Starting database population")
    # Parse command-line arguments
    args = parse_arguments()

    # Connect to database
    connection = connect_to_database()
    cursor = connection.cursor()
    
    try:
        # Only attempt to load and insert if the respective argument is provided
        try:
            if args.questions:
                questions_data = load_json_file(args.questions)
                insert_questions(cursor, questions_data)
        except AttributeError:
            pass
        
        try:
            if args.teams:
                teams_data = load_json_file(args.teams)
                insert_teams(cursor, teams_data)
        except AttributeError:
            pass
        
        # Commit changes
        connection.commit()
        logging.info("Database population completed successfully!")
        
    except connector.Error as err:
        logging.error(f"Database error occurred: {err}")
        connection.rollback()
        
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()