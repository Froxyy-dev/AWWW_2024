



# List of Machine Learning Algorithms

## List of algorithms

### Linear Regression [Link for wikipedia description](linear_regression.md)


Perhaps the most commonly used machine learning algorithm, linear regression, predicts the relationship between two variables. This simple algorithm is used to make linear predictions based on a set of training data. Linear regression can be used for classification and regression problems, and it is often one of the first algorithms people learn when they start machine learning.

### Logistic Regression [Link for wikipedia description](logistic_regression.md)


Like linear regression, logistic regression predicts the relationship between two variables. However, instead of predicting continuous values like a real number or percentage, logistic regression predicts whether an outcome will occur. As such, it uses a binary classification model to make predictions.

### Support Vector Machines  [Link for wikipedia description](support_vector_machines .md)


Support vector machines, or SVMs for short, are used for regression and classification problems. They work by using past examples to build a model that can be used to classify new data points. SVMs are one of the most powerful classification algorithms available, and they have been shown to outperform other popular classification algorithms in many different situations.

### One-Class SVM [Link for wikipedia description](one-class_svm.md)


Much like regular SVMs, one-class SVMs are used for classification problems. However, this algorithm uses a hypersphere instead of using a hyperplane to identify which data points belong to the same class. It can encompass only a single class of data points, allowing it to be used for novelty or outlier detection.

### Decision Trees [Link for wikipedia description](decision_trees.md)


If you’ve ever seen a flowchart or flow diagram, then you’ve seen a decision tree in action. As the name suggests, decision trees are used to make decisions based on the data that has been provided. Each branching point in the diagram represents an algorithm that will be executed on the input data. This process is repeated for each branch until a final decision is reached at the end of the tree.

### Random Forest [Link for wikipedia description](random_forest.md)


A random forest is used to build multiple decision trees based on the same training data. As each tree is generated, random subsets of the data are used to train the tree. This process is repeated for each individual tree in the forest, which means that there will be thousands or even millions of different decision trees within a single model.

### Isolation Forest [Link for wikipedia description](isolation_forest.md)


The isolation forest is to the decision tree what One-Class SVM is to SVM. In other words, it uses random subspaces to identify outliers within a dataset. These anomalies are then further examined to see if they are truly outliers or just part of the normal distribution. Isolation forests detect the distance of a data point from the rest of the data set and can deal with both numerical and categorical features.

### Gradient Boosting [Link for wikipedia description](gradient_boosting.md)


Gradient boosting is a powerful machine learning algorithm that combines multiple “weak learners” into a single predictive model. For example, it could be used to combine the output of several decision trees or to combine multiple support vector machines. The result is an algorithm that often outperforms the random forest and other machine learning algorithms in terms of predictive performance.

### Neural Networks [Link for wikipedia description](neural_networks.md)


Neural networks are a type of machine learning algorithm that is loosely based on the structure and function of the human brain. They consist of several interconnected nodes, commonly referred to as neurons, which can be configured to process data differently. Weights are assigned to the connections between each node, allowing the network to “learn” from the provided data.

### Principal Component Analysis [Link for wikipedia description](principal_component_analysis.md)


Next, PCA, or principal component analysis, is a pattern-detection algorithm commonly used in conjunction with neural networks. It works by finding a direction within a dataset that maximizes the variance of that data. This allows it to reduce the dimensionality of a dataset by pulling out patterns and trends, which can then be used for more detailed analysis.

### Linear Discriminant Analysis [Link for wikipedia description](linear_discriminant_analysis.md)


LDA, or linear discriminant analysis, is similar to Fisher’s linear discriminant analysis used in statistics. It uses data analysis to predict a categorical output based on multiple features. The relationship between features is used to make predictions about the future outcome. Both the features and the output can be continuous or categorical, making this a very versatile algorithm for many different types of machine-learning problems.

### K-Means Clustering [Link for wikipedia description](k-means_clustering.md)


To cluster simply means to categorize data points based on similarities. K-means clustering is a common technique for unsupervised machine learning, meaning it is used without any labeled training data. It works by assigning each data point to a cluster using the Euclidean distance between them, intending to minimize variance within groups while maximizing the similarity between clusters.

### Hierarchical Clustering [Link for wikipedia description](hierarchical_clustering.md)


Taking things one step further, hierarchical clustering uses an organized tree structure to cluster data points. This allows it to create clusters containing not just individual data points but entire groups. In essence, you build a hierarchy of clusters, with individual clusters being clustered themselves.

### DBSCAN [Link for wikipedia description](dbscan.md)


Density-based spatial clustering of applications with noise, or DBSCAN for short, is another type of unsupervised machine learning algorithm. It works by taking into account the distance between data points and their density to create clusters that contain both close points and those with high densities. The highest-density clusters are determined first, which allows the algorithm to focus on these high-quality clusters before moving on to lower-quality ones.

### Autoencoders [Link for wikipedia description](autoencoders.md)


Another unsupervised algorithm, autoencoders, are neural networks that are used for dimension reduction. They take an input, encode it in a lower-dimensional space that preserves the most important information, and then decode the data into its original form. The end result is a compressed version of the original data that can be used for analysis and comparison.

### Locally Linear Embedding [Link for wikipedia description](locally_linear_embedding.md)


Locally linear embedding, or LLE for short, is a dimensionality reduction algorithm that uses low-dimensional manifolds to map high-dimensional data points. It finds similar data points and maps them to nearby locations on the manifold. This allows it to preserve local distances within the dataset while preserving global distances between different data clusters.

### t-SNE [Link for wikipedia description](t-sne.md)


In addition to LLE, t-SNE, or t-distributed stochastic neighbor embedding, is another commonly used dimensionality reduction algorithm. It works by using a probability distribution over pairs of points to preserve important features within the data while minimizing noise and other irrelevant information. A 2D or 3D representation is then created based on this probability distribution, which can be used for visualization and analysis of the data.

### Independent Component Analysis (ICA) [Link for wikipedia description](independent_component_analysis_(ica).md)


ICA is used to find independent components within a dataset. These “hidden patterns” can then be used to make predictions or extract more information about the data. It assumes that maximum one of the components in a given dataset is Gaussian and the other components are independent of each other.

### Factor Analysis [Link for wikipedia description](factor_analysis.md)


Factor analysis observes variability in data. It seeks to identify a relatively small number of unobserved variables that explain the observed variability, called factors. It reduces the need for data collection by focusing on the relationships between existing variables.

### Naive Bayes [Link for wikipedia description](naive_bayes.md)


Bayes’ theorem is a fundamental statistic theorem that allows us to make predictions about future observations considering the relations between different variables. Naive Bayes is a simple machine learning algorithm based on this theorem that assumes that each variable is independent of the others. This allows it to easily model complex data using only a small amount of training data. Naive Bayes is commonly used for classification tasks as a simple yet effective algorithm.

### Bagging [Link for wikipedia description](bagging.md)


Bootstrap aggregating, or bagging for short, is a type of machine learning algorithm that uses resampling techniques to create subsamples of the training data. This means that you can use individual data points multiple times to train a model, improving the algorithm’s overall performance. Once the models have been trained, they are combined in some way to make a final prediction.

### Dimensionality Reduction [Link for wikipedia description](dimensionality_reduction.md)


Finally, dimensionality reduction is another important technique for working with high-dimensional data. It refers to any method that reduces the number of dimensions in a dataset while preserving the most relevant information. Common methods include principal component analysis, k-nearest neighbors, and clustering algorithms like k-means or spectral clustering. With proper dimensionality reduction, we can gain important insights about our data and make more accurate predictions.
