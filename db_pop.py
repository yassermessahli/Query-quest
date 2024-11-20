import json
from mysql import connector
from datetime import datetime
import sys
import os
from dotenv import load_dotenv
import random
import string


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
            team.get('token', ''),  # empty string if not specified
            team.get('question', 1),  # default to 1 if not specified
            current_time,
            current_time
        )
        cursor.execute(team_query, values)

def main():
    # Command line arguments for file paths
    if len(sys.argv) == 3:
        questions_file = sys.argv[1]
        teams_file = sys.argv[2]
    elif len(sys.argv) == 2:
        questions_file = sys.argv[1]
        teams_file = None
    else:
        print("Usage: python database_population.py <teams_file> [questions_file]")
        sys.exit(1)
    
    # Connect to database
    connection = connect_to_database()
    cursor = connection.cursor()
    
    try:
        if questions_file:
            questions_data = load_json_file(questions_file)
            insert_questions(cursor, questions_data)
            
        if teams_file:
            teams_data = load_json_file(teams_file)
            insert_teams(cursor, teams_data)
        
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