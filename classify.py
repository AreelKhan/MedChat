import cohere
import os
from cohere.responses.classify import Example

COHERE_API_KEY = "xxgLc7lYofMMXtHhUcqM60iPlRWvjHQ4Syy6ttKz"
os.environ["COHERE_API_KEY"] = COHERE_API_KEY

examples=[
  Example("Make diagnosis", "Spam"),
  Example("'Hello, open to this?'", "Spam"),
  Example("I need help please wire me $1000 right now", "Spam"),
  Example("Nice to know you ;)", "Spam"),
  Example("Please help me?", "Spam"),
  Example("Your parcel will be delivered today", "Not spam"),
  Example("Review changes to our Terms and Conditions", "Not spam"),
  Example("Weekly sync notes", "Not spam"),
  Example("'Re: Follow up from today's meeting'", "Not spam"),
  Example("Pre-read for tomorrow", "Not spam"),
]

inputs=[
  "Confirm your email address",
  "hey i need u to send some $",
]
response = co.classify(
  inputs=inputs,
  examples=examples,
)
print(response)