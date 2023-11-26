import streamlit as st
import pandas as pd
import plotly.express as px
from tree_func import *

def main():

    tree_growth_rate_per_year = {'pine': 0.00313, 'oak': 0.00188}
    tree_density = {'pine': 616.5, 'oak': 745}

    CO2_in_1kg_of_carbon = 3.67  # [kg] stala
    average_oxygen_production_in_one_year = 66  # [kg] stala
    oxygen_per_person_one_day = 0.28  # [kg] stala
    average_car_co2_emission_in_one_year = 4600  # [kg] stala
    
    tree_data = {'species': ["oak", "pine"]}
    trees_df = pd.DataFrame(data=tree_data)
    

    # Set page config to wide layout
    st.set_page_config(layout="wide")
    bg_img = '''
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url('https://images.unsplash.com/photo-1609901525254-9e64b77b483a?q=80&w=3087&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
    background-size: cover;
    background-repeat: no-repeat;
    # opacity: 0.1; /* Adjust the opacity value (0.0 to 1.0) */
    }
    </style>
    '''
    st.markdown(bg_img, unsafe_allow_html=True)


  
# Title
    st.markdown("<h1 style='text-align: center; color: White;'>Arboris Capitalis</h1>", unsafe_allow_html=True)

    # Description
    st.markdown(
        """
        <p style='text-align: justify;'>Welcome to Arboris Capitalis - your source of knowledge about the value of trees! Discover ecological and economic benefits by understanding the impact of trees on our environment. Learn how trees shape our world and why their conservation is crucial for the future of our planet.</p>
        """,
        unsafe_allow_html=True
    )
    st.header("Tell us about your tree: ")


    selected_species = st.selectbox("Tree Species", trees_df['species'].unique().tolist())
    density = tree_density[selected_species]

    growth_rate_per_year = tree_growth_rate_per_year[selected_species]

    circumference = st.slider("Tree girth measurement in m", 0.1, 5.0)
    height = st.slider("Height in m", 5, 20)
    diameter = (circumference * 0.5)/3.14

    tree_mass_calculation = mass_calculation(density, height, diameter)
    years = years_of_tree_growth(diameter, growth_rate_per_year)
    dry_mass = dry_mass_calculation(tree_mass_calculation)

    # carbon absorption
    current_carbon_absorption = current_carbon_tree_absorption(dry_mass, CO2_in_1kg_of_carbon)
    carbon_tree_absorption_in_1_year= carbon_tree_absorption_in_one_year(current_carbon_absorption, years)
    carbon_tree_absorption_in_next_10 = carbon_tree_absorption_in_next_10_years(carbon_tree_absorption_in_1_year)
    compensation_years_of_car_emissions = years_car_emission(current_carbon_absorption)
    

    # oxygen production
    current_oxygen_production = current_oxygen_tree_production(years)
    oxygen_production_in_next_10 = oxygen_tree_production_in_next_10_years()
    production_days_for_one_person = oxygen_days_for_one_person(current_oxygen_production)
    production_years_for_one_person_in_next_10_years = oxygen_years_for_one_person(oxygen_production_in_next_10)

    number_of_iphones_14 = int(how_many_smartphones(current_carbon_absorption))
    number_of_iphones_14_in_next_10_years = int(how_many_smartphones(carbon_tree_absorption_in_next_10))

   # Current carbon absorption and equivalent iPhones
    st.markdown(f"""
        #### How many kilograms of carbon has been absorbed by your tree so far?
        - Kilograms of carbon absorbed: {current_carbon_absorption}
        - Equivalent iPhones 14: {number_of_iphones_14}
    """)

    # Carbon absorption in the next 10 years
    st.markdown(f"""
        #### How many kilograms of carbon will absorbed by your tree in next 10 years?
        - Estimated kilograms in the next decade: {carbon_tree_absorption_in_next_10}
    """)

    # Current oxygen production and equivalent person-days
    st.markdown(f"""
        #### How many kilograms of oxygen has been produced by your tree so far?
        - Kilograms of oxygen produced: {current_oxygen_production}
        - Equivalent person-days of oxygen: {production_days_for_one_person}
    """)

    # Oxygen production in the next 10 years and equivalent person-years
    st.markdown(f"""
        #### How many kg of oxygen will be produced by your tree in next 10 years?
        - Estimated kilograms in the next decade: {oxygen_production_in_next_10}
        - Equivalent person-years of oxygen: {production_years_for_one_person_in_next_10_years}
    """)
    
    # fig = px.bar(filtered_df, x="HighestInterest", y="MaxPLN", color="Bank",color_discrete_map=c, title = 'Indiviudal clients')

if __name__ == '__main__':
    main()
