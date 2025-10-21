import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from catboost import CatBoostClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from groq import Groq

# ------------------------------------------------------------
# Setup and downloads
# ------------------------------------------------------------
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# ------------------------------------------------------------
# Load vectorizer and model
# ------------------------------------------------------------
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('catboost_model.pkl', 'rb') as f:
    model = pickle.load(f)

# ------------------------------------------------------------
# Text cleaning function (same as used in training)
# ------------------------------------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'@[\w_]+', '', text)
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    tokens = [word for word in text.split() if word not in stop_words]
    return ' '.join(tokens)

# ------------------------------------------------------------
# Groq Client Setup
# ------------------------------------------------------------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ------------------------------------------------------------
# Streamlit UI Configuration
# ------------------------------------------------------------
st.set_page_config(page_title=" Ai Suggestion System :)", page_icon="💙", layout="centered")

# Custom CSS for Twitter-like look
st.markdown(
"""
<style>
body { 
    background-color: #000000;  /* black background */
    color: #FFFFFF;             /* white text for contrast */
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
}
.main-title { 
    color: #1DA1F2; 
    text-align: center; 
    font-size: 40px; 
    font-weight: bold; 
    margin-bottom: 20px; 
}
.tweet-box { 
    background-color: #1E1E1E;  /* darker card for contrast */
    padding: 20px; 
    border-radius: 20px; 
    box-shadow: 0px 2px 10px rgba(0,0,0,0.5); 
    margin-top: 10px; 
}
.prediction { 
    font-size: 20px; 
    font-weight: 600; 
    color: #1DA1F2; 
    margin-top: 10px; 
}
.response-box { 
    background-color: #333333; 
    border-radius: 20px; 
    padding: 15px; 
    margin-top: 10px; 
    font-size: 18px; 
    color: #FFFFFF;
}
</style>
""",
unsafe_allow_html=True
)


# ------------------------------------------------------------
# App layout
# ------------------------------------------------------------
st.markdown('<div class="main-title">💙 Ai Based Suggestion System </div>', unsafe_allow_html=True)

username = st.text_input("Enter your name:", placeholder="e.g. Kishore")
user_text = st.text_area("What's on your mind? ( Feel Free to express with Us :) )", height=150)

if st.button("How Do I Sound ?"):
    if user_text.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        cleaned = clean_text(user_text)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)

        # Ensure prediction is a string, not array
        pred_label = str(prediction[0]) if hasattr(prediction, '__getitem__') else str(prediction)

        mood_emoji = {
            "Sad/Depressed": "😔",
            "Suicidal": "💔",
            "Anxious/Angry": "😡",
            "Positive": "😊",
            "Neutral": "😐"
        }

        emoji = mood_emoji.get(pred_label, "💭")
        st.markdown(f'<div class="tweet-box"><div class="prediction">{emoji} Detected Mood: {pred_label}</div></div>', unsafe_allow_html=True)

        # Compose prompt for Groq GPT model
        prompt = f"""
        You are a friendly AI companion. The user's detected emotion is '{pred_label}'.
        Respond as if talking to {username or 'your friend'} in a warm, friendly tone.
        Your goal: lift their spirits, calm their mind, and help them feel better.
        Suggest something meaningful — it could be a joke, motivational quote, calming playlist idea, or short pep talk.
        If emotion is 'Suicidal', include India's helpline number 9152987821 and a strong hopeful message.
        Be impactful, positive, and empathetic.
        """

        try:
            with st.spinner("Generating a supportive message..."):
                completion = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=1,
                    max_completion_tokens=500,
                    top_p=1,
                    reasoning_effort="medium"
                )

                response = completion.choices[0].message.content.strip()
                st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error generating response: {e}")

st.markdown("---")
st.caption("Developed with 💙 | Powered by CatBoost + Groq GPT-OSS-120B")
