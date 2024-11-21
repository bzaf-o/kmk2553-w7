import streamlit as st

# Title and Description
st.title("Natural Selection Dynamics 🌱🐇")
st.markdown("""
Explore how the presence of a dam and water availability affect the ecosystem.
""")
st.info("Adjust water levels or add a dam to observe how the ecosystem adapts!")

# Sidebar for Interaction
st.sidebar.header("Simulation Controls")

# Initial parameters
initial_water_level = 80
initial_dam_present = False
initial_years_passed = 0

# State management for water level, dam, and year counter
if "water_level" not in st.session_state:
    st.session_state.water_level = initial_water_level
if "dam_present" not in st.session_state:
    st.session_state.dam_present = initial_dam_present
if "years_passed" not in st.session_state:
    st.session_state.years_passed = initial_years_passed

# Dam toggle and water slider
st.session_state.dam_present = st.sidebar.checkbox("Dam on the River 🌊", value=st.session_state.dam_present)
if st.session_state.dam_present:
    st.session_state.water_level = 30  # Reduced dam impact by increasing the fixed water level
    st.sidebar.write("Water levels are reduced due to the dam.")
else:
    st.session_state.water_level = st.sidebar.slider("Amount of Water 💧", 0, 100, st.session_state.water_level)

# Reactive calculations based on water level
def calculate_population(water_level):
    grass_a = max(0, water_level - 15)
    grass_b = max(0, water_level - 30)
    grass_c = max(0, water_level)
    return {
        "grass_a": grass_a,
        "grass_b": grass_b,
        "grass_c": grass_c,
        "small_rabbits": max(0, grass_a - 5),
        "medium_rabbits": max(0, grass_b - 15),
        "large_rabbits": max(0, grass_c)
    }

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

# Horizontal layout for simulation buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Simulate 1 Year"):
        st.session_state.water_level = max(0, st.session_state.water_level - 10)
        st.session_state.years_passed += 1

with col2:
    if st.button("Simulate 5 Years"):
        st.session_state.water_level = max(0, st.session_state.water_level - 50)
        st.session_state.years_passed += 5

with col3:
    if st.button("Reset to Initial Values"):
        st.session_state.water_level = initial_water_level
        st.session_state.dam_present = initial_dam_present
        st.session_state.years_passed = initial_years_passed

# Display current year counter
st.markdown(f"### Years Passed: {st.session_state.years_passed}")

# Display current state
populations = calculate_population(st.session_state.water_level)

col1, col2 = st.columns(2)

# Left Column: Rabbit Populations
with col1:
    st.header("Rabbit Populations 🐇")
    display_factor(
        "Small Rabbits", populations["small_rabbits"], "#FEC206", "🐇",
        "Too many small rabbits!" if populations["small_rabbits"] > 80 else
        "Balanced population of small rabbits." if populations["small_rabbits"] > 30 else
        "Low population of small rabbits!"
    )
    display_factor(
        "Medium Rabbits", populations["medium_rabbits"], "#F99DBC", "🐇",
        "Too many medium rabbits!" if populations["medium_rabbits"] > 80 else
        "Balanced population of medium rabbits." if populations["medium_rabbits"] > 30 else
        "Low population of medium rabbits!"
    )
    display_factor(
        "Large Rabbits", populations["large_rabbits"], "#FC72A5", "🐇",
        "Too many large rabbits!" if populations["large_rabbits"] > 80 else
        "Balanced population of large rabbits." if populations["large_rabbits"] > 30 else
        "Low population of large rabbits!"
    )

# Right Column: Grass Types
with col2:
    st.header("Grass Availability 🌱")
    display_factor(
        "Grass A", populations["grass_a"], "#a3b18a", "🌾",
        "Too little Grass A for small rabbits!" if populations["grass_a"] < 30 else
        "Adequate Grass A for small rabbits." if populations["grass_a"] <= 80 else
        "Plentiful Grass A for small rabbits!"
    )
    display_factor(
        "Grass B", populations["grass_b"], "#588157", "🌿",
        "Too little Grass B for medium rabbits!" if populations["grass_b"] < 30 else
        "Adequate Grass B for medium rabbits." if populations["grass_b"] <= 80 else
        "Plentiful Grass B for medium rabbits!"
    )
    display_factor(
        "Grass C", populations["grass_c"], "#3a5a40", "🌱",
        "Too little Grass C for large rabbits!" if populations["grass_c"] < 30 else
        "Adequate Grass C for large rabbits." if populations["grass_c"] <= 80 else
        "Plentiful Grass C for large rabbits!"
    )
