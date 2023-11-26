import cohere
import os
from cohere.responses.classify import Example

COHERE_API_KEY = "xxgLc7lYofMMXtHhUcqM60iPlRWvjHQ4Syy6ttKz"
os.environ["COHERE_API_KEY"] = COHERE_API_KEY

co = cohere.Client('{apiKey}')

INTENTS = {'General QA': 0, 'Diagnose Brain Tumour': 1, 'Blood Work': 2}

def get_user_intent(user_message):

  examples = [
    Example("I need a tumour diagnoses on this brain scan.", "Diagnose Brain Tumour"),
    Example("Can you make a diagnoses for this brain MRI?", "Diagnose Brain Tumour"),
    Example("What is the cancer likelihood for this MRI scan of a patient's brain?", "Diagnose Brain Tumour"),
    Example("What is the probability of positive tumour diagnosis for this brain MRI.", "Diagnose Brain Tumour"),
  ]

  # Sends the classification request to the Cohere model
  user_intent = co.classify(
    model='large',
    inputs=[user_message],
    examples=examples
  )

  return user_intent.classifications[0].prediction

