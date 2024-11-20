from mysql import connector
from datetime import datetime
from dotenv import load_dotenv
import argparse
import json
import sys
import random
import string
import os




DOT_ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'server', '.env') # edit this when needed



def getid(way: str = 'M'):
    if way == 'D':
        characters = string.digits
    elif way == 'C':
        caracters = string.ascii_lowercase + string.ascii_uppercase
    elif way == 'M':
        characters = string.digits + string.ascii_lowercase
    else:
        raise ValueError("Invalid way argument")

    question_id = ''.join(random.choice(characters) for _ in range(8))
    return question_id

def connect_to_database():
    """Establish connection to MySQL database"""
    load_dotenv(DOT_ENV_PATH)
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


def load_json_file(file_path):
    """Load and parse JSON file"""
    with open(file_path, 'r') as file:
        return json.load(file)

def insert_questions(cursor, questions_data):
    """Insert questions into the database"""
    question_query = """
    INSERT INTO app_question_table 
    (number, id, secret, duration, statement, task, exp_output, 
     typical_answer, created_at, updated_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    current_time = datetime.now()
    
    for question in questions_data:
        values = (
            question.get('number', None),  # default NULL if not specified
            question.get('id', getid()),  # empty string if not specified
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
    args = parser.parse_args()
    return args


def main():
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
        print("Database population completed successfully!")
        
    except connector.Error as err:
        print(f"An error occurred: {err}")
        connection.rollback()
        
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()