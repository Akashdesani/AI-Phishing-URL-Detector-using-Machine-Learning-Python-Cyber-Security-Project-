import re

def extract_features(url):
    
    length = len(url)

    has_https = 1 if "https" in url else 0

    suspicious_words = ["login","verify","bank","secure","update"]
    
    suspicious = 0
    for word in suspicious_words:
        if word in url:
            suspicious = 1

    dots = url.count(".")

    return [length, has_https, suspicious, dots]