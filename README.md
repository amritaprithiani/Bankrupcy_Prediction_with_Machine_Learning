# Predicting Bankruptcy with Machine Learning

## Project Description / Outline

Predicting Bankruptcy involves examining various financial performance measures of financially distressed firms.

This process is important for financial institutions and investors as they evaluate performance and make predictions to manage lending risks.

This project uses financial data NASDAQ and incorporates machine learning classification algorithms to determine bankruptcy predictions.

Goal of this Project is to predict if company will go bankrupt within a given period of time based on data gathered.

----

## Tecnologies

Language: Python 3.9.12

Libraries used:

Pandas
Pathlib
Jupyter Labs
Scikit-Learn
Imblanced-Learn

----

## Installation Guide

conda install pandas
conda install jupyterlab
conda install -U Scikit-Learn
conda install scikit-learn

----

## Datasets

Data used among this project is gathered at the link below

- [Github Repository](https://github.com/sowide/bankruptcy_dataset)
- [Bankruptcy American Dataset](Resources/american_bankruptcy_dataset)

----

## Content

1. Importing libraries
2. Importing and organizing data:

- Relabling the columns

3. Preprocessing:

- Confirming missing data
- scaling and spliting data
- Oversampling with SMOTE

4. Modeling:

- k-Fold cross validation
- Decision Tree Classifier
- Random Forest Classifier
- XGBoost

4. Model Analysis:

- Confusion Matrix
- Classification report

![Random Forest Classifier](/Random_Forest.png)

----

## Conclusion:

As per the evaluation for the 3 classification models: Random Forests, Decision Tree, and XG Boost. While all 3 models are performing well, Random Forests gave the maximum accuracy. Both precision and recall showed 90%+ with F1 score of 92%. Primary drivers for model performance was to ensure the data is balanced, scaled and cleaned. Balanced data was achieved by oversampling minority class labels using Synthetic Miniority Oversampling technique. Kfold technique was used for model evaluation and this helped with giving better insights into our data and model.

----

### Resources

- [Machine Learning for Bankruptcy Prediction in the American Stock Market: Dataset and Benchmarks](https://www.mdpi.com/1999-5903/14/8/244/htm)
- [Bankruptcy prediction dataset for american companies in the stock market](https://github.com/sowide/bankruptcy_dataset)
- [Bankruptcy Prediction](https://www.kaggle.com/code/gcdatkin/bankruptcy-prediction/notebook)
- [How to Plot a Confusion Matrix from a K-Fold Cross-Validation](https://towardsdatascience.com/how-to-plot-a-confusion-matrix-from-a-k-fold-cross-validation-b607317e9874)
