import streamlit as st
import pickle

with open('pkl/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('pkl/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

st.set_page_config(page_title="Spam SMS Classifier", layout="centered")

st.title("📱 Spam SMS Classifier")
st.write("Enter a message below to check if it's Spam or Not.")

user_input = st.text_area("✉️ Message", height=150)

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message to classify.")
    else:
        
        input_vector = vectorizer.transform([user_input]).toarray()

        
        prediction = model.predict(input_vector)[0]

        
        if prediction == 1:
            st.error("🚫 This message is **SPAM**.")
        else:
            st.success("✅ This message is **NOT SPAM**.")
