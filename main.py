import pandas as pd
import numpy as np
import random

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

urls_data = pd.read_csv("urldata.csv")

type(urls_data)

print(urls_data.head(10))
#URLs and labels (good or bad)

print("Missing data: ", urls_data.isnull().sum().sum())
#Check for missing data

#Tokenizer
def makeTokens(f):
    tkns_byslash = str(f.encode('utf-8')).split('/')
    total_tokens = []
    for i in tkns_byslash:
        tokens = str(i).split('-')
        tkns_bydot = []
        for j in range(0,len(tokens)):
            temp_tokens = str(tokens[j]).split('.')
            tkns_bydot = tkns_bydot + temp_tokens
        total_tokens = total_tokens + tokens + tkns_bydot
    total_tokens = list(set(total_tokens))
            if 'com' in total_tokens:
                total_tokens.remove('com')
            return total_tokens

y = urls_data["label"]

url_list = urls_data["url"]

vectorizer = TfidfVectorizer(tokenizer=makeTokens)

X = vectorizer.fit_transform(url_list)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

logit = LogisticRegression()
logit.fit(X_train, y_train)

print("Test Accuracy ", logit.score(X_test, y_test))
print("Train Accuracy ",logit.score(X_train, y_train))


X_predict = ["URL1.com",
"URL2.com",
"URL3.com",
"..."]
#The URLs that you want to analyze

X_predict = vectorizer.transform(X_predict)
new_predict = logit.predict(X_predict)
print("Scan Results: ", new_predict)
