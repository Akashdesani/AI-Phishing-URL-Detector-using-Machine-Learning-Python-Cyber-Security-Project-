import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_model():
    
    data = pd.read_csv("dataset.csv")

    X = data.drop("label", axis=1)
    y = data["label"]

    model = RandomForestClassifier()
    model.fit(X,y)

    pickle.dump(model, open("phishing_model.pkl","wb"))

def load_model():
    return pickle.load(open("phishing_model.pkl","rb"))