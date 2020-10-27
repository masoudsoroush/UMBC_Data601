# Project 1: Seattle's Weather - An Opportunity for Logistic Regression
<p align="center">
<img src="rainy-seattle.png" width=800, height=400>

## Overview 
The major weather indicators of Seattle's weather have been recorded for more than 25000 consecutive days from 1948 to 2017. This data set is publicly accessible at Kaggle. In this data set, the minimum and the maximum temperatures of each day of the year for the period 1948 to 2017 have been recorded. Moreover, the rain situation for each day has been recorded as a True/False boolean variable. In a seperate column, the precipitation rates for rainy days have been recorded as well. In this project, we would like to employ the logistic regression method to build a simple model for predicting whether a typical day will be rainy.

## Goals of the Project
In this project, we perform logistic regression at different levels:

1. We will first perform a supervised learning through logistic regression model by treating the maximum temperature ('TMAX') and the minimum temperature ('TMIN') as the two only features of our model. The boolean rain variable ('RAIN') will be regarded as our categorical target variable. We will perform a *binary logistic regression with two features* on our data set, and we will explore the success of our model.
