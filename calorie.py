import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Calorie Calculator",
    page_icon="🥗",
    layout="centered"
)

# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------
st.title("🥗 Calorie Calculator")
st.write("Calculate your estimated daily calorie requirement easily.")

st.divider()

# ---------------------------------------------------------
# PERSONAL DETAILS
# ---------------------------------------------------------
st.subheader("👤 Personal Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=20
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0,
        max_value=300.0,
        value=60.0,
        step=0.5
    )

with col2:
    height = st.number_input(
        "Height (cm)",
        min_value=50.0,
        max_value=250.0,
        value=165.0,
        step=0.5
    )

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

# ---------------------------------------------------------
# ACTIVITY LEVEL
# ---------------------------------------------------------
st.subheader("🏃 Activity Level")

activity = st.selectbox(
    "Select your usual activity level",
    [
        "Sedentary - Little or no exercise",
        "Lightly Active - Exercise 1-3 days/week",
        "Moderately Active - Exercise 3-5 days/week",
        "Very Active - Exercise 6-7 days/week",
        "Extra Active - Very hard exercise / physical job"
    ]
)

# Activity multipliers
activity_multiplier = {
    "Sedentary - Little or no exercise": 1.2,
    "Lightly Active - Exercise 1-3 days/week": 1.375,
    "Moderately Active - Exercise 3-5 days/week": 1.55,
    "Very Active - Exercise 6-7 days/week": 1.725,
    "Extra Active - Very hard exercise / physical job": 1.9
}

# ---------------------------------------------------------
# CALCULATE BUTTON
# ---------------------------------------------------------
st.divider()

if st.button("🧮 Calculate Calories", use_container_width=True):

    # -----------------------------------------------------
    # BMR CALCULATION
    # Mifflin-St Jeor Equation
    # -----------------------------------------------------
    if gender == "Male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    # -----------------------------------------------------
    # TDEE CALCULATION
    # -----------------------------------------------------
    calorie_requirement = bmr * activity_multiplier[activity]

    # -----------------------------------------------------
    # RESULT
    # -----------------------------------------------------
    st.success("✅ Calculation Completed!")

    st.subheader("🔥 Your Estimated Daily Calorie Requirement")

    st.metric(
        label="Estimated Calories / Day",
        value=f"{calorie_requirement:,.0f} kcal"
    )

    st.info(
        f"Your estimated daily calorie requirement is approximately "
        f"**{calorie_requirement:,.0f} kcal/day** based on the information provided."
    )

    # -----------------------------------------------------
    # ADDITIONAL INFORMATION
    # -----------------------------------------------------
    st.subheader("📊 Your Calculation")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Basal Metabolic Rate (BMR)**")
        st.write(f"🔥 {bmr:,.0f} kcal/day")

    with col2:
        st.write("**Activity Multiplier**")
        st.write(f"🏃 {activity_multiplier[activity]}")

    # -----------------------------------------------------
    # INTERPRETATION
    # -----------------------------------------------------
    st.subheader("💡 Simple Interpretation")

    st.write(
        f"Your body is estimated to need around "
        f"**{calorie_requirement:,.0f} calories per day** "
        f"to support your normal body functions and selected activity level."
    )

    st.caption(
        "This is an estimate, not a medical or dietary prescription. "
        "Actual calorie needs can vary between individuals."
    )