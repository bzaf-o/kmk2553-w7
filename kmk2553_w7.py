import streamlit as st
import numpy as np

# Title and Description
st.title("Natural Selection Dynamics 🌱🐇")
st.markdown("""
Explore how the presence of a dam and water availability affect the ecosystem. 
Adjust sliders and see how populations and resources respond dynamically.
""")

# Sidebar for Interaction
st.sidebar.header("Simulation Controls")

# Dam toggle and water slider
dam_present = st.sidebar.checkbox("Dam on the River 🌊")
if dam_present:
    water_level = 20  # Fixed water level when dam is present
    st.sidebar.write("Water level is limited by the dam.")
else:
    water_level = st.sidebar.slider("Amount of Water 💧", 0, 100, 50)

# Reactive calculations based on water level
grass_a = max(0, water_level - 40)  # Small rabbits' grass (needs more water)
grass_b = max(0, water_level - 20)  # Medium rabbits' grass (moderate water needs)
grass_c = max(0, water_level)       # Large rabbits' grass (more drought-resistant)

small_rabbits = max(0, grass_a - 20)  # Small rabbit population reacts to Grass A
medium_rabbits = max(0, grass_b - 10)  # Medium rabbit population reacts to Grass B
large_rabbits = max(0, grass_c)       # Large rabbit population reacts to Grass C

# Helper function for severity color
def get_severity_color(value):
    if value < 30:
        return "#ff4d4d"  # Red
    elif value > 80:
        return "#3ae374"  # Green
    else:
        return "#ffa500"  # Orange

# Display factors with dynamic bars
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
    st.markdown("---")

# Layout for factors
col1, col2 = st.columns(2)

# Left Column: Rabbit Populations
with col1:
    st.header("Rabbit Populations 🐇")
    display_factor(
        "Large Rabbits", large_rabbits, "#FC72A5", "🐇",
        "Too many large rabbits!" if large_rabbits > 80 else
        "Balanced population of large rabbits." if large_rabbits > 30 else
        "Low population of large rabbits!"
    )
    display_factor(
        "Medium Rabbits", medium_rabbits, "#F99DBC", "🐇",
        "Too many medium rabbits!" if medium_rabbits > 80 else
        "Balanced population of medium rabbits." if medium_rabbits > 30 else
        "Low population of medium rabbits!"
    )
    display_factor(
        "Small Rabbits", small_rabbits, "#FEC206", "🐇",
        "Too many small rabbits!" if small_rabbits > 80 else
        "Balanced population of small rabbits." if small_rabbits > 30 else
        "Low population of small rabbits!"
    )

# Right Column: Grass Types
with col2:
    st.header("Grass Availability 🌱")
    display_factor(
        "Grass C", grass_c, "#3a5a40", "🌱",
        "Too little Grass C for large rabbits!" if grass_c < 30 else
        "Adequate Grass C for large rabbits." if grass_c <= 80 else
        "Plentiful Grass C for large rabbits!"
    )
    display_factor(
        "Grass B", grass_b, "#588157", "🌿",
        "Too little Grass B for medium rabbits!" if grass_b < 30 else
        "Adequate Grass B for medium rabbits." if grass_b <= 80 else
        "Plentiful Grass B for medium rabbits!"
    )
    display_factor(
        "Grass A", grass_a, "#a3b18a", "🌾",
        "Too little Grass A for small rabbits!" if grass_a < 30 else
        "Adequate Grass A for small rabbits." if grass_a <= 80 else
        "Plentiful Grass A for small rabbits!"
    )

# Notes
st.info("Adjust water levels or add a dam to observe how the ecosystem adapts!")
