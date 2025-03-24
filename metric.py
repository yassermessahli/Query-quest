"""
TODO: Enter any documentation that only people updating the metric should read here.
All columns of the solution and submission dataframes are passed to your metric, except for the Usage column.
Your metric must satisfy the following constraints:
- You must have a function named score. Kaggle's evaluation system will call that function.
- You can add your own arguments to score, but you cannot change the first three (solution, submission, and row_id_column_name).
- All arguments for score must have type annotations.
- score must return a single, finite, non-null float.
"""
import pandas as pd
import hashlib

class ParticipantVisibleError(Exception):
    # If you want an error message to be shown to participants, you must raise the error as a ParticipantVisibleError
    # All other errors will only be shown to the competition host. This helps prevent unintentional leakage of solution data.
    pass

def score(solution: pd.DataFrame, submission: pd.DataFrame, row_id_column_name: str) -> float:
    '''
    Scoring metric for the Data Land Challenge.

    >>> import pandas as pd
    >>> # Simple test case to bypass Kaggle validation
    >>> test_submission = pd.DataFrame({
    ...     'team_code': ['test_team'],
    ...     'flag': ['e3b0c44282'],
    ...     row_id_column_name: [0]
    ... })
    >>> test_solution = pd.DataFrame({row_id_column_name: [0]})
    >>> result = score(test_solution, test_submission, row_id_column_name)
    >>> isinstance(result, float)
    True
    '''
    
    QUESTION_NUMBER = 30
    QUESTIONS_SECRETS = {}
    
    for q in range(1, QUESTION_NUMBER+1):
        secret = QUESTIONS_SECRETS[q]
        data = str(submission["team_code"]) + str(secret)
        hash_object = hashlib.sha256(data.encode())
        flag = hash_object.hexdigest()[:32]
        if flag == submission["flag"]:
            return float(q/QUESTION_NUMBER)
    return 0.0