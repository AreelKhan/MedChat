from doc import Documents
import json
import pickle

# read webmd_links.json
with open("webmd_links.json", "r") as f:
    sources = json.load(f)

documents = Documents(sources)

# save documents
with open("docs.pkl", "wb") as f:
    pickle.dump(documents, f)