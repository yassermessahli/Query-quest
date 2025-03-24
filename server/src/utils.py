# utils.py: utility functions
import hashlib
from .models import Question
from .question_validation import LLMChecker


def validate_answer(question, answer: str) -> bool:
    return LLMChecker().check_with_llm(question, answer)

def ontime_flag(team: str, question: int) -> str:
    """
    Generate a Ontime-flag based on question ID and team code.
    
    Args:
        question (int): The question number (1 to MAX_QUESTIONS)
        team (str): Team's unique 8-digits code
    
    Returns:
        str: Generated flag in format: 32-characters long hexadecimal string
    """
    
    secret = Question.objects.get(number=question).secret
    # Combine team_code and secret_key
    data = team + secret

    # Generate hash using SHA-256
    hash_object = hashlib.sha256(data.encode())
    flag = hash_object.hexdigest()[:32]  # Take first 32 chars for medium-length flag

    return flag
    


if __name__ == '__main__':
    print(ontime_flag('53405032', 2))
    