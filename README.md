# 💬 Mental-Health-Prediction-and-AI-based-Suggestion-System 🌈

> _“Even a small push in the right direction can save a life.”_  

---

## 🧠 Project Overview  

**Mental-Health-Prediction-and-AI-based-Suggestion-System** is an intelligent chatbot designed to detect emotions like **depression, anxiety, sadness, anger, or happiness** from social media text and offer **personalized support** to uplift the user’s mood.  

Built using **CatBoost** for emotion classification and **GPT-powered responses** from `openai/gpt-oss-120b` (via GroqCloud), the system suggests jokes, quotes, music playlists, and mental health helpline info — all through a friendly chat-style Streamlit interface inspired by **Twitter’s UI**.  

---

## 🚀 Features  

✨ **Emotion Detection** — Classifies text into *Happy*, *Sad/Depressed*, *Suicidal*, *Angry*, or *Anxious*.  
💬 **AI-Generated Comfort** — GPT tailors meaningful replies to soothe the user.  
🎵 **Mood Boosting Content** — Shares jokes, quotes, and playlists.  
📞 **India Helpline Integration** — Displays helpline info for critical cases.  
🌙 **Dark Mode UI** — Sleek, modern black-themed interface.  
⚡ **Fast & Lightweight** — Powered by CatBoost + TF-IDF Vectorizer.  

---

## 🏗️ Tech Stack  

| Component | Technology |
|------------|-------------|
| ML Model | CatBoost |
| Text Vectorization | TF-IDF |
| AI Suggestions | openai/gpt-oss-120b (GroqCloud) |
| Interface | Streamlit |
| Deployment | Hugging Face / Local / VS Code |

---

## 🖥️ Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/kishorekumarbn/Mental-Health-Prediction-and-AI-based-Suggestion-System.git
cd Mental-Health-Prediction-and-AI-based-Suggestion-System

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Add Model Files
Place the following in the project root:
vectorizer.pkl  
catboost_model.pkl  

4️⃣ Set Your Groq API Key

Option A — Locally
Create a .env file:
GROQ_API_KEY=your_api_key_here

Option B — Hugging Face
Add it in “Settings → Secrets” as GROQ_API_KEY.

▶️ Run the App
streamlit run streamlit_app.py
Then open:
👉 http://localhost:8501

💡 How It Works

1️⃣ User enters a post or thought.
2️⃣ Model predicts the emotional label using CatBoost.
3️⃣ Based on emotion → GPT generates an uplifting response.
4️⃣ Streamlit displays it beautifully with emoji and cards.

❤️ For Suicidal or Critical Thoughts

If you or someone you know is in distress, please reach out for help.
📞 India Helpline: AASRA — 91-9820466726
24x7 Support: Snehi — 91-9582208181

🌟 Future Enhancements

🔊 Voice-based emotional chat

💾 User journaling and progress tracking

🎧 Spotify / YouTube integration

🧘 Mental health resource recommendations

👨‍💻 Author

Kishore Kumar B N
Data Science & AI Enthusiast

⭐ Show Your Support

If you like this project,
leave a ⭐ on GitHub and help spread awareness about AI for mental health!



