import streamlit as st
import numpy as np

# Title and Description
st.title("Natural Selection Dynamics 🌱🐇")
st.markdown("""
Explore how different factors affect natural selection in a rabbit population. 
Adjust sliders and toggle the presence of a dam to see how the ecosystem reacts.
""")

# Sidebar for Interaction
st.sidebar.header("Simulation Controls")

# Dam toggle and water slider
dam_present = st.sidebar.checkbox("Dam on the River 🌊")
if dam_present:
    water_level = 0
    st.sidebar.write("Water level is controlled by the dam.")
else:
    water_level = st.sidebar.slider("Amount of Water 💧", 0, 100, 50)

# Rabbit population sliders
large_rabbits = st.sidebar.slider("Population of Large Rabbits 🐇 (Large)", 0, 100, 50)
medium_rabbits = st.sidebar.slider("Population of Medium Rabbits 🐇 (Medium)", 0, 100, 50)
small_rabbits = st.sidebar.slider("Population of Small Rabbits 🐇 (Small)", 0, 100, 50)

# Grass availability sliders
grass_a = st.sidebar.slider("Amount of Grass A 🌾 (Preferred by Small Rabbits)", 0, 100, 50)
grass_b = st.sidebar.slider("Amount of Grass B 🌿 (Preferred by Medium Rabbits)", 0, 100, 50)
grass_c = st.sidebar.slider("Amount of Grass C 🌱 (Preferred by Large Rabbits)", 0, 100, 50)

# Helper function for severity color
def get_severity_color(value):
    if value < 30:
        return "#ff4d4d"  # Red
    elif value > 80:
        return "#3ae374"  # Green
    else:
        return "#ffa500"  # Orange

# Display bars with reactive text
def display_factor(name, value, color, emoji, description):
    st.markdown(f"**{name} {emoji}**")
    st.progress(value)
    severity_color = get_severity_color(value)
    st.markdown(
        f"""
        <div style="background-color:{severity_color};padding:5px;border-radius:5px;">
        <strong>{description}</strong>
        </div>
        """, unsafe_allow_html=True
    )

# Ecosystem Analysis
water_text = "Not enough water to sustain the ecosystem!" if water_level < 30 else "Water levels are adequate." if water_level <= 80 else "Plentiful water for the ecosystem!"
display_factor("Water Level", water_level, "#87CEEB", "💧", water_text)

large_rabbit_text = "Too many large rabbits!" if large_rabbits > 80 else "Balanced population of large rabbits." if large_rabbits > 30 else "Low population of large rabbits!"
display_factor("Large Rabbits", large_rabbits, "#FC72A5", "🐇", large_rabbit_text)

medium_rabbit_text = "Too many medium rabbits!" if medium_rabbits > 80 else "Balanced population of medium rabbits." if medium_rabbits > 30 else "Low population of medium rabbits!"
display_factor("Medium Rabbits", medium_rabbits, "#F99DBC", "🐇", medium_rabbit_text)

small_rabbit_text = "Too many small rabbits!" if small_rabbits > 80 else "Balanced population of small rabbits." if small_rabbits > 30 else "Low population of small rabbits!"
display_factor("Small Rabbits", small_rabbits, "#FEC206", "🐇", small_rabbit_text)

grass_a_text = "Too little Grass A for small rabbits!" if grass_a < 30 else "Adequate Grass A for small rabbits." if grass_a <= 80 else "Plentiful Grass A for small rabbits!"
display_factor("Grass A", grass_a, "#a3b18a", "🌾", grass_a_text)

grass_b_text = "Too little Grass B for medium rabbits!" if grass_b < 30 else "Adequate Grass B for medium rabbits." if grass_b <= 80 else "Plentiful Grass B for medium rabbits!"
display_factor("Grass B", grass_b, "#588157", "🌿", grass_b_text)

grass_c_text = "Too little Grass C for large rabbits!" if grass_c < 30 else "Adequate Grass C for large rabbits." if grass_c <= 80 else "Plentiful Grass C for large rabbits!"
display_factor("Grass C", grass_c, "#3a5a40", "🌱", grass_c_text)

# Notes
st.info("Use the controls on the left to adjust ecosystem factors and observe their effects!")
