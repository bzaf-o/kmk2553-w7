import streamlit as st
import numpy as np  # Import numpy

# Set page config
st.set_page_config(page_title="🐰 Natural Selection Model 🐰", layout="wide")

# Emojis for the factors
rabbit_emoji = "🐇"
grass_emoji = "🌱"

# Utility function to get text color based on value
def get_text_color(value):
    if value < 30:
        return "red"
    elif value > 80:
        return "orange"
    else:
        return "green"

# Helper function for dynamic status messages
def get_status_message(factor, value):
    if value < 30:
        return f"Low {factor} level!"
    elif value > 80:
        return f"High {factor} level!"
    return "Balanced levels."

# Sidebar slider for water
st.sidebar.header("Adjust Water Level")
water = st.sidebar.slider("💧 Water Level", 0, 100, 50)

# Calculate other factors based on water level
large_rabbits = max(0, min(100, water + np.random.randint(-10, 10)))
medium_rabbits = max(0, min(100, water + np.random.randint(-5, 15)))
small_rabbits = max(0, min(100, water + np.random.randint(-15, 5)))
large_grass = max(0, min(100, water + np.random.randint(-10, 10)))
medium_grass = max(0, min(100, water + np.random.randint(-5, 15)))
small_grass = max(0, min(100, water + np.random.randint(-15, 5)))

# Helper function for rendering bars
def render_bar(label, value, color, emoji):
    bar_html = f"""
    <div style="display: flex; align-items: center; margin-bottom: 10px;">
        <div style="width: 150px; font-weight: bold;">{emoji} {label}:</div>
        <div style="flex: 1; background-color: {color}; height: 20px; width: {value}%; border-radius: 5px;"></div>
        <div style="margin-left: 10px; font-size: 12px;">{value}%</div>
    </div>
    """
    st.markdown(bar_html, unsafe_allow_html=True)

    text_color = get_text_color(value)
    status_message = get_status_message(label, value)
    status_html = f"""
    <div style="color: {text_color}; padding: 5px; margin-bottom: 20px; font-size: 12px;">
        {status_message}
    </div>
    """
    st.markdown(status_html, unsafe_allow_html=True)

# Layout for factors
st.header("Natural Selection Factors")

col_rabbits, col_grass = st.columns(2)

with col_rabbits:
    st.subheader("Rabbit Population")
    render_bar("Large Rabbits", large_rabbits, "#FB928E", rabbit_emoji)
    st.markdown("---")
    render_bar("Medium Rabbits", medium_rabbits, "#FFB8BF", rabbit_emoji)
    st.markdown("---")
    render_bar("Small Rabbits", small_rabbits, "#FBC4BF", rabbit_emoji)

with col_grass:
    st.subheader("Grass Types")
    render_bar("Large Grass", large_grass, "#0f2310", grass_emoji)
    st.markdown("---")
    render_bar("Medium Grass", medium_grass, "#265628", grass_emoji)
    st.markdown("---")
    render_bar("Small Grass", small_grass, "#449e48", grass_emoji)
