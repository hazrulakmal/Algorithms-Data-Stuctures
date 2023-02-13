#write a code workflow for classifcation task that takes in a dataset and returns the model performance metrics
#the model should be a random forest classifier
#the dataset should be a csv file
#the model performance metrics should be a dataframe with the following columns: accuracy, precision, recall, f1 score, and auc
#worfklow should involve the following steps:
#1. read in the dataset
#2. split the dataset into train and test sets
#3. feature engineering the dataset
    #(e.g. one hot encoding, imputing missing values, scaling, etc.)

#4. feature selection
#5. train the model
#6. Tune the model (kfolds cross validation)
#7. evaluate the model
#8. return the model performance metrics

library(tidyverse)
library(caret)
library(ranger)
library(randomForest)
library(rpart)
library(rpart.plot)
library(rattle)

1. 


