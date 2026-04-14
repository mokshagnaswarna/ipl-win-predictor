IPL Win Predictor
A machine learning web app that predicts the probability of an IPL team winning a match based on live match conditions like score, overs, wickets, target, etc.

Built using Python, Scikit-learn, and Streamlit, and deployed on Streamlit Cloud.

Live Demo
https://ipl-win-predictor-gk4xcoyqyya6gd4adsmbep.streamlit.app/

Features:
Predicts win probability of chasing team
Real-time input of match situation
Simple and interactive UI using Streamlit
Trained ML pipeline for accurate predictions
Handles match stats like:
Current score
Overs completed
Wickets fallen
Target score
 Model Details:
Algorithm: (Logistic Regression / Random Forest / XGBoost)
Trained on historical IPL match data
Output: Win probability (0–100%)
Tech Stack
Python 3.11
Pandas & NumPy
Scikit-learn
Streamlit
Pickle (for model serialization)

Project Structure:
ipl-win-predictor/
│
├── app.py                # Streamlit app
├── train_model.py        # Model training script
├── model.pkl             # Trained ML model
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
└── data/                 # Dataset
Installation & Setup:
 1.Clone the repository:
       git clone https://github.com/your-username/ipl-win-predictor.git
       cd ipl-win-predictor
 2.Create a virtual environment:
       python -m venv venv
       source venv/bin/activate  # On Windows: venv\Scripts\activate

 3.Install dependencies:
       pip install -r requirements.txt
 4.Run the app:
       streamlit run app.py

Future Improvements:
Add live match API integration
Improve model accuracy with advanced algorithms (XGBoost/LightGBM)
Add team logos and better UI design
Add innings-wise prediction graphs

