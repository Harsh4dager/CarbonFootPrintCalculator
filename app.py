import streamlit as st

Emission_Factors_per_country = {
    "india": {
        "Transportation" : 0.14, # kgCo2/km
        "Electricity" : 0.82, # kgCo2/kwh
        "Diet" : 1.25, # kgCo2/meal
        "Waste" : 0.1 # kgCo2/kg
    },
    "china": {
        "Transportation" : 0.16, # kgCo2/km
        "Electricity" : 0.62, # kgCo2/kwh
        "Diet" : 1.30, # kgCo2/meal
        "Waste" : 0.11 # kgCo2/kg
    },
    "usa": {
        "Transportation" : 0.17, # kgCo2/km
        "Electricity" : 0.49, # kgCo2/kwh
        "Diet" : 1.45, # kgCo2/meal
        "Waste" : 0.15 # kgCo2/kg
    },
    "indonesia": {
        "Transportation" : 0.15, # kgCo2/km
        "Electricity" : 0.55, # kgCo2/kwh
        "Diet" : 1.20, # kgCo2/meal
        "Waste" : 0.13 # kgCo2/kg
    },
    "pakistan": {
        "Transportation" : 0.18, # kgCo2/km
        "Electricity" : 0.45, # kgCo2/kwh
        "Diet" : 1.30, # kgCo2/meal
        "Waste" : 0.12 # kgCo2/kg
    },
    "nigeria": {
        "Transportation" : 0.16, # kgCo2/km
        "Electricity" : 0.60, # kgCo2/kwh
        "Diet" : 1.25, # kgCo2/meal
        "Waste" : 0.14 # kgCo2/kg
    },
    "brazil": {
        "Transportation" : 0.20, # kgCo2/km
        "Electricity" : 0.50, # kgCo2/kwh
        "Diet" : 1.40, # kgCo2/meal
        "Waste" : 0.11 # kgCo2/kg
    },
    "bangladesh": {
        "Transportation" : 0.17, # kgCo2/km
        "Electricity" : 0.60, # kgCo2/kwh
        "Diet" : 1.25, # kgCo2/meal
        "Waste" : 0.13 # kgCo2/kg
    },
    "russia": {
        "Transportation" : 0.18, # kgCo2/km
        "Electricity" : 0.55, # kgCo2/kwh
        "Diet" : 1.35, # kgCo2/meal
        "Waste" : 0.12 # kgCo2/kg
    },
    "ethiopia": {
        "Transportation" : 0.16, # kgCo2/km
        "Electricity" : 0.65, # kgCo2/kwh
        "Diet" : 1.30, # kgCo2/meal
        "Waste" : 0.14 # kgCo2/kg
    },
     "mexico": {
        "Transportation" : 0.19, # kgCo2/km
        "Electricity" : 0.48, # kgCo2/kwh
        "Diet" : 1.35, # kgCo2/meal
        "Waste" : 0.12 # kgCo2/kg
    },
    "japan": {
        "Transportation" : 0.18, # kgCo2/km
        "Electricity" : 0.41, # kgCo2/kwh
        "Diet" : 1.30, # kgCo2/meal
        "Waste" : 0.13 # kgCo2/kg
    },
    "philippines": {
        "Transportation" : 0.17, # kgCo2/km
        "Electricity" : 0.55, # kgCo2/kwh
        "Diet" : 1.25, # kgCo2/meal
        "Waste" : 0.14 # kgCo2/kg
    },
    "egypt": {
        "Transportation" : 0.16, # kgCo2/km
        "Electricity" : 0.60, # kgCo2/kwh
        "Diet" : 1.30, # kgCo2/meal
        "Waste" : 0.11 # kgCo2/kg
    },
    "dr_congo": {
        "Transportation" : 0.15, # kgCo2/km
        "Electricity" : 0.65, # kgCo2/kwh
        "Diet" : 1.28, # kgCo2/meal
        "Waste" : 0.15 # kgCo2/kg
    },
    "vietnam": {
        "Transportation" : 0.17, # kgCo2/km
        "Electricity" : 0.50, # kgCo2/kwh
        "Diet" : 1.32, # kgCo2/meal
        "Waste" : 0.13 # kgCo2/kg
    },
    "iran": {
        "Transportation" : 0.18, # kgCo2/km
        "Electricity" : 0.58, # kgCo2/kwh
        "Diet" : 1.33, # kgCo2/meal
        "Waste" : 0.12 # kgCo2/kg
    },
    "turkey": {
        "Transportation" : 0.20, # kgCo2/km
        "Electricity" : 0.52, # kgCo2/kwh
        "Diet" : 1.38, # kgCo2/meal
        "Waste" : 0.11 # kgCo2/kg
    },
       "germany": {
        "Transportation" : 0.17, # kgCo2/km
        "Electricity" : 0.41, # kgCo2/kwh
        "Diet" : 1.30, # kgCo2/meal
        "Waste" : 0.12 # kgCo2/kg
    },
    "thailand": {
        "Transportation" : 0.18, # kgCo2/km
        "Electricity" : 0.50, # kgCo2/kwh
        "Diet" : 1.35, # kgCo2/meal
        "Waste" : 0.13 # kgCo2/kg
    },
    "tanzania": {
        "Transportation" : 0.16, # kgCo2/km
        "Electricity" : 0.55, # kgCo2/kwh
        "Diet" : 1.25, # kgCo2/meal
        "Waste" : 0.14 # kgCo2/kg
    },
    "united_kingdom": {
        "Transportation" : 0.19, # kgCo2/km
        "Electricity" : 0.35, # kgCo2/kwh
        "Diet" : 1.30, # kgCo2/meal
        "Waste" : 0.11 # kgCo2/kg
    },
    "france": {
        "Transportation" : 0.17, # kgCo2/km
        "Electricity" : 0.30, # kgCo2/kwh
        "Diet" : 1.28, # kgCo2/meal
        "Waste" : 0.12 # kgCo2/kg
    },
    "south_africa": {
        "Transportation" : 0.18, # kgCo2/km
        "Electricity" : 0.60, # kgCo2/kwh
        "Diet" : 1.32, # kgCo2/meal
        "Waste" : 0.13 # kgCo2/kg
    },
    "italy": {
        "Transportation" : 0.19, # kgCo2/km
        "Electricity" : 0.40, # kgCo2/kwh
        "Diet" : 1.33, # kgCo2/meal
        "Waste" : 0.11 # kgCo2/kg
    },
    "kenya": {
        "Transportation" : 0.16, # kgCo2/km
        "Electricity" : 0.50, # kgCo2/kwh
        "Diet" : 1.25, # kgCo2/meal
        "Waste" : 0.14 # kgCo2/kg
    },
    "myanmar": {
        "Transportation" : 0.17, # kgCo2/km
        "Electricity" : 0.55, # kgCo2/kwh
        "Diet" : 1.30, # kgCo2/meal
        "Waste" : 0.12 # kgCo2/kg
    },
    "colombia": {
        "Transportation" : 0.18, # kgCo2/km
        "Electricity" : 0.45, # kgCo2/kwh
        "Diet" : 1.35, # kgCo2/meal
        "Waste" : 0.13 # kgCo2/kg
    },
    "south_korea": {
        "Transportation" : 0.19, # kgCo2/km
        "Electricity" : 0.52, # kgCo2/kwh
        "Diet" : 1.30, # kgCo2/meal
        "Waste" : 0.11 # kgCo2/kg
    },
    "uganda": {
        "Transportation" : 0.16, # kgCo2/km
        "Electricity" : 0.55, # kgCo2/kwh
        "Diet" : 1.25, # kgCo2/meal
        "Waste" : 0.14 # kgCo2/kg
    },
    "sudan": {
        "Transportation" : 0.17, # kgCo2/km
        "Electricity" : 0.60, # kgCo2/kwh
        "Diet" : 1.30, # kgCo2/meal
        "Waste" : 0.13 # kgCo2/kg
    },
    "spain": {
        "Transportation" : 0.18, # kgCo2/km
        "Electricity" : 0.45, # kgCo2/kwh
        "Diet" : 1.35, # kgCo2/meal
        "Waste" : 0.12 # kgCo2/kg
    },
    "argentina": {
        "Transportation" : 0.19, # kgCo2/km
        "Electricity" : 0.50, # kgCo2/kwh
        "Diet" : 1.40, # kgCo2/meal
        "Waste" : 0.11 # kgCo2/kg
    },
    "algeria": {
        "Transportation" : 0.17, # kgCo2/km
        "Electricity" : 0.52, # kgCo2/kwh
        "Diet" : 1.30, # kgCo2/meal
        "Waste" : 0.13 # kgCo2/kg
    },
    "iraq": {
        "Transportation" : 0.18, # kgCo2/km
        "Electricity" : 0.48, # kgCo2/kwh
        "Diet" : 1.35, # kgCo2/meal
        "Waste" : 0.12 # kgCo2/kg
    },
    "afghanistan": {
        "Transportation" : 0.16, # kgCo2/km
        "Electricity" : 0.55, # kgCo2/kwh
        "Diet" : 1.25, # kgCo2/meal
        "Waste" : 0.14 # kgCo2/kg
    },
    "poland": {
        "Transportation" : 0.19, # kgCo2/km
        "Electricity" : 0.42, # kgCo2/kwh
        "Diet" : 1.30, # kgCo2/meal
        "Waste" : 0.11 # kgCo2/kg
    },
    "canada": {
        "Transportation" : 0.20, # kgCo2/km
        "Electricity" : 0.48, # kgCo2/kwh
        "Diet" : 1.35, # kgCo2/meal
        "Waste" : 0.12 # kgCo2/kg
    },
    "morocco": {
        "Transportation" : 0.18, # kgCo2/km
        "Electricity" : 0.50, # kgCo2/kwh
        "Diet" : 1.30, # kgCo2/meal
        "Waste" : 0.13 # kgCo2/kg
    },
    "saudi_arabia": {
        "Transportation" : 0.17, # kgCo2/km
        "Electricity" : 0.52, # kgCo2/kwh
        "Diet" : 1.25, # kgCo2/meal
        "Waste" : 0.14 # kgCo2/kg
    },
    "ukraine": {
        "Transportation" : 0.16, # kgCo2/km
        "Electricity" : 0.55, # kgCo2/kwh
        "Diet" : 1.30, # kgCo2/meal
        "Waste" : 0.13 # kgCo2/kg
    },
    "angola": {
        "Transportation" : 0.18, # kgCo2/km
        "Electricity" : 0.50, # kgCo2/kwh
        "Diet" : 1.35, # kgCo2/meal
        "Waste" : 0.12 # kgCo2/kg
    },
    "uzbekistan": {
        "Transportation" : 0.19, # kgCo2/km
        "Electricity" : 0.48, # kgCo2/kwh
        "Diet" : 1.30, # kgCo2/meal
        "Waste" : 0.11 # kgCo2/kg
    },
    "yemen": {
        "Transportation" : 0.17, # kgCo2/km
        "Electricity" : 0.52, # kgCo2/kwh
        "Diet" : 1.25, # kgCo2/meal
        "Waste" : 0.14 # kgCo2/kg
    },
    "peru": {
        "Transportation" : 0.18, # kgCo2/km
        "Electricity" : 0.50, # kgCo2/kwh
        "Diet" : 1.35, # kgCo2/meal
        "Waste" : 0.12 # kgCo2/kg
    },
    "malaysia": {
        "Transportation" : 0.19, # kgCo2/km
        "Electricity" : 0.48, # kgCo2/kwh
        "Diet" : 1.30, # kgCo2/meal
        "Waste" : 0.11 # kgCo2/kg
    },
    "ghana": {
        "Transportation" : 0.17, # kgCo2/km
        "Electricity" : 0.52, # kgCo2/kwh
        "Diet" : 1.25, # kgCo2/meal
        "Waste" : 0.14 # kgCo2/kg
    },
    "mozambique": {
        "Transportation" : 0.13, # kgCo2/km
        "Electricity" : 0.55, # kgCo2/kwh
        "Diet" : 1.30, # kgCo2/meal
        "Waste" : 0.14 # kgCo2/kg
    },
    "nepal": {
        "Transportation" : 0.17, # kgCo2/km
        "Electricity" : 0.60, # kgCo2/kwh
        "Diet" : 1.25, # kgCo2/meal
        "Waste" : 0.13 # kgCo2/kg
    }
}

