# streamlit app

# app.py
import streamlit as st
from utils import load_model, predict_progress, get_motivational_response
# Loading the ML model

# Predicting fitness progress

# Getting an LLM-based response


st.set_page_config(page_title="Fitness Goal Coach", layout="centered")
st.title("Fitness Goal Coach")

st.markdown("Enter your daily stats to see if you're on track and get motivational coaching.")

# Input form
# This creates a form UI, which groups all user input widgets.
# Only runs when the "Check My Progress" button is clicked

with st.form("user_input"):
    age = st.number_input("⏳Age", 10, 100, 30)
    weight = st.number_input("💪Current Weight (㎏)", 30.0, 200.0, 80.0)
    calories = st.number_input("🍴Calories Consumed", 1000, 5000, 2200)
    sleep = st.number_input("💤Sleep Hours", 0.0, 12.0, 7.0)
    steps = st.number_input("👣Steps Walked", 0, 30000, 8000)
    workout = st.number_input("🏋🏽Workout Duration (mins)", 0, 300, 45)
    mood = st.slider("🥀Mood (1-10)", 1, 10, 6)
    submitted = st.form_submit_button("🔍Check My Progress")

if submitted: #This block runs only after the user clicks the button.
    features = [age, weight, calories, sleep, steps, workout, mood] #Collects all input values into a list, in the same order the model expects.
    model = load_model() #Loads the fitness_model.pkl file using joblib.
    prediction = predict_progress(model, features) #Runs the model on the user's input and returns 1(on track) or 0(not on track)
    
    if prediction: #Displays a green success box or a yellow warning box based on prediction.
        st.success("✅ You are on track with your fitness goals!")
    else: #Displays a yellow warning box if the user is not on track.
        st.warning("⚠️ You might be falling off track. Let’s adjust!")

    with st.spinner("🧠 Generating personalized coaching..."): #Shows a spinner while the LLM generates a response.
        message = get_motivational_response(features, prediction)
        st.markdown(f"**💬 Coach Says:**\n\n{message}")

# Shows a loading spinner while waiting for the LLM.

# Calls the Gemini API (or whatever LLM is configured) using the helper.

# When done, it prints a custom motivational message using markdown.

# ✅ Visible output:

# Spinner while thinking

# Text box that says:
# 💬 Coach Says:
# followed by the LLM-generated message

