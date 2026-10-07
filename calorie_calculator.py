import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Calorie Calculator",
    page_icon="🥗",
    layout="centered"
)

st.title("🥗 Calorie Calculator")
st.write("Calculate your estimated daily calorie requirement.")

# Personal details
st.subheader("👤 Personal Details")

age = st.number_input(
    "Age (years)",
    min_value=1,
    max_value=120,
    value=20
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

weight = st.number_input(
    "Weight (kg)",
    min_value=1.0,
    max_value=300.0,
    value=60.0
)

height = st.number_input(
    "Height (cm)",
    min_value=50.0,
    max_value=250.0,
    value=165.0
)

# Activity level
st.subheader("🏃 Activity Level")

activity = st.selectbox(
    "Select your activity level",
    [
        "Sedentary - Little or no exercise",
        "Lightly Active - Exercise 1-3 days/week",
        "Moderately Active - Exercise 3-5 days/week",
        "Very Active - Exercise 6-7 days/week",
        "Extra Active - Very hard exercise/physical job"
    ]
)

# Activity multipliers
activity_factors = {
    "Sedentary - Little or no exercise": 1.2,
    "Lightly Active - Exercise 1-3 days/week": 1.375,
    "Moderately Active - Exercise 3-5 days/week": 1.55,
    "Very Active - Exercise 6-7 days/week": 1.725,
    "Extra Active - Very hard exercise/physical job": 1.9
}

# Calculate button
if st.button("🧮 Calculate Calories", use_container_width=True):

    # Calculate BMR using the Mifflin-St Jeor equation
    if gender == "Male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    # Calculate TDEE
    activity_factor = activity_factors[activity]
    calories = bmr * activity_factor

    st.divider()

    # Display results
    st.subheader("📊 Your Results")

    st.metric(
        "Estimated Daily Calories",
        f"{calories:.0f} kcal"
    )

    st.write(f"**BMR:** {bmr:.0f} kcal/day")
    st.write(f"**Activity Level:** {activity}")

    # Simple interpretation
    st.subheader("💡 Interpretation")

    st.info(
        f"Your estimated daily calorie requirement is "
        f"approximately **{calories:.0f} kcal per day** "
        f"to maintain your current weight at the selected "
        f"activity level."
    )

    st.warning(
        "This is an estimate for educational purposes, not medical advice. "
        "Individual calorie needs can vary."
    )