st.set_page_config(layout="wide", page_title="your carbon calculator")

st.title('Your Carbon Footprint Calculator')

# user inputs
st.subheader(" 🌎 Your country")
country = st.selectbox("Select", [
    "india", "china", "usa", "indonesia", "pakistan", "nigeria", "brazil", "bangladesh", "russia", "ethiopia", "mexico",
    "japan", "philippines", "egypt", "dr_congo", "vietnam", "iran", "turkey", "germany", "thailand",
    "tanzania", "uk", "france", "south africa", "italy", "kenya", "myanmar", "colombia", "south korea",
    "uganda", "sudan", "spain", "argentina", "algeria", "iraq", "afghanistan", "poland", "canada", "morocco",
    "saudi arabia", "ukraine", "angola", "uzbekistan", "yemen", "peru", "malaysia", "ghana", "mozambique", "nepal"
])

column1, column2 = st.columns(2)

with column1:
    st.subheader(' 🚗 Daily compute distance(in km)')
    distance = st.slider("Distance", 0.0, 100.0, key="distance_input")

    st.subheader(' 💡 Monthly electricity consumption(in kwh)')
    electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")

with column2:
    st.subheader(' 🗑️ Waste generated per week(in kg)')
    waste = st.slider("Waste", 0.0, 100.0, key="waste_input")

    st.subheader(' 🍲 Number of meals per day')
    meals = st.number_input("Meals", 0, key="meals_input")


