

import streamlit as st
import numpy as np

# ===================================
# PAGE CONFIGURATION
# ===================================

st.set_page_config(
    page_title="Tourism Analytics",
    page_icon="🌍",
    layout="centered"
)

# ===================================
# TITLE
# ===================================

st.title("🌍 Tourism Experience Analytics")

st.write("""
This application predicts:

✔ Tourist Visit Mode  
✔ Attraction Ratings  
✔ Attraction Recommendations
""")

# ===================================
# SIDEBAR
# ===================================

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Home",
        "Visit Mode Prediction",
        "Rating Prediction",
        "Recommendation System"
    ]
)

# ===================================
# HOME PAGE
# ===================================

if menu == "Home":

    st.header("🏖 Tourism Analytics Project")

    st.write("""
    This project uses Machine Learning
    and Recommendation Systems to analyze
    tourism experiences.
    """)

# ===================================
# VISIT MODE PREDICTION
# ===================================

elif menu == "Visit Mode Prediction":

    st.header("🧳 Visit Mode Prediction")

    age = st.slider(
        "Enter Age",
        18,
        70,
        25
    )

    visit_month = st.slider(
        "Visit Month",
        1,
        12,
        6
    )

    rating = st.slider(
        "Previous Rating",
        1,
        5,
        4
    )

    if st.button("Predict Visit Mode"):

        # Dummy prediction logic

        if rating >= 4:
            result = "Family"

        elif rating == 3:
            result = "Friends"

        else:
            result = "Business"

        st.success(f"Predicted Visit Mode: {result}")

# ===================================
# RATING PREDICTION
# ===================================

elif menu == "Rating Prediction":

    st.header("⭐ Attraction Rating Prediction")

    attractions = st.selectbox(
        "Select Attraction Type",
        [
            "Beach",
            "Museum",
            "Park",
            "Historical Place"
        ]
    )

    visit_month = st.slider(
        "Visit Month",
        1,
        12,
        5
    )

    if st.button("Predict Rating"):

        # Dummy prediction logic

        if attractions == "Beach":
            rating = 4.7

        elif attractions == "Museum":
            rating = 4.2

        elif attractions == "Park":
            rating = 4.5

        else:
            rating = 4.3

        st.success(
            f"Predicted Rating: {rating}"
        )

# ===================================
# RECOMMENDATION SYSTEM
# ===================================

elif menu == "Recommendation System":

    st.header("🎯 Tourist Attraction Recommendations")

    preference = st.selectbox(
        "Choose Preference",
        [
            "Beach",
            "Museum",
            "Park",
            "Historical Place"
        ]
    )

    if st.button("Get Recommendations"):

        recommendations = {

            "Beach": [
                "Goa Beach",
                "Maldives",
                "Bondi Beach"
            ],

            "Museum": [
                "Louvre Museum",
                "British Museum",
                "National Museum"
            ],

            "Park": [
                "Central Park",
                "Yellowstone Park",
                "National Park"
            ],

            "Historical Place": [
                "Taj Mahal",
                "Colosseum",
                "Great Wall of China"
            ]
        }

        st.subheader("Recommended Attractions")

        for place in recommendations[preference]:

            st.write(f"✔ {place}")

# ===================================
# FOOTER
# ===================================

st.markdown("---")

st.caption("Tourism Experience Analytics System")
