import streamlit as st
import pickle
import string
import nltk.corpus
import nltk
from nltk.stem.porter import PorterStemmer

ps= PorterStemmer
text=[]
def transform_text (text):
 text = text.lower()
 text = nltk.word_tokenize(text)

y = []
for i in text:
  if i.isalnum():
   y.append(i)

test = y[:]
y.clear()

for i in text:
      y.append(ps.stem(i))



tfidf=pickle.load(open(vectorizer_utf8.pkl,rb))
model=pickle.load(open(utf-8-model.pkl,rb))

st.title("Email/SMS Spam Classifier")

input_sms= st.text_input("Enter the message")

transformed_sms=transform_text(input_sms)
vector_input= tfidf.transform([transformed_sms])

result=model.predict(vector_input)[0]

if result==1:
    st.header='Spam'
else:
    st.header='Non Spam'
