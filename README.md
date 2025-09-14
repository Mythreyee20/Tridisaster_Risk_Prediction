# 🌊🌪️🔥 Tridisaster Risk Prediction

**Tridisaster** is a smart AI-powered application to predict **Flood**, **Cyclone**, and **Heatwave** risks based on environmental and meteorological features.  

---

## 🚀 Features

- ✅ Predict Flood, Cyclone, or Heatwave Risk  
- ✅ Easy-to-use **web interface**  
- ✅ Built with **Python, Flask, and Random Forest**  
- ✅ Trained on real datasets for **accurate predictions**  
- ✅ Visualization-ready (**EDA plots: Distribution, Boxplot, Heatmap**)  

---

## 📂 Folder Structure

Tridisaster-Project/
│
├── app.py                  # Flask web application
├── Tridisaster.ipynb       # Notebook (EDA + Model Training + Saving)
├── README.md               # Project Documentation
│
├── datasets/               # Raw datasets
│   ├── flood.csv
│   ├── cyclone_dataset.csv
│   └── india_weather_data.csv
│
├── models/                 # Trained ML models & scalers
│   ├── flood_model.pkl
│   ├── flood_scaler.pkl
│   ├── cyclone_model.pkl
│   ├── cyclone_scaler.pkl
│   ├── heatwave_model.pkl
│   └── heatwave_scaler.pkl
│
├── templates/              # HTML templates for Flask
│   └── index.html
📥 Download Model Files

Due to GitHub’s 25 MB file size limit, trained model files are stored on Google Drive.

Flood Model & Scaler (.pkl file) https://drive.google.com/file/d/1YrdHZtAhBHc6xmjs1gEvZpg5-wb2BuJ7/view?usp=drive_link
Heatwave Model & Scaler (.pkl file) https://drive.google.com/file/d/1eIRuVPTMSKPLYDyLFHeYSTvz5TDzUWa-/view?usp=drive_link
India weather data (.csv file) https://drive.google.com/file/d/1dLejOwA1Hp8M65fNwBy5plcsKIpiMKQ6/view?usp=drive_link

👉 Download these .pkl files and place them inside the models/ folder before running the Flask app.

