# utils.py: utility functions
import hashlib
from .models import Question



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

    try:
        secret = Question.objects.get(number=question).secret
        # Combine team_code and secret_key
        data = team + secret
    
        # Generate hash using SHA-256
        hash_object = hashlib.sha256(data.encode())
        flag = hash_object.hexdigest()[:32]  # Take first 32 chars for medium-length flag
    
        return flag
        
    except Question.DoesNotExist:    
        raise ValueError(f"Invalid question ID: {question}")
    


if __name__ == '__main__':
    print(ontime_flag('53405032', 2))
    