# TELCO CUSTOMER CHURN PREDICTOR

## Description
A machine learning web app that predicts whether a telecom customer is likely to churn. 
The app takes a customer dataset in CSV format, preprocesses it automatically, and returns 
churn predictions with probability scores and SHAP explainability charts — helping telecom 
companies identify at-risk customers before they leave.

## Tech Stack
* Tools: Python, Streamlit, JupyterLab, Git
* Libraries: numpy, pandas, matplotlib, seaborn, xgboost, scikit-learn, shap, joblib, imbalanced-learn

## Project Structure
```
project1-churn-predictor/
├── app/              Streamlit app
├── models/           saved model file
├── notebooks/        main Jupyter notebook
├── src/              preprocessing module
├── .gitignore        files excluded from git
├── README.md         project documentation
└── requirements.txt  project dependencies
```

## Model Performance
| Metric | Score |
|---|---|
| Accuracy | 0.79 |
| Weighted F1 | 0.79 |
| Weighted Precision | 0.79 |
| Weighted Recall | 0.79 |
| ROC AUC | 0.84 |

## How to Run

1. Clone the repository
```
git clone https://github.com/Razashah01/ai-bootcamp.git
```

2. Create and activate the environment
```
conda create -n aibootcamp python=3.11
conda activate aibootcamp
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Run the notebook
Open `notebooks/01_eda_and_pipeline.ipynb` in JupyterLab and run all cells

5. Launch the Streamlit app
```
streamlit run app/app.py
```

6. Upload the Telco CSV dataset and view predictions

## Limitations
- The uploaded CSV must have the same columns as the Telco Customer Churn dataset used for training
- The model is trained specifically on Telco customer data — predictions on data from a different domain or company may be unreliable
- Missing or renamed columns will cause the app to fail or return incorrect predictions
- For production use, retraining on domain-specific data is recommended