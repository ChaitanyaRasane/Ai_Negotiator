import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
df = pd.read_csv("chat_dataset_craigslist.csv").sample(n=2000)

# Train
X = df["message"]
y = df["response"]

vec = TfidfVectorizer()
X_vec = vec.fit_transform(X)

clf = LogisticRegression(max_iter=1000)
clf.fit(X_vec, y)

# Save
with open("response_model.pkl", "wb") as f:
    pickle.dump(clf, f)
with open("response_vectorizer.pkl", "wb") as f:
    pickle.dump(vec, f)
