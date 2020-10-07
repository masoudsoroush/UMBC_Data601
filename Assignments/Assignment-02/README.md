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
  * Box Office (*i.e.* how much the movie sold tickets in cinemas)
  * Critic Ratings (The average rating given by the critics of rottentomatoes)
  * Audience Ratings (The average rating given by general auidience)
  
By the end of this step, we will produce a dataframe consisting of 250 rows corresponding to the top 250 movies of all times, and 8 columns corresponding to the above mentioned characteristics.

2. After collecting all the necessary information in the previous step, we cleanse the data, and store it for the final analysis.  

3. 











## References
1. Movies Ranking Website: https://www.listchallenges.com/reel-stats-statistical-top-250-movies-of-all-time
2. The Movie Encyclopedia Website: https://www.rottentomatoes.com/
