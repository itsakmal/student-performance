# Student Math Score Prediction

This project predicts the **Math Score** of students based on demographic and academic features using a range of regression models. It is designed to help educators understand which students may need academic support based on related factors such as reading and writing performance, parental education, and preparation levels.

---

## Table of Contents

- [Features Used](#features-used)
- [Models Used](#models-used)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

---

## Features Used

The following features are used as input:

- **Gender**: The student's gender.
- **Race/ethnicity**: The student's racial or ethnic background.
- **Parental level of education**: The highest education level attained by a parent.
- **Lunch type**: Whether the student receives standard or free/reduced lunch.
- **Test preparation course**: Whether the student completed a test preparation course.
- **Reading Score**: The student's score in a reading exam.
- **Writing Score**: The student's score in a writing exam.

---

## Models Used

The following regression models were implemented and compared:

| Model Name                | Description                                                 |
|---------------------------|--------------------------------------------------------------|
| Random Forest Regressor   | An ensemble learning method that constructs a multitude of decision trees during training and outputs the mean prediction of the individual trees to reduce overfitting and improve accuracy. |
| Decision Tree Regressor   | A non-parametric supervised learning method used for regression. It approximates a sine curve with a set of if-then-else decision rules. |
| Gradient Boosting Regressor | A boosting method that builds an ensemble of weak prediction models, typically decision trees, in a stage-wise fashion; it generalizes them by allowing optimization of an arbitrary differentiable loss function. |
| Linear Regression         | A statistical model that models the linear relationship between a scalar response and one or more explanatory variables (also known as dependent and independent variables). |
| K-Neighbors Regressor     | A non-parametric method used for regression that predicts the value of a new data point based on the average of its 'k' nearest neighbors in the feature space. |
| XGBRegressor              | An optimized distributed gradient boosting library designed to be highly efficient, flexible, and portable. It implements machine learning algorithms under the Gradient Boosting framework. |
| CatBoosting Regressor     | A high-performance open-source gradient boosting on decision trees library. It is optimized for working with categorical features, automatically handling them without requiring explicit pre-processing. |
| AdaBoost Regressor        | An ensemble meta-algorithm that can be used with many other types of learning algorithms to improve performance. It works by fitting a sequence of weak learners on re-weighted versions of the data. |

---

## Dataset

The dataset used for this project is "Students Performance in Exams" and can be found on Kaggle:

[Students Performance in Exams Dataset](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)

---
## Installation

To get started with this project, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/itsakmal/student-performance.git
    cd student-performance
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    * On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    * On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` file contains the following dependencies:
    ```
    pandas
    numpy
    seaborn
    matplotlib
    scikit-learn
    catboost
    xgboost
    dill
    streamlit
    ```

---

## Usage

After installation, you can run the prediction script.

1.  **Ensure the dataset is available:**
    The original dataset `data.csv` (or `StudentsPerformance.csv` from Kaggle, which you'll need to rename or adjust paths) should be present in the `artifacts/` directory, along with `train.csv` and `test.csv` which are likely generated during data splitting.

2.  **Run the main application (e.g., Streamlit app):**

    If `app.py` is your Streamlit application, run it using:
    ```bash
    streamlit run app.py
    ```

    This will open a web browser with the Streamlit application, where you can interact with the model.

    If `app.py` is a standard Python script for training/evaluation, run it using:
    ```bash
    python app.py
    ```

    The script will typically:
    * Load the data from `artifacts/`.
    * Preprocess the data (potentially using `preprocessor.pkl`).
    * Train and evaluate each of the specified models, or load a pre-trained model (`model.pkl`).
    * Output the performance metrics for each model or provide predictions via the web interface.

---

## Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeatureName`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add Your Feature'`).
5.  Push to the branch (`git push origin feature/YourFeatureName`).
6.  Open a Pull Request.

---
