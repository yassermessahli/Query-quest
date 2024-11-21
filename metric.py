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
import pandas.api.types
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
    QUESTIONS_SECRETS = {
        1: "07aos1rm",
        2: "nira5k6p", 
        3: "ykj4xylq",
        4: "ie1dtuwg",
        5: "542dmc2b",
        6: "2h33udhn",
        7: "oljf3yln",
        8: "450mjlkt",
        9: "jg1ph9an",
        10: "4g87t2db",
        11: "i59bn62y", 
        12: "c9bdckta",
        13: "a0314yki",
        14: "1mm2xv33",
        15: "39fv7f9k",
        16: "va5w0hoy",
        17: "h32coht6",
        18: "y45s24f7",
        19: "13e59ezx",
        20: "7589fa3h",
        21: "3e5d8kze",
        22: "862oblna",
        23: "ihz31mkl",
        24: "4nq0w65c",
        25: "l9cltd21",
        26: "nvgxd5nx",
        27: "oowgh1bi",
        28: "glelenqp",
        29: "urggxk2m",
        30: "a9rkxn54"
    }
    
    for q in range(QUESTION_NUMBER):
        secret = QUESTIONS_SECRETS[q]
        data = str(submission["team_code"]) + str(secret)
        hash_object = hashlib.sha256(data.encode())
        flag = hash_object.hexdigest()[:32]
        if flag == submission["flag"]:
            return float(q/QUESTION_NUMBER)
    return 0.0