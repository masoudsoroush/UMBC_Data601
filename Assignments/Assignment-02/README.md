# The Top 250 Movies of All Times
![](TopMovies.png)

## Overview
When it comes to movies, everyone has their favorites! Although looking for *best movies of all times* is to some extent a subjective matter, we would like to list the top 250 movies of all times produced in the past century (*i.e.* 1920-2019) based on the average ratings of both general and critic audiences of the movies. We will be collecting and analyzing the qualitative as well as some quantitative characteristics of the 250 collected movies.

## Goals
This project has three main goals:

1.a. We identify the top 250 movies of all times according to the ranking of the website https://www.listchallenges.com/reel-stats-statistical-top-250-movies-of-all-time through *webscraping*. In this stage of the process, we collect the following characteristics: Movie's Name, Production Year, and url of the movie in the rottentomatoes encyclopedia (https://www.rottentomatoes.com/). 

1.b. For each of the 250 movies obtained from 1.a., we find the movie in the *rottentomates* website, and extract the following information about the movie by  webscraping: 
  * Genre
  * Runtime (Movie's length)
  * Box Office (*i.e.* how much, in US dollars, the movie sold tickets in cinemas)
  * Critic Ratings (The average rating given by the critics of rottentomatoes)
  * Audience Ratings (The average rating given by general auidience)
  



2. After collecting all the necessary information in the previous step, we cleanse the data, and store it for the final analysis in step 3. In this process, there is however a nontrivial step. We would like to be able to compare the values of the *Box Office* of these 250 movies with each other. This comparison cannot be performed naively, as the box office values of different movies have been obtained in different years! To overcome this problem, we collect the value of US dollar in the past 100 years through the CPI index read (and stored as a txt file) from https://www.usinflationcalculator.com/. The CPI/inflation index allows us to convert the values of box office of all movies to the current value in 2020.       

3. In the final step of this project, we analyze the few quantitaive variables of the top 250 movies of all times. We will specifically answer the following questions from the collected data in the previous steps:
    * How are the Critic Ratings and Audience Ratings distributed? Does the shape of distribution of Critic Ratings necessarily agree with the shape of distribution of Audience Ratings?
    * What decade in the previous century (*i.e.* 1920-2019) has been the most productive decade in terms of producing the best movies?
    * How are the Box Office values for the top 250 movies of all times (*after converting all of them to their values in 2020*) distributed?

## Conclusions
Our study in this project reaches the following conclusions:
* The shape of distributions of the Critic Ratings, and the Audience Ratings are qualitatively different. The Audience Ratings distribution tends to towards a symmetric distribution whereas the Critic Ratings distribution is completely left-skewed. 
* The most productive decade of cinema during the past 100 years in terms of producing best movies is 1950-1960. After that, 1990-2000 is the second most productive decade of cinema. Interestingly, we find that 1930-1940, is the least productive decade for producing best movies! This period is coincidentally the period between Word War I and World War II.
* The distribution of the Box Office values of the top 250 movies of all times reveals that in terms of the value of US dollar in 2020, the highest frequency belongs to the interval 0.5-0.6 Billion dollars.

## Navigation
1. In the first step, the notebook HW-2-WebScraping.ipynb collects the data of the best 250 movies of all times (in accordance with Goals 1.a. and 1.b.) and stores the obtained data in the csv file '250-Best-Movies.csv' (which is also available in this repository). By the end of this step, we will produce a dataframe consisting of 250 rows corresponding to the top 250 movies of all times, and 8 columns corresponding to the above mentioned characteristics.
2. In the second step, the notebook HW-2-Data-Cleansing.ipynb cleans the collected data in the file '250-Best-Movies.csv' (in accordance with Goals 2.) and stores the cleansed data in the new csv file 'Cleansed_Data.csv' (which is also available in this repository). This notebook uses a text file ('CPI-Conversion.txt' which is available in this repository) in which all the CPI/inflation indices have been stored.  
3. In the final step, the notebook HW-2-DataAnalysis receives the data stored in 'Cleansed_Data.csv'. This notebook is responsible for the data analysis part of the task.

## Software Requirements and Packages
The above notebooks use the following libraries and python packages:
1. 'requests' for webscraping
2. 'BeautifulSoup' for webscraping
3. The standard 'numpy', 'pandas', 'matplotlib', and 'seaborn'  libraries for data cleansing and data analysis

## Data
1. The outcome of the webscraping performed in HW-2-WebScraping.ipynb (step 1. of Navigation) is stored in '250-Best-Movies.csv' as a dataframe consisting 250 rows corresponding to the 250 best movies, and 8 columns capturing the characteristics of the movies.
2. The outcome of the data cleansing performed in HW-2-Data-Cleansing.ipynb (step 2. of Navigation) is stored in 'Cleansed_Data.csv' as a new dataframe consisting 250 rows (corresponding to the top 250 movies), and 9 columns. The one extra column of the dataframe correcponds to the conversion of the value of the Box Office to the year 2020.
3. 'CPI-Conversion.txt' consists of the CPI indecies of the past 100 years (*i.e.* 1920-2020) is used in the notebook HW-2-Data-Cleansing.ipynb. This simple text file has 100 rows corresponding to the past 100 years, and two columns capturing 'year' and 'CPI index'.




## References
1. Movies Ranking Website: https://www.listchallenges.com/reel-stats-statistical-top-250-movies-of-all-time
2. The Movie Encyclopedia Website: https://www.rottentomatoes.com/
3. CPI/Inflation Index Website: https://www.usinflationcalculator.com/
