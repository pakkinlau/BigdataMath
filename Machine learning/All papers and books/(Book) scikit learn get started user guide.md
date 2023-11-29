- 14-12-2022: created

- Chapter 3: model selection and evaluation


- Overfitting: 
	- A model would that would have a perfect score but fail to predict anything useful yet-unseen data. 
	- To avoid it, we hold out part of the available data as a test set. Putting test data to the model as a way of testing its prediction power. In this way, the model in the training session should not have any information from the test set.
	- 
  - Best parameter
	  - Can be determined by grid search techniques

![[Pasted image 20221214015056.png|400]]
- Fig: the flowchart of the location of the cross-validation 

- Example pipeline of machine learning. It gives us a very high performance score.
```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm

# X and y should comes from the same tabular data source.
X, y = datasets.load_iris(return_X_y=True)

# by checking the shape of the dataset, we know we have the same amount of X and y. 
X.shape, y.shape

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=0)

# We check the size of X and y again, to verify the size of samples are probably divided. 
X_train.shape, y_train.shape
X_test.shape, y_test.shape

clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
clf.score(X_test, y_test)
# 0.966666...
```