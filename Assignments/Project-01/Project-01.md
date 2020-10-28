# Project 1: Seattle's Weather - An Opportunity for Logistic Regression
<p align="center">
<img src="rainy-seattle.png" width=800, height=400>

## Overview 
The major weather indicators of Seattle's weather have been recorded for more than 25000 consecutive days from 1948 to 2017. This data set is publicly accessible at Kaggle. In this data set, the minimum and the maximum temperatures of each day of the year for the period 1948 to 2017 have been recorded. Moreover, the rain situation for each day has been recorded as a True/False boolean variable. In a seperate column, the precipitation rates for rainy days have been recorded as well. In this project, we would like to employ the logistic regression method to build a simple model for predicting whether a typical day will be rainy.

## Goals of the Project
In this project, we perform logistic regression at different levels:

1. We will first perform a supervised learning through logistic regression model by treating the maximum temperature ('TMAX') and the minimum temperature ('TMIN') as the two only features of our model. The boolean rain variable ('RAIN') will be regarded as our categorical target variable. We will perform a *binary logistic regression with two features* on our data set, and we will explore the success of our model.

2. We will add one more feature to our model, and we will perform a *binary logistic regression with three features*. The new feature is built from the date ('DATE') variable. We will do this in two ways. As we will see, the second way (we call it The More Refined Approach) will lead to a better performance of the model.

3. We will perform a multinominal logistic regression. We will use the precipitation variable of our dataset to create 4 classes (instead of only two classes rainy, and not rainy) for our taget variable. The four classes are: No Rain, Light Rain, Moderate Rain, and Heavy Rain. We will perform the multinomial logistic regression both with two and three features.

## Conclusions and Possible Future Directions
At the end of our analysis, we draw the following conclusions:

  1. As is observed by the decision regions plots, the data is highly degenerate. Nonetheless, the binary logistic regression is predicting the class of the target variable for 75% of the test data.
  
  2. When a third feature is correctly added (*i.e.* consistent with the nature of the logistics regression as we saw in section 2.1.3.) to the analysis of binary logistic regression, the decision regions are less degenerate, and the rate of the correct predictions for the test data slightly improves. 
  
  3. When more classes added to the model, the rate of the correct predictions for test data drops by at least 15%. This is an indicator of the fact that the multiclass model is very complex, and one cannot optimally analyze the model with only very few features. Perhaps, adding more variables/features such as the air pressure, the speed and the direction of the wind would improve the analysis. However, it is worth noticing that when we add our third feature (*i.e.* FREQUENCY), we do see a slightly better performance, just as the case of the binary analysis.
  

It would be interesting to extend our analysis in future in two different directions:


  1. The logistic regression analysis we performed here is based on the sigmoid function. It would be interesting to perform a similar modeling with other bounded functions that one can take into consideration.
  
  2. It would be interesting to examine other machine learning algorithms (different from logistic regression) on the same dataset and compare the performances of different models.
 
## Navigation
1. The main notebook which represents our logistic regression analysis is Seattle's_Weather.ipynb.
2. The functions that will be used in above notebook have been stored in the functions.py file. For convenience, a ipynb version of this file has been added to this repository as well. 
3. Our dataset file 'SeattleWeather.csv' is accessible as a csv file.

## Software and Packages
We will use the following python libraries:

- For data wrangling, we use the standard *pandas* and *numpy* libraries.
- For data visualization and plotting, we use the standard *matplotlib* and *seaborn* libraries, as well as *mlxtend* library.
- For data training and logistic regression, we use various features of *scikit learn* library. 

## Data Resources and References 
1. Main source of data for Seattle's weather is found at kaggle.com through the following link:<br> 
https://www.kaggle.com/rtatman/did-it-rain-in-seattle-19482017?select=seattleWeather_1948-2017.csv
2. NC Climate Office for Types of Precipitations: https://climate.ncsu.edu/edu/PrecipTypes
