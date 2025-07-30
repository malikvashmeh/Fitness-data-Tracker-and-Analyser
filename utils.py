# Predict & Gemini Response

import joblib
# joblib: For loading the saved ML model.

import os 
# os: For accessing environment variables.

import openai
# openai: For OpenAI API access

import google.generativeai as genai
# google.generativeai: For Google Gemini API access

from dotenv import load_dotenv
# dotenv: Loads your .env file so your API key is available in code



# API Key Loading
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# Reads your .env file and sets API keys.

# This does not produce any output — it silently loads the keys.



# Load ML Model
def load_model():
    return joblib.load("model/fitness_model.pkl")
# Loads your saved model from disk.

# Returns the model but does not print or display anything on its own.


# Make Predictions
def predict_progress(model, input_data):
    return model.predict([input_data])[0]
# Takes the model and input data, makes a prediction, and returns the result.
# Takes in the model and a single row of data (as a list).

# Returns the predicted class: 1 = on track, 0 = not on track

# Also returns a value but produces no output unless printed elsewhere


# Get Motivational Response (LLM)
def get_motivational_response(input_data, prediction):
    prompt = f"""
User fitness data: {input_data}
Prediction: {'On track ✅' if prediction else 'Off track ❌'}

Give a short, friendly motivational coaching message, with one fitness tip and one meal idea.
"""

    # Try OpenAI first, then fall back to Google Gemini
    try:
        # Try OpenAI
        if openai.api_key and openai.api_key != "your_openai_api_key_here":
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content
    except Exception as e:
        pass  # Fall back to Google Gemini
    
    try:
        # Try Google Gemini
        if os.getenv("GOOGLE_API_KEY") and os.getenv("GOOGLE_API_KEY") != "your_google_api_key_here":
            model = genai.GenerativeModel('gemini-1.5-pro')
            response = model.generate_content(prompt)
            return response.text
    except Exception as e:
        pass  # Fall back to default message
    
    # Default response if no API keys are set
    if prediction:
        responses = [
            "🎯 Excellent work! You're crushing your fitness goals. 💪 Tip: Try adding some strength training to your routine. 🍽️ Meal idea: Salmon with sweet potato and steamed broccoli.",
            "🚀 You're on fire! Your consistency is paying off. 💪 Tip: Mix up your cardio with some HIIT intervals. 🍽️ Meal idea: Turkey and avocado wrap with a side salad.",
            "⭐ Amazing progress! You're building healthy habits. 💪 Tip: Focus on proper form during your workouts. 🍽️ Meal idea: Quinoa bowl with grilled chicken and roasted vegetables.",
            "🏆 Outstanding! You're setting a great example. 💪 Tip: Don't forget to stretch after your workouts. 🍽️ Meal idea: Greek yogurt parfait with granola and fresh berries."   
        ]
        import random
        return random.choice(responses)
    else:
        responses = [
            "💪 Every journey has ups and downs - you've got this! 🔥 Tip: Start with a 20-minute walk today. 🍽️ Meal idea: Greek yogurt with berries and a handful of nuts.",
            "🌟 Small steps lead to big changes. Let's get back on track! 🔥 Tip: Try a 15-minute home workout. 🍽️ Meal idea: Oatmeal with banana and honey.",
            "🌈 Progress isn't always linear - that's totally normal! 🔥 Tip: Take the stairs instead of the elevator. 🍽️ Meal idea: Smoothie bowl with protein powder.",
            "🎯 You're stronger than any setback. Let's bounce back! 🔥 Tip: Do some gentle stretching today. 🍽️ Meal idea: Grilled cheese with tomato soup."
        ]
        import random
        return random.choice(responses)
