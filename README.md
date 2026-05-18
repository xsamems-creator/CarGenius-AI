CarGenius-AI/
│
├── backend/
│   ├── app.py
│   ├── recommender.py
│   ├── nlp_processor.py
│   ├── emi_calculator.py
│   ├── fuel_cost.py
│   ├── ownership_cost.py
│   ├── cars_dataset.csv
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── components/
│   │   │   ├── ChatBox.js
│   │   │   ├── RecommendationCard.js
│   │   │   ├── CompareCars.js
│   │   │   ├── EMI.js
│   │   │   └── FuelAnalysis.js
│   │   ├── styles.css
│   │
│   ├── package.json
│
├── README.md
└── .gitignore
# 🚗 CarGenius AI

AI-powered car recommendation platform using NLP and Machine Learning.

## Features

- Smart Car Recommendations
- NLP-based Query Understanding
- EMI Calculator
- Fuel Cost Analysis
- Ownership Cost Prediction
- Car Comparison

## Tech Stack

Frontend:
- React.js

Backend:
- Flask
- Python

AI/ML:
- Scikit-learn
- NLP

## Run Project

Backend:

pip install -r requirements.txt
python app.py

Frontend:

npm install
npm start
