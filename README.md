# Predictive Modeling of Water Quality Parameters for Fish Farming
## Introduction
Aquaculture, the farming of aquatic organisms in controlled environments, is crucial for ensuring the sustainability and productivity of fish farming operations. Real-time monitoring of water parameters like turbidity, pH, and temperature is essential. This project aims to develop a predictive model to optimize fish farming practices by forecasting conditions that maximize fish production.

## Overview
This project is focused on classifying different types of fish based on their environmental conditions. The dataset includes features such as pH, temperature, and turbidity of water, which are used to predict the type of fish present.

## Dataset
The dataset used in this project is `fish_dataset.csv`, which includes the following columns:
- `ph`: pH level of the water
- `temperature`: Temperature of the water
- `turbidity`: Turbidity of the water
- `fish`: Type of fish (target variable)

## Libraries Used
This project uses various Python libraries for data processing, model training, and evaluation:
- `numpy`
- `pandas`
- `seaborn`
- `matplotlib`
- `scikit-learn`
- `xgboost`
- `pickle`

## Project Workflow

1. **Data Preprocessing**:
    - Load the dataset
    - Encode the target variable
    - Compute and visualize the correlation matrix

2. **Data Splitting**:
    - Split the dataset into training and testing sets
    - Further split the training set into a validation set

3. **Model Training and Evaluation**:
    - Logistic Regression
    - K-Nearest Neighbors (KNN)
    - Decision Tree
    - Random Forest
    - AdaBoost
    - Support Vector Machine (SVM)
    - XGBoost

4. **Model Saving**:
    - Save the best-performing Random Forest model using `pickle`
5. **User Interface**:
    - The project includes a mobile-based information system providing real-time recommendations and insights to farmers.

## Installation
To run the code, you need to have Python and the required libraries installed. You can install the necessary libraries using pip:
```
pip install numpy pandas seaborn matplotlib scikit-learn xgboost
```
