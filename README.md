# **Wine Quality Prediction**

## **Overview**
The **Wine Quality Prediction** project aims to predict the quality of red and white wines based on their chemical properties. Using a machine learning model, this project analyzes various features, such as acidity, alcohol content, and residual sugar, to predict a wine's quality on a scale from 0 to 10.

The dataset used for this project is the **Wine Quality Dataset**, which can be found on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Wine+Quality).

---

## **Project Structure**
```
wine_quality_prediction/
│
├── data/
│   ├── winequality-red.csv            # Wine dataset (red wine)
│
├── notebooks/
│   ├── data_analysis.ipynb             # Jupyter notebook for EDA
│
├── src/
│   ├── __init__.py                     # Init file for the src module
│   ├── data_preprocessing.py           # Script for data preprocessing and cleaning
│   ├── model_training.py               # Script for training the model
│   ├── evaluate_model.py               # Script for evaluating the model
│   ├── prediction.py                   # Script for making predictions
│
├── model/
│   ├── wine_quality_model.pkl          # Trained model saved as a pickle file
│
├── static/                             # Static folder for UI (optional)
│   └── css/
│
├── templates/                          # HTML templates for web UI (optional)
│   └── index.html
│
├── app.py                              # Flask application for deploying the project
├── requirements.txt                    # Project dependencies
├── Dockerfile                          # Docker file for containerization (optional)
└── README.md                           # Documentation file
```

---

## **Installation**

### **1. Clone the Repository**
First, clone the project repository to your local machine:
```bash
git clone https://github.com/yourusername/wine_quality_prediction.git
cd wine_quality_prediction
```

### **2. Install Dependencies**
Make sure you have Python installed (preferably Python 3.8+). Then, install the project dependencies:
```bash
pip install -r requirements.txt
```

### **3. Download Dataset**
Download the wine quality dataset (red wine or white wine) from the UCI repository:

- Red Wine: [winequality-red.csv](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv)
- White Wine: [winequality-white.csv](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv)

Place the dataset file into the `data/` folder.

---

## **Usage**

### **1. Train the Model**
To train the model, use the following command:
```bash
python src/model_training.py
```
This will train the model using the RandomForestClassifier and save it in the `model/` directory as `wine_quality_model.pkl`.

### **2. Evaluate the Model**
To evaluate the model's performance, run:
```bash
python src/evaluate_model.py
```
This will output a classification report with metrics such as precision, recall, and F1-score.

### **3. Make Predictions**
To predict wine quality using custom data, edit the sample data in the `src/prediction.py` script and run:
```bash
python src/prediction.py
```
This will output the predicted wine quality based on the input features.

---

## **Files and Scripts**

- `src/data_preprocessing.py`: Contains functions for loading, cleaning, and preprocessing the dataset (standardization, train-test split, etc.).
- `src/model_training.py`: The script for training the machine learning model using RandomForest.
- `src/evaluate_model.py`: Used to evaluate the trained model on the test set and generate a performance report.
- `src/prediction.py`: Contains the logic to make predictions using the trained model.
- `notebooks/data_analysis.ipynb`: Jupyter notebook for exploratory data analysis (EDA) and data visualization.
- `app.py`: A simple Flask application to deploy the model as a web service (optional for deployment).

---

## **Technologies Used**

- **Python** (3.8+)
- **Pandas** (for data manipulation)
- **Scikit-learn** (for machine learning model building)
- **Flask** (for building a web app)
- **Jupyter Notebook** (for data exploration)
- **Docker** (optional, for containerization)

---

## **Future Enhancements**

- **Hyperparameter tuning**: Improve the model's performance by tuning hyperparameters.
- **Web deployment**: Host the Flask web app on platforms like Heroku or AWS.
- **Additional Models**: Experiment with other machine learning models like SVM, Gradient Boosting, and XGBoost.
- **UI/UX**: Add a graphical user interface to allow non-technical users to interact with the model.

---

## **Contributors**
- [Your Name](https://github.com/yourusername)

---

## **License**
This project is licensed under the MIT License - see the `LICENSE` file for details.

---