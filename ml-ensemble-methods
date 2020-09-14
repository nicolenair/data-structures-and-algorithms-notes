Here I review random forests and gradient boosting algorithms.

# Random Forests
1. Build many decision trees
2. Count the number of votes for each final class, and select the class with the most votes (you can average the predicted class probabilities)

## Augmentations:
1. BAGGING: sample from the dataset (with replacement, size of dataset) [BOOTSTRAP SAMPLES]
2. randomly sample features (so no one feature dominates) usually log_2(p) features where p = n_features

^ both of these reduce correlation between trees and improve final prediction

## Characteristics
1. you get OOB error for free
2. more accurate that single trees/logistic regression
3. 

# Boosting Algorithms

## Boosting
1. similar to random forests, but we IMPROVE the trees as we build them, by *reweighting the data* to give more weight to where we are not doing so well
2. not IID trees
3. stagewise additive modeling as opposed to generalized additive modeling (in statistics -- basis functions etc.) --. we fix other params. slows down overfitting (we don't overwrite old ones as easily)

##Characteristics
1. more prone to overfitting
2. we might grow shallow trees (as opposed to bushy random forest)
3. boosting stumps work remarkably well (one split, two terminal nodes)
4. can drive training error down to zero but when training error goes to zero, test error can still go down
5. 

## Examples
1. adaboost = additive logistic regression model
2. 

## Boosting for Regression (least squares boosting)
1. we repeatedly fit the residual (regression tree)
2. use shrinkage (with epsilon) like lr
3. 

