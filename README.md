# AI-Powered Multilingual Learning Assistant

## 💡 Project Overview
This project is an AI-based learning assistant that translates Hindi text into English and converts it into speech. It is designed to help students, especially in rural or non-English-speaking areas, better understand educational content by breaking language barriers.

## 🚀 Features
- Translate text from Hindi to English using a pre-trained MarianMT model
- Convert translated English text into audio using gTTS
- Simple and interactive Streamlit web interface

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python
- **Translation Model:** Helsinki-NLP/opus-mt-hi-en (via HuggingFace Transformers)
- **Text-to-Speech:** gTTS (Google Text-to-Speech)

## 📦 Requirements
See `requirements.txt` for full dependencies.

## 📂 File Structure
```
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # Project overview and instructions
```

## 📈 How to Run Locally
1. Clone this repository  
2. Install dependencies:  
   ```
   pip install -r requirements.txt
   ```
3. Run the app:  
   ```
   streamlit run app.py
   ```

## 🌐 Live Demo
[Click here to view the live app](https://your-streamlit-link-here)

## 📄 License
This project is open-source and free to use under the MIT License.