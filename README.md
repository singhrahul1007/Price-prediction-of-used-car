# 🚗 Used Car Price Predictor

![Banner](static/Images/web_page.png)

Provide necessary input using provided dropdown-option and also enter Kilometers Driven amount
![providing_input](static/Images/input.png)

After Providing all the info `Press` **Predict price** Button
![predict_price](static/Images/prediction.png)

Welcome to **Used Car Price Predictor**, an end-to-end Machine Learning project that predicts the resale value of used cars. This is my very first ML project, where I put into practice what I've recently learned about:

* 🔹 Linear Regression
* 🔹 SimpleImputer
* 🔹 ColumnTransformer
* 🔹 Scikit-learn Pipelines

Despite the dataset being quite small (only 724 rows after cleaning), I achieved an approximate accuracy of **88%**, which was very exciting for a first project!

---

## 📌 Project Objectives

* ✅ Practice **data preprocessing**
* ✅ Apply **feature transformation** using `ColumnTransformer`
* ✅ Implement **missing value handling** using `SimpleImputer`
* ✅ Train a regression model using `LinearRegression`
* ✅ Deploy a simple web app using **Flask**
* ✅ Learn full ML pipeline from dataset to deployment

---

## 📁 Repository Structure

```
Used-Cars-Price-Prediction/
│
├── static/
│   └── css/
│       └── style.css         # Custom CSS styles
│
├── templates/
│   └── index.html            # Frontend HTML page
│
├── Images/
│   └── background.png        # Background or banner image
│
├── app.py                    # Flask application
├── model.pkl                 # Trained regression model
├── car_data.csv              # Cleaned dataset
├── requirements.txt          # Python dependencies
├── .gitignore                # Files ignored by Git
├── README.md                 # Project overview and usage
└── venv/                     # Virtual environment (excluded from Git)
```

---

## 💠 How to Run This Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Used-Cars-Price-Prediction.git
cd Used-Cars-Price-Prediction
```

### 2️⃣ Create & Activate Virtual Environment

**Windows (PowerShell):**

```bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

Open your browser and visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---


![Web App Prediction Screenshot](static/Images/background.png)

---

## 🔍 Dataset Information

The dataset was collected from a publicly available source containing details like:

* Company
* Model
* Year
* Fuel Type
* Kilometers Driven
* Selling Price

I did some manual cleaning and saved the final data as `car_data.csv`.

---

## 🔬 Technologies Used

* Python 🐍
* pandas, NumPy
* scikit-learn
* Flask
* HTML/CSS
* Bootstrap

---

## 🚀 Future Improvements

* Improve accuracy with more data and feature engineering
* Try advanced regressors (Random Forest, XGBoost)
* Add model evaluation metrics (R², MAE, RMSE)
* Include car images per brand/model
* Host it live with Heroku or Streamlit

---

## 🙌 Contribution & Feedback

This project is a personal learning initiative, but I'm open to:

* Feedback
* Suggestions
* Contributions

Feel free to fork or raise an issue!

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

**Thanks for checking it out! 🚗💻**