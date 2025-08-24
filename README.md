# README – Intrusion Detection System using Ensemble Machine Learning

# Project Overview

This project implements a Network Intrusion Detection System (IDS) using ensemble machine learning models. The goal is to automatically detect and classify malicious network traffic into different types of cyberattacks, thereby enhancing system security.

The system is trained and tested on the "NSL-KDD dataset", which is a standard benchmark dataset for intrusion detection research. It combines multiple machine learning algorithms into an "ensemble voting classifier" to improve accuracy and robustness.


# Features

* Classifies traffic into: Normal, DoS (Denial of Service), Probe, R2L (Remote to Local), U2R (User to Root).
* Uses feature engineering & selection for optimal performance.
* Employs ensemble learning (Voting Classifier) combining multiple algorithms.
* Provides detailed performance metrics: Accuracy, Precision, Recall, F1-score, ROC curves.
* Includes a Streamlit web interface for interactive testing and predictions.

---

# Algorithms Used

* Random Forest
* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)
* Naive Bayes
* Logistic Regression
* Ensemble Voting Classifier (Soft Voting)

---

# Tools & Technologies

* Python 3
* Jupyter Notebook (Model training & analysis)
* Streamlit (Web-based interface for predictions)
* scikit-learn, pandas, NumPy, matplotlib
* NSL-KDD dataset for training and testing

---

# Project Workflow

1. Data Preprocessing – Cleaned and encoded categorical features, applied scaling and normalization.
2. Feature Selection – Used multiple techniques (ANOVA, RFE, Chi-square, LASSO, Mutual Information).
3. Model Training – Trained ML models individually and as an ensemble.
4. Evaluation – Measured accuracy, precision, recall, F1-score, and ROC curves.
5. Deployment – Integrated the final ensemble model (`finalpro.p`) with Streamlit app for live predictions.

---

# How to Run the Project

1. Clone this repository.

   git clone https://github.com/username/IDS-Ensemble-ML.git
   cd IDS-Ensemble-ML

2. Install dependencies.

   pip install -r requirements.txt

3. Train the model (optional, already trained model `finalpro.p` provided).

   jupyter notebook DBids.ipynb

4. Run the Streamlit app.

   streamlit run app.py

5. Open the web browser at [http://localhost:8501/](http://localhost:8501/) and test the IDS.

---

# Results

* Achieved high accuracy and improved detection rate using ensemble learning.
* ROC curves demonstrated reliable separation between attack classes.
* Ensemble classifier outperformed individual models in robustness.

---

# Future Improvements

* Extend to real-time traffic analysis using packet capture tools (e.g., Zeek/Suricata).
* Enhance feature extraction to support modern network environments.
* Deploy as a containerized microservice for scalability.

---

# Authors

* DhanushBharathi – Final Year B.E Project (Computer Science & Engineering)

---
