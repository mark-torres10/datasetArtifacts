"""Helpful utility functions."""
from typing import Dict

def is_answer_correct(pred: Dict) -> bool:
  """Evaluates if a prediction is within the set of possible answer choices.

  Allows us to evaluate "exact match" metric for ELECTRA evaluation. The
  "exact match" that we see during the model's evaluation portion should
  be replicated with this function.
  
  Returns boolean.
  """

  possible_answers = pred["answers"]["text"]
  predicted_answer = pred["predicted_answer"]
  return predicted_answer in possible_answers
