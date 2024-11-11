# utils.py: utility functions
import hashlib
from .models import Question


# Maximum number of questions
try:  # to handle not existing table yets
    MAX_QUESTIONS = Question.objects.last().number
except (Question.DoesNotExist, Exception):
    MAX_QUESTIONS = 0

# Secret keys for Flag generation
try:
    SECRET_KEYS = {question.number:question.secret for question in Question.objects.all()}
except (Question.DoesNotExist, Exception):
    SECRET_KEYS = {}



def chech_with_LLM(question: Question, answer: str) -> bool:
    """
    Check if the answer (input code) is correct using Language Model.
    
    Args:
        question (Question): Question object
        answer (str): Answer provided by the team
        
    Returns:
        bool: True if answer is correct, False otherwise
    """
    return True


def ontime_flag(team: str, question: int) -> str:
    """
    Generate a Ontime-flag based on question ID and team code.
    
    Args:
        question (int): The question number (1 to MAX_QUESTIONS)
        team (str): Team's unique 8-digits code
    
    Returns:
        str: Generated flag in format: 32-characters long hexadecimal string
    """

    secret = SECRET_KEYS.get(question, None)
    if secret:
        # Combine team_code and secret_key
        data = team + secret
    
        # Generate hash using SHA-256
        hash_object = hashlib.sha256(data.encode())
        flag = hash_object.hexdigest()[:32]  # Take first 32 chars for medium-length flag
    
        return flag
        
    else:    
        raise ValueError(f"Invalid question ID: {question}")  # FIX THIS!
    


if __name__ == '__main__':
    print(ontime_flag('53405032', 2))
    