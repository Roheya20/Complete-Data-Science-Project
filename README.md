# Internship Selection Prediction

A machine learning project that uses applicant application features to predict whether an internship applicant is likely to be selected.

## 1. Objective

The objective of this project is to build a machine learning classification model that predicts internship selection outcomes based on applicant information.

The project explores how machine learning can support the analysis of internship applications and assist recruitment decision-making.

## 2. Dataset Description

The project uses an applicant dataset containing seven input features and one target variable representing the internship selection outcome.

The target variable is encoded as:
- `1` – Selected
- `0` – Not selected

**Data limitation:** Some features in the dataset were artificially generated for learning and experimentation. Therefore, the dataset may not fully represent real-world internship applicants or recruitment decisions.

## 3. Methodology

The project followed these main steps:

1. **Data cleaning:** Prepared the dataset for analysis and modelling.
2. **Feature preparation:** Selected the input features (X) and target variable (y).
3. **Data splitting:** Divided the dataset into training and testing sets using an 80/20 split.
4. **Model training:** Used Logistic Regression to learn patterns in the training data.
5. **Evaluation:** Evaluated the model using accuracy, precision, recall, and a confusion matrix.

Logistic Regression was selected because the task is a binary classification problem involving two possible outcomes.

## 4. Key Results

The Logistic Regression model achieved the following results:

| Evaluation metric | Result |
|---|---:|
| Accuracy | 60.00% |
| Precision | 66.67% |
| Recall | 85.71% |

**What the results mean:**

- **Accuracy (60%):** The model correctly predicted 60% of all cases in the test dataset.
- **Precision (66.67%):** Of the applicants predicted as selected, approximately 67% were actually selected.
- **Recall (85.71%):** The model identified approximately 86% of the applicants who were actually selected.

These results reflect performance on the available test data and should not be treated as proof of performance on real-world recruitment data.

## 5. Limitations and Recommendations

The dataset is relatively small, and some features were simulated. This limits how well the results may generalise to real internship selection processes.

A key recommendation is to collect a larger dataset containing genuine applicant information and selection outcomes, with appropriate privacy protections, to improve the model's reliability.

The model should support human decision-making rather than replace recruitment decisions.

## 6. Tools and Technologies

- Python
- Google Colab
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn (if used in the notebook)

## 7. How to Run the Notebook

1. Open the project notebook in Google Colab.
2. Ensure the required dataset is available.
3. Open the notebook.
4. Select **Runtime → Run all**.
5. Run the cells from top to bottom to reproduce the data preparation, model training, predictions, and evaluation results.

## 8. Project Walkthrough

A recorded walkthrough explaining the project's objective, methodology, results, limitations, and recommendation is available here:

**Walkthrough video:** [Insert your recording link here]

---

*This project was developed for educational purposes as an introduction to machine learning classification and model evaluation.*
