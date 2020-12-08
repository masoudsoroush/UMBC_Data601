# Food Nutrients: An Unsupervised Learning 
<p align="center">
<img src="Food_Nutrients.png" width=800, height=400>

## Overview

-- **What is the problem?**

We focus on a large number of food items (8618 items) and their different food nutrients (23 nutrients). Our goal in this project is twofold. First, we desire to only focus on a smaller subset of the food nutrients. Not all of the food ingredients are equally important. Using PCA, we would like to find a subset of the 23 nutrients which is responsible for the major part of the variation in the food nutrients. Second, after reducing the number of features (*i.e.* food nutrients), we would like to classify the 8618 food items into a number of clusters, using k-means clustering algorithm.  

-- **Metrics of Success**

In this project, we aim to achieve the following goals:

   1. *Reducing the number of food ingredients*: Using PCA, we reduce the number of features (food nutrients in this context) to a smaller subset so that the a large portion of variance is still captured.
   2. *Understanding the properties of the new features*: Each new feature will be a linear combination of the old features. We would like to obtain a qualitative understanding of the new features. For instance, we would like to understand that what old features vary most for each new feature.    
   3. *Clustering the food items*: After reducing the number of features (through the PCA algorithm), we intend to classify the food items into a number of clusters, using the k-means algorithm approach.
   4. *Understanding the properties of the clusters*: We would like to obtain a good understanding of the clusters. Among many factors, we intend to determine the size of each cluster, the food items in each cluster, and whether or not some clusters will be more significant than others.
   
**-- Why is this project important?**

Most people know good nutrition and physical activity can help maintain a healthy weight. But the benefits of good nutrition go beyond just weight. Having a good understanding of the nutrition factors and applying this knowledge in decision making when it comes to foods can have an immense impact in one's physical and mental health. However, the problem is that there are too many food items and too many food nutrients! Also, not all nutrients are on equal footing! Therefore, picking the most relevant factors and classifying the food items according to picked nutrients is of vital importance.

