from typing import Optional
from openai import OpenAI
from dotenv import load_dotenv
from dataclasses import dataclass
import os
from pathlib import Path


@dataclass
class LLMConfig:
    """Configuration for LLM parameters"""
    model: str = "gpt-4o-mini"  # Updated to a more recent model
    temperature: float = 0.5
    max_tokens: int = 1
    max_retries: int = 5
    personality: str = """You are an expert in data science and Python programming. Your task is to evaluate Python code solutions for data science 
    challenges. You must respond ONLY with 'True' for correct solutions or 'False' for incorrect ones, 
    considering both syntax and logical correctness."""

class LLMResponseError(Exception):
    """Custom exception for LLM response errors"""
    pass

class LLMChecker:
    
    DOT_ENV_PATH = Path(__file__).resolve().parent.parent / '.env'
    
    def __init__(self, config: Optional[LLMConfig] = None):
        """Initialize the LLM checker with configuration"""
        load_dotenv()
        self.config = config or LLMConfig()
        # # REMOVE THIS BELOW IN PRODUCTION!!!!!
        # AND ADD THIS INSTEAD!
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key not found in environment variables")
        self.agent = OpenAI(api_key=self.api_key)

    def _setup_prompt(self, question, answer: str) -> str:
        """Prepare the prompt for the LLM"""
        return f"""
        Evaluate this data science solution of the user. Respond ONLY with 'True' or 'False'.
        
        CHALLENGE DETAILS:
        Statement: {question.statement}
        Task: {question.task}
        Expected Output Format: {question.exp_output}
        
        SUBMITTED SOLUTION:
        {answer}
        
        ===========
        Respond only with 'True' or 'False'. you can accept the code if the syntax error is small
        NOTE: do not be that strict, consider the user's effort and the logic behind the code.
        """

    def _validate_question(self, question) -> None:
        """Validate question object"""
        required_fields = ['statement', 'task', 'exp_output', 'typical_answer']
        for field in required_fields:
            if not getattr(question, field, None):
                raise ValueError(f"Question missing required field: {field}")

    def _get_llm_response(self, prompt: str) -> bool:
        """Get response from LLM """
        try:
            response = self.agent.chat.completions.create(
                model=self.config.model,
                messages=[
                    {"role": "system", "content": self.config.personality},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=self.config.max_tokens,
                temperature=self.config.temperature
            )
            response_content = response.choices[0].message.content.strip().lower()
            
            if response_content not in ['true', 'false']:
                raise LLMResponseError(f"Invalid response format: {response_content}")
            
            return response_content == 'true'
            
        except Exception as e:
            raise LLMResponseError(f"Error from Language Model: {e}")




    def check_with_llm(self, question, answer: str) -> bool:
        """
        Check if the answer is correct using LLM.
        
        Args:
            question (Question): Question object
            answer (str): Answer provided by the team
            
        Returns:
            Tuple[bool, dict]: (is_correct, metadata)
        """
        try:
            # Validate inputs
            self._validate_question(question)

            # Prepare and send prompt to LLM
            prompt = self._setup_prompt(question, answer)
            result = self._get_llm_response(prompt)
            return result
        
        except Exception as e:
            raise e

if __name__ == "__main__":
    checker = LLMChecker()
    print(checker)