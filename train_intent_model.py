import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load dataset
df = pd.read_csv("craigslist_bargains_train.csv")

# Extract intent-labeled buyer utterances
examples = []
for text in df["text"].dropna():
    lines = text.split("\n")
    for line in lines:
        if "Buyer:" in line:
            msg = line.replace("Buyer:", "").strip().lower()
            if any(w in msg for w in ["price", "lakh", "rs", "offer", "can you", "get it", "deal for"]):
                intent = "offer"
            elif any(w in msg for w in ["too low", "too much", "expensive", "cheap", "not enough"]):
                intent = "counter"
            elif any(w in msg for w in ["ok", "deal", "fine", "confirm", "accepted", "yes"]):
                intent = "accept"
            elif any(w in msg for w in ["no", "pass", "not interested", "skip", "leave"]):
                intent = "reject"
            elif any(w in msg for w in ["hi", "hello", "hey"]):
                intent = "greet"
            else:
                continue
            examples.append((msg, intent))

# Create DataFrame and sample
intent_df = pd.DataFrame(examples, columns=["message", "intent"]).drop_duplicates().sample(n=500, random_state=42)

# Train model
X = intent_df["message"]
y = intent_df["intent"]
vec = CountVectorizer()
X_vec = vec.fit_transform(X)

clf = MultinomialNB()
clf.fit(X_vec, y)

# Save
with open("intent_model.pkl", "wb") as f:
    pickle.dump(clf, f)
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vec, f)

print("✅ Saved intent_model.pkl and vectorizer.pkl trained on Craigslist data")
