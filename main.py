from features import extract_features
from model import load_model

def check_url(url):
    model = load_model()
    features = extract_features(url)
    prediction = model.predict([features])

    if prediction[0] == 1:
        print("⚠️ Warning: This URL is likely PHISHING!")
    else:
        print("✅ This URL appears SAFE.")

if __name__ == "__main__":
    url = input("Enter URL to check: ")
    check_url(url)