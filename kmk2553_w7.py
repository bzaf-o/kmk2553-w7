import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("🌟 Interactive Mental Health Modelling Tool")

# Introduction
st.write("""
This tool allows you to explore how different factors influence mental health. Adjust the sliders below to see 
how changes in lifestyle and environment affect the overall mental health score.
""")

# Sidebar for Factor Adjustments
st.sidebar.header("Adjust Factors")
stress = st.sidebar.slider("😰 Stress Levels (Higher is worse)", 0, 100, 50)
physical_activity = st.sidebar.slider("🏃‍♂️ Physical Activity (Higher is better)", 0, 100, 50)
sleep_quality = st.sidebar.slider("😴 Sleep Quality (Higher is better)", 0, 100, 50)
social_interaction = st.sidebar.slider("🫂 Social Interaction (Higher is better)", 0, 100, 50)
nutrition = st.sidebar.slider("🥗 Nutrition Quality (Higher is better)", 0, 100, 50)
coping_mechanisms = st.sidebar.slider("🧘‍♂️ Coping Mechanisms (Higher is better)", 0, 100, 50)

# Define Weights for Each Factor
weights = {
    "Stress": -8.0,  # More strongly negative
    "Physical Activity": 6.5,
    "Sleep Quality": 6.6,
    "Social Interaction": 6.4,
    "Nutrition": 6.3,
    "Coping Mechanisms": 6.8
}

# Normalize Inputs
inputs = {
    "Stress": stress,
    "Physical Activity": physical_activity,
    "Sleep Quality": sleep_quality,
    "Social Interaction": social_interaction,
    "Nutrition": nutrition,
    "Coping Mechanisms": coping_mechanisms
}

normalized_inputs = {key: val / 100 for key, val in inputs.items()}

# Calculate Mental Health Score
mental_health_score = sum(
    normalized_inputs[key] * weights[key] for key in normalized_inputs
)

# Scale to 0-100
mental_health_score_scaled = np.clip((mental_health_score + 4) * 10, 0, 100)

# Display Overall Mental Health Score
st.subheader("Overall Mental Health Score 🧘‍♀️")
st.write(f"**Score:** {mental_health_score_scaled:.1f} / 100")

# Horizontal Progress Bar
st.progress(int(mental_health_score_scaled))

# Dynamic Feedback Based on Score
st.markdown("### Mental Health State")
if mental_health_score_scaled >= 80:
    st.success("😊 You're doing well!")
elif 50 <= mental_health_score_scaled < 80:
    st.info("🙂 Keep up the good work!")
elif 20 <= mental_health_score_scaled < 50:
    st.warning("😟 Things are a bit rough. Take some time for yourself!")
else:
    st.error("💔 Be gentle with yourself! Seek support if needed.")

# Visualize Factor Contributions
st.subheader("Factor Contributions")
contributions = pd.DataFrame({
    "Factor": list(normalized_inputs.keys()),
    "Contribution": [normalized_inputs[key] * weights[key] for key in normalized_inputs]
})

# Horizontal Bar Plot for Contributions
fig, ax = plt.subplots(figsize=(8, 5))
contributions.set_index("Factor").plot(kind="barh", legend=False, ax=ax, color='skyblue')
ax.set_xlabel("Contribution to Mental Health Score")
ax.set_title("Factor Contributions")
st.pyplot(fig)
