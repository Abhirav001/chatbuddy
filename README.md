# 🤖 AI Chatbot using Streamlit & OpenAI

An interactive AI chatbot built using **Streamlit** and **OpenAI API**.
This app provides a clean chat interface, maintains conversation history, and displays responses in real-time.

---

## 🚀 Features

* 💬 Interactive chat interface
* 🧠 AI-powered responses using OpenAI
* 🕒 Chat history with timestamps
* 🎨 Custom UI styling with CSS
* 📌 Sidebar chat history viewer
* ⚡ Fast and lightweight Streamlit app

---

## 🗂️ Project Structure

```bash
chatbot-project/
│
├── chatbot.py      # Main Streamlit app
├── README.md
└── requirements.txt (optional)
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2️⃣ Install dependencies

```bash
pip install streamlit openai
```

---

## 🔑 Setup API Key

⚠️ **Important:** Never expose your API key publicly.

### ❌ Current (Not Secure)

```python
client = OpenAI(api_key="your_api_key")
```

### ✅ Recommended (Using Environment Variables)

**Windows:**

```bash
setx OPENAI_API_KEY "your_api_key"
```

**Linux/Mac:**

```bash
export OPENAI_API_KEY=your_api_key
```

Then update your code:

```python
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

---

## ▶️ Run the Application

```bash
streamlit run chatbot.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. User enters a message
2. Message is sent to OpenAI API (`gpt-4o-mini`)
3. AI generates a response
4. Both user and AI messages are stored in session state
5. Chat is displayed with timestamps

---

## 🎨 UI Features

* Gradient user messages
* Clean assistant response design
* Scrollable chat container
* Sidebar chat history

---

## ⚠️ Security Notes

* ❌ Do NOT commit API keys to GitHub
* ✅ Use `.env` or environment variables
* ✅ Add `.gitignore` to exclude sensitive files

---

## 📌 Future Improvements

* Add login/authentication
* Save chat history to database
* Add file upload support
* Deploy on cloud (Streamlit Cloud / AWS)

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Abhirav Sharma**

---

⭐ If you like this project, don’t forget to star the repo!
