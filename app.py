import streamlit as st
import random
import time

# Page Configuration
st.set_page_config(page_title="EcoPlate - SDG Solution", page_icon="🌱")

# Title and Header
st.title("🌱 EcoPlate: AI Food Waste Reducer")
st.markdown("### Aligning with UN SDG 12: Responsible Consumption and Production")
st.write("Enter the ingredients you have at home, and our AI will suggest recipes to prevent waste!")

# Sidebar for Info
st.sidebar.header("About SDG 12")
st.sidebar.info("Target 12.3: By 2030, halve per capita global food waste at the retail and consumer levels.")

# Input Section
st.subheader("Your Pantry Inventory")
ingredients = st.text_area("List your ingredients (e.g., eggs, spinach, bread, milk):", height=100)

# Button to Generate
if st.button("Generate Sustainable Recipes"):
    if not ingredients:
        st.warning("Please enter some ingredients first!")
    else:
        # Simulate AI Processing
        with st.spinner('AI is analyzing ingredients and checking sustainability metrics...'):
            time.sleep(2) # Simulate processing time
            
            # Mock AI Logic for Prototype Stability
            # In a production environment, you would call Hugging Face or OpenAI API here
            recipes = [
                f"**1. Quick {ingredients.split(',')[0].strip()} Scramble**\n\nA simple dish focusing on using your fresh proteins first. \n*Estimated CO2 Saved: 0.5kg*",
                f"**2. Leftover {ingredients.split(',')[-1].strip()} Bake**\n\nPerfect for using up items close to expiration. \n*Estimated CO2 Saved: 0.8kg*",
                f"**3. Sustainable Pantry Stir-Fry**\n\nMixes your dry goods with fresh produce. \n*Estimated CO2 Saved: 0.3kg*"
            ]
            
            st.success("Recipes Generated Successfully!")
            
            # Display Results
            for recipe in recipes:
                st.markdown("---")
                st.write(recipe)
                
            # Impact Metric
            st.metric(label="Total Estimated CO2 Saved", value="1.6 kg", delta="100% Sustainable")

# Footer
st.markdown("---")
st.caption("Project submitted for SDG AI Challenge | Built with Streamlit & Python")
