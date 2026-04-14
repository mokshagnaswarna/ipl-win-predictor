import streamlit as st
import pandas as pd
import pickle

teams = ['Sunrisers Hyderabad',
         'Mumbai Indians',
         'Royal Challengers Bangalore',
         'Kolkata Knight Riders',
         'Kings XI Punjab',
         'Chennai Super Kings',
         'Rajasthan Royals',
         'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Kolkata', 'Delhi',
          'Chennai', 'Jaipur', 'Pune', 'Ahmedabad']

pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title('IPL Winner Predictor 🏏')

team1 = st.selectbox('Team 1', teams)
team2 = st.selectbox('Team 2', teams)
city = st.selectbox('City', cities)

if st.button('Predict Winner'):
    input_df = pd.DataFrame({
        'team1': [team1],
        'team2': [team2],
        'city': [city]
    })

    result = pipe.predict(input_df)

    st.success(f"🏆 Winner: {result[0]}")