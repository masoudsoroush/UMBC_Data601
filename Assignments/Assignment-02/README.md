# The Top 250 Movies of All Times
![](TopMovies.png)

## Overview
When it comes to movies, everyone has their favorites! Although looking for *best movies of all times* is to some extent a subjective matter, we would like to list the top 250 movies of all times produced in the past century (*i.e.* 1920-2019) based on the average ratings of both general and critic audiences of the movies. We will be collecting and analyzing the qualitative as well as some quantitative characteristics of these movies.

## Goals
This project has three main goals:

1.a. We identify the top 250 movies of all times according to the ranking of the website https://www.listchallenges.com/reel-stats-statistical-top-250-movies-of-all-time through *webscraping*. In this stage of the process, we collect the collect the following characteristics: Movie's Name, Production Year, and url of the movie in the rottentomatoes encyclopedia (https://www.rottentomatoes.com/). 

1.b. For each of the 250 movies obtained from 1.a., we find the movie in the *rottentomates* website, and extract the following information through webscraping: 
  * Genre
  * Runtime (Movie's length)
  * Box Office (*i.e.* how much, in US dollars, the movie sold tickets in cinemas)
  * Critic Ratings (The average rating given by the critics of rottentomatoes)
  * Audience Ratings (The average rating given by general auidience)
  
By the end of this step, we will produce a dataframe consisting of 250 rows corresponding to the top 250 movies of all times, and 8 columns corresponding to the above mentioned characteristics.

2. After collecting all the necessary information in the previous step, we cleanse the data, and store it for the final analysis in step 3. In this process, there is however a nontrivial step. We would like to be able to compare the values of the *Box Office* of these 250 movies with each other. This comparison cannot be performed naively, as the box offices of different movies have been obtained in different years! To overcome this problem, we collect the value of US dollar in the past 100 years through the CPI index read (and stored as a txt file) from https://www.usinflationcalculator.com/. The CPI/inflation index allows us to convert the value of box office of all movies to the current value in 2020.       

3. In the final goal of this project is to analyze the few quantitaive variables of the top 250 movies of all times. We will specifically answer the following questions from the collected data in the previous steps:
  * How are the Critic Ratings and Audience Ratings distributed? Does the shape of distribution of Critic Ratings necessarily agree with the shape of distribution of Audience Ratings?
  * What decade in the previous century (*i.e.* 1920-2019) has been the most productive decade in terms of producing the best movies?
  * How are the Box Office values for the top 250 movies of all times (*after converting all of them to their values in 2020*) distributed?
  











## References
1. Movies Ranking Website: https://www.listchallenges.com/reel-stats-statistical-top-250-movies-of-all-time
2. The Movie Encyclopedia Website: https://www.rottentomatoes.com/
