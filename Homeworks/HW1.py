# 1) Machine learning is a branch of artificial intelligence (AI) 
# that allows computers to learn from examples without being explicitly programmed.

# 2) The difference between supervised and unsupervised learning is that in a supervised learning model,
# the algorithm learns on a labeled dataset, providing an answer key that the algorithm can use to evaluate its accuracy on training data. 
# An unsupervised model, in contrast, provides unlabeled data that the algorithm tries to make sense of by extracting features and 
# patterns on its own. And also supervised learning models are used for classification and regression problems while unsupervised learning 
# models are used for clustering problems.
# As examples of supervised models we can cite: "Linear Regression" for regression problems, "Support Vector Machine" for classification problems 
# and regression problems, and "Random Forest" for both classification and regression.
# As examples of unsupervised models we can cite: "K-Means Clustering" which clusters the data points into a number (K) of mutually exclusive clusters,
# "Hierarchical Clustering" that clusters the data points into parent and child clusters, and "Probabilistic Clustering" which clusters the data points 
# into clusters on a probabilistic scale.

# 3) Test set: is a set of examples used only to assess the performance of a fully-specified classifier.
# Validation set: is a set of examples used to tune the parameters of a classifier. It is used to select proper parameters of the system, it is part
# of the training set.
# We to use validation set to compare the performances of the prediction algorithms that where created based on training set.
# We apply our chosen prediction algorithm on our test set in order to see how it is going to perform so we can have an idea about our algorithm's
# performance on unseed data.

# 4) The main preprocessing steps are:
# - Removing duplicates values: in most cases, we need to check and remove the duplicates values in order not to affect on our model's performance;
# - Balancing dataset: imbalanced data refers to a problem with classification problems where the classes are not represented equally. We need to balance 
# the dataset to avoid the memorization of the mojority classe or the minority one by our performed algorithm. In order to balance the data, we use 
# oversampling or undersampling;
# - Eliminating the missing values by fiiling with median or mean;
# - Detecting outliers: outliers are extreme values that deviate from other observations on data , they may indicate a variability in a measurement,
# experimental errors or a novelty. The common used outliers detecting techniques are: satandart deviation, box Plots/IQR calculation and isolation forest;
# - Feature scaling: Feature scaling in machine learning is one of the most critical steps during the pre-processing of data before creating a machine learning model. 
# Scaling can make a difference between a weak machine learning model and a better one. 
# The most common techniques of feature scaling are Normalization and Standardization;
# -Bucketing (Binning): data binning, bucketing is a data pre-processing method used to minimize the effects of small observation errors. 
# The original data values are divided into small intervals known as bins and then they are replaced by a general value calculated for that bin;
# - Extracting feature: Feature Extraction aims to reduce the number of features in a dataset by creating new features from the existing ones;
# - Feature Encoding: feature encoding is basically performing transformations on the data such that it can be easily accepted as input for machine 
# learning algorithms while still retaining its original meaning.
# - Spliting the dataset into train, validation and test set before performing any processing.
# We need to prepare our data by using some preprocessing steps to minimize the error and to increase the performance of our trained model to perform better prediction.

# 5) 
# 6)
