import streamlit as st

def show():
    st.title("About!")

    st.markdown("""
# 📘 About This Project

This project is developed as part of Caption Project  to predict and understand **extreme weather events** in **Nepal**.

## 🎯 Objective
To build a machine learning-based pipeline that:
- Predicts daily climate variables for each district in Nepal
- Classifies upcoming days into **normal or extreme weather events**
- Identifies **event types** like flood, drought, heatwave, and coldwave

## 🔧 Technologies Used
- **Streamlit** for the interactive web app
- **scikit-learn** for regression and classification models
- **Pandas & NumPy** for data processing
- **Matplotlib & Seaborn** for visualizations
- **Cimate data** from https://www.kaggle.com/datasets/saimondahal/nepal-daily-climate-1981-2019?resource=download
- **Shape file**


## 👥 Contributor(s)
- Suresh Subedi
- Omdena's & NIC Capacity Building Batchll - Nepal instructors

## 📌 Disclaimer
This tool is for **educational and research purposes only**. It is **not intended for official forecasting** or emergency response use.

---
For more details, contact the development team or refer to the GitHub repository (if available).
""")

#     st.markdown("""
# Welcome to the **Extreme Weather Event Detection and Prediction App** developed for Nepal.

# This application is a part of the Omdena-NIC-Nepal collaborative AI project that focuses on analyzing and predicting extreme weather conditions using historical climate data from 93 weather stations spanning 62 districts in Nepal and machine learning models.

# ### 🚀 Navigation
# Use the sidebar to explore the following sections:

# - 📊 **Data Exploration**  
# - 🧪 **Model Training and Evaluation**  
# - 🔮 **Extreme Weather Prediction**  
# - ℹ️ **About the Project**
# """)
