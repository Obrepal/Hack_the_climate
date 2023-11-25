import streamlit as st
import pandas as pd
import plotly.express as px




def value_of_tree(species, condition, size):
    return 5*3*size

def main():

    # Set page config to wide layout
    st.set_page_config(layout="wide")
    # Set the background image
    # bg_img = '''
    # <style>
    # [data-testid="stAppViewContainer"] {
    # background-image: url('https://images.unsplash.com/photo-1520262494112-9fe481d36ec3?q=80&w=3087&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
    # background-size: cover;
    # background-repeat: no-repeat;
    # # opacity: 0.1; /* Adjust the opacity value (0.0 to 1.0) */
    # }
    # </style>
    # '''
    # st.markdown(bg_img, unsafe_allow_html=True)
    tree_data = {'species': ["Dąb", "Klon", "Sosna", "Brzoza"],  "condition" : ["good", "bad", "dying", "amazing"]}

    trees_df = pd.DataFrame(data=tree_data)
    
  
    st.markdown("<h1 style='text-align: center; color: Black;background-color:#4B5320'>Arboris Capitalis</h1>", unsafe_allow_html=True)
    # st.markdown("<h3 style='text-align: center; color: Black;'>Drop in The required Inputs and we will do  the rest.</h3>", unsafe_allow_html=True)

    # st.markdown("<h4 style='text-align: center; color: Black;'>Submission for The Python Week</h4>",
    #             unsafe_allow_html=True)
    st.text("Welcome to Arboris Capitalis - your source of knowledge about the value of trees! Discover ecological and economic benefits by understanding the impact of trees on our \nenvironment. Learn how trees shape our worldand why their conservation is crucial for the future of our planet.")
    st.header("Tell us about your tree: ")


    selected_species = st.multiselect("Tree Species", trees_df['species'].unique().tolist())
    selected_condition = st.radio("Tree condition", trees_df['condition'].unique().tolist())
    selected_size = st.slider("Trunk size in cm", 50, 500)

    value_t = value_of_tree(selected_species,selected_condition,selected_size)

    st.markdown(f"""
    #### <span style="color:blue"></span> Value of your tree {value_t} """,unsafe_allow_html=True)  
    
    # fig = px.bar(filtered_df, x="HighestInterest", y="MaxPLN", color="Bank",color_discrete_map=c, title = 'Indiviudal clients')

if __name__ == '__main__':
        main()
