# EduMind AI: End-to-End Student Performance Predictor

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Ganateja19/EduMind-AI)

> **Note:** Please refer to [Deployment Guide](deployment_guide.md) for detailed instructions on how to deploy this application to Render, Docker, or Azure. The model artifacts are now included in the repository for easier deployment.

![Dashboard Design](app_screenshot.png)

### 🚀 Run Locally
1. Clone the repo:
   ```bash
   git clone https://github.com/Ganateja19/EduMind-AI-End-to-End-Student-Performance-Predictor
   cd EduMind-AI
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open [http://localhost:5000](http://localhost:5000) in your browser.

## Overview
This **End-to-End Machine Learning** application predicts student performance based on critical socio-economic and educational factors.

## Features
- **Accurate Predictions**: Uses trained ML models to forecast scores.
- **Modern UI**: Clean, glassmorphism-inspired interface.
- **Instant Results**: Real-time prediction display.

## Tech Stack
- **Frontend**: HTML5, CSS3 (Glassmorphism), JavaScript
- **Backend**: Python, Flask
- **ML**: Scikit-Learn, CatBoost, XGBoost, Pandas
- **Deployment**: Docker, Ready for Cloud (AWS/Azure/Render)

## Model Performance
We trained multiple models to ensure high accuracy. The best performing model was **CatBoost Regressor** with an R2 Score of **98%**.

| Model | R2 Score |
|-------|----------|
| CatBoost Regressor | 98.2% |
| XGBoost Regressor | 97.8% |
| Random Forest | 96.5% |

## Dataset Details
The model is trained on a dataset containing:
- **Gender**: Male/Female
- **Race/Ethnicity**: Groups A-E
- **Parental Education**: High school to Master's degree
- **Lunch**: Standard/Free
- **Test Prep**: None/Completed


## Deployment
This project is containerized with Docker and includes deployment configurations for:
- Docker (`Dockerfile`)
- AWS Elastic Beanstalk (`.ebextensions`)
- Azure Web Apps (GitHub Actions)
