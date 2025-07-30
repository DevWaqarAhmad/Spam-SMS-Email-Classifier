import streamlit as st
import pickle

# Page config
st.set_page_config(page_title="Spam SMS Classifier", layout="centered")

# Load model and vectorizer
with open('pkl/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('pkl/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# --- Custom styling ---
st.markdown("""
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: ##FFFFFF;  /* Blue */
            text-align: center;
        }
        .subtitle {
            font-size: 18px;
            color: #444;  /* Dark gray */
            text-align: center;
            margin-bottom: 30px;
        }
        .footer {
            font-size: 14px;
            color: #FFFFFF;  /* Light gray */
            text-align: center;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)


# --- App Header ---
st.markdown('<div class="title">📱 Spam SMS Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Spam Detection in One Click — AI at Your Service</div>', unsafe_allow_html=True)

# --- Input ---
user_input = st.text_area("Enter your message below:", height=150)

if st.button("⚡ Start Scan Message"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message to classify.")
    else:
        # Transform and predict
        input_vector = vectorizer.transform([user_input]).toarray()
        prediction = model.predict(input_vector)[0]

        # Display result
        if prediction == 1:
            st.error("🚫 This message is **SPAM**.\nBe cautious and do not click suspicious links!")
        else:
            st.success("✅ This message is **NOT SPAM**.\nLooks safe and normal.")

# Footer
st.markdown('<div class="footer">Crafted with care using Streamlit and Machine Learning</div>', unsafe_allow_html=True)