if(distance > 0):
    distance = distance * 365

if(electricity > 0):
    electricity = electricity * 12

if(waste > 0):
    waste = waste * 52

if(meals > 0):
    meals = meals * 365

# calculating the carbon footprint
transportation_emission = Emission_Factors_per_country[country]["Transportation"] * distance
Electricity_emission = Emission_Factors_per_country[country]["Electricity"] * electricity
Waste_emission = Emission_Factors_per_country[country]["Waste"] * waste
Diet_emission = Emission_Factors_per_country[country]["Diet"] * meals

# getting tonnes CO2
transportation_emission = round(transportation_emission/1000, 2)
Electricity_emission = round(Electricity_emission/1000, 2)
Waste_emission = round(Waste_emission/1000, 2)
Diet_emission = round(Diet_emission/1000, 2)

total_emission = round(
    transportation_emission + Electricity_emission + Waste_emission + Diet_emission, 2
)


# displaying 

if st.button("Calculate CO2 Emissions"):

    # Display results
    st.header("Results")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emissions by Category")
        st.info(f"🚗 Transportation: {transportation_emission} tonnes CO2 per year")
        st.info(f"💡 Electricity: {Electricity_emission} tonnes CO2 per year")
        st.info(f"🗑️ Waste: {Waste_emission} tonnes CO2 per year")
        st.info(f"🍽️ Diet: {Diet_emission} tonnes CO2 per year")


    with col4:
        st.subheader("Total Carbon Footprint")
        st.success(f"🌍 Your total carbon footprint is: {total_emission} tonnes CO2 per year")
