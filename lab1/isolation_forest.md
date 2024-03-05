



# Isolation Forest

## Description


The isolation forest is to the decision tree what One-Class SVM is to SVM. In other words, it uses random subspaces to identify outliers within a dataset. These anomalies are then further examined to see if they are truly outliers or just part of the normal distribution. Isolation forests detect the distance of a data point from the rest of the data set and can deal with both numerical and categorical features.

## Duck response

### Isolation forest - Wikipedia [link to wikipedia](https://en.wikipedia.org/wiki/Isolation_forest)

### Wikipedia description


Isolation Forest is an algorithm for data anomaly detection initially developed by Fei Tony Liu in 2008. Isolation Forest detects anomalies using binary trees. The algorithm has a linear time complexity and a low memory requirement, which works well with high-volume data.
In essence, the algorithm relies upon the characteristics of anomalies, i.e., being few and different, in order to detect anomalies. No density estimation is performed in the algorithm. The algorithm is different from decision tree algorithms in that only the path-length measure or approximation is being used to generate the anomaly score, no leaf node statistics on class distribution or target value is needed.

### Wikipedia image


![Image: ](https://tse2.mm.bing.net/th?id=OIP.uJXoY1sA7kXM2k6tCw3T8AHaCy&pid=Api)