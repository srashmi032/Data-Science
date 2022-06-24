# Real Estate Price Prediction
Problem Statement:

To build a machine learning that predicts price of real estates based on some features

Steps to build a model:

1.load dataset:Here I am using boston house dataset from kaggle

2.Getting data information like number of rows and columns, their datatypes, mean, median and mode of all columns, finding correlation and plotting graphs 

3.Data pre processing: Dealing with missing values if any, converting values to suitable datatypes

4.Splitting dataset into training and test data (80:20 ratio)

5.Creating a pipeline and passing training data through it

6.Selecting best model with least root mean squared error

7.Fitting the selected model on my training dataset and saving my model in joblib file

8.This joblib model can be used for predicting the price based on input features

Results of various models are included in a text file.
