# Fitness Coach Guidance

An AI-powered fitness coaching web application that analyzes your daily fitness metrics and provides personalized motivational coaching.

## 🚀 Quick Start

### 1. Activate Virtual Environment
```bash
source env/bin/activate
```

### 2. Run the Application
```bash
streamlit run app.py
```

### 3. Open in Browser
- **Local URL**: http://localhost:8501
- **Network URL**: http://192.168.100.28:8501

## 📋 What You Need

### Required Files
- ✅ `app.py` - Main application
- ✅ `utils.py` - Core functions
- ✅ `train_model.py` - Model training
- ✅ `requirements.txt` - Dependencies
- ✅ `.env` - API keys (optional)
- ✅ `data/user_data.csv` - Training data
- ✅ `model/fitness_model.pkl` - Trained model

### Optional: AI Features
To enable AI-generated responses, add your API keys to `.env`:
```bash
# OpenAI API Key (get from https://platform.openai.com/api-keys)
OPENAI_API_KEY=your_openai_api_key_here

# Google API Key (get from https://makersuite.google.com/app/apikey)
GOOGLE_API_KEY=your_google_api_key_here
```

## 🎯 How to Use

1. **Enter Your Daily Stats:**
   - Age, Weight, Calories, Sleep, Steps, Workout, Mood

2. **Click "Check My Progress"**

3. **Get Personalized Coaching:**
   - Smart prediction (On track ✅ or Off track ⚠️)
   - Motivational message
   - Fitness tip
   - Meal suggestion

## 🔧 Troubleshooting

### If the app doesn't start:
```bash
# Install dependencies
pip install -r requirements.txt

# Retrain the model
python train_model.py

# Try again
streamlit run app.py
```

### If AI responses don't work:
- Check your API keys in `.env` file
- App works with default responses even without API keys

## 📁 Project Structure
```
FItness coach Guidance/
├── app.py                    # Web application
├── utils.py                  # Core functions
├── train_model.py           # Model training
├── requirements.txt         # Dependencies
├── .env                     # API keys
├── data/user_data.csv      # Training data
└── model/fitness_model.pkl # Trained model
```

## 🎉 Features

- ✅ **Machine Learning** - Smart fitness predictions
- ✅ **AI Coaching** - Personalized motivational messages
- ✅ **Web Interface** - Easy-to-use Streamlit app
- ✅ **Fallback System** - Works without internet/API keys
- ✅ **Varied Responses** - Different messages each time

---

**Enjoy your personalized fitness coaching! 💪** 