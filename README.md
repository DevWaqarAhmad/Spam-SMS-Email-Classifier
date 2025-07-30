
# 📧 Spam SMS/Email Classifier (with Streamlit App)

A powerful and accurate Machine Learning-based solution that detects whether a given SMS or email is spam or not. This project uses Logistic Regression and TF-IDF vectorization, built using Python, Scikit-learn, Pandas, and Streamlit.

[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()

---

## 📂 Repository Structure

```
Spam-SMS-Email-Classifier/
│
├── data/
│   └── spam.csv                  # Raw dataset (SMS labeled as ham/spam)
│
├── pkl/
│   ├── model.pkl                 # Trained ML model (Logistic Regression)
│   └── vectorizer.pkl            # TF-IDF vectorizer
│
├── app.py                        # Streamlit app for message prediction
├── spam_classifier_notebook.ipynb  # Jupyter notebook with full model pipeline
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies
└── .gitignore
```

---

## 📊 Features

- Detects whether input message is Spam or Not
- Uses Logistic Regression (option to change model)
- Data preprocessing & text cleaning
- Spam class balancing using upsampling
- TF-IDF feature extraction (top 5000 features)
- User-friendly Streamlit Web App
- Ready for deployment (Render/HuggingFace)

---

## 📁 Dataset

- Dataset: [`spam.csv`](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- Classes:
  - `ham`: Legitimate messages
  - `spam`: Fraud, loan, prize messages

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/DevWaqarAhmad/Spam-SMS-Email-Classifier.git
cd Spam-SMS-Email-Classifier
```

### 2. Create a virtual environment

```bash
python -m venv env
```

### 3. Activate the environment

- On Windows:
```bash
env\Scripts\activate
```

- On Mac/Linux:
```bash
source env/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Streamlit app

```bash
streamlit run app.py
```

---

## 🧠 Model Details

- **Vectorizer**: `TfidfVectorizer` with `max_features=5000`
- **Classifier**: `LogisticRegression (max_iter=1000)`
- **Balanced Dataset**: Using `sklearn.utils.resample` to upsample spam class
- **Accuracy Achieved**: ~97-98%

---

## 🧪 Sample Predictions

| Message                                                                 | Prediction |
|-------------------------------------------------------------------------|------------|
| "Claim your free $5000 loan now. No documents required!"               | Spam       |
| "Hey, meeting is at 3 PM today. Don't be late."                         | Not Spam   |

---

## 🌍 Live Deployment (Coming Soon)

> Deployed app link will be added here once hosted on Render/HuggingFace

---

## 👨‍💻 Author

**Waqar Ahmad**  
📧 Email: [devwaqarahmad@gmail.com](mailto:devwaqarahmad@gmail.com)  
🌐 GitHub: [DevWaqarAhmad](https://github.com/DevWaqarAhmad)

---

## 📃 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---
