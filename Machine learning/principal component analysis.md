---
category:
alias: PCA
---

---

- Figure: example given by Nathan Kutz
![[Pasted image 20231105020930.png]]

---
- notes in October 2023

	- PCA
		- ` pca = PCA(n_components=2).fit(A)` # create PCA instances and fit on data
		- `B = pca.transform(A)` # return the same shape data that the first column is align on the first principal axis, the second column align on the second axis, and so on
		- `new_dataset=pca.fit_transform(dataset)` : another way to create PCA dataset. 
	- Truncated SVD
		- Get a smaller size U Sigma V: `u = u[:, :num_components]; sigma = sigma[:num_components]; vt = vt[:num_components, :]`
		- Combine them back together: `X_reduced = X @ vt.T
	- Cumulative explained variance ratio: `explained_variance_ratio = (sigma**2) / (n-1)`
	- PCA by SVD
		- The principal components are the columns of $V$, corresponding to the largest singular values in $\Sigma$. 
		- Transformation of data:
			- By $B = A \times V^T[:,:k]$ (Lab3 Q->A.ipynb)
			- Here, $B$ is the transformed matrix containing the data points in the reduced $k$ dimensional space. 
	- Support vector classification:
		- `from sklearn.svm import SVC` # classifier took x-y-training set data, and then predict test set data
		- `classifier = SVC().fit(X_train_pca, y_train)`
		- `predictions = classifier.predict(X_test_pca)` # feeding PCA processed data into the classifier
	  - Take a test images and represent it using first r PCA modes"
		  - $\tilde x_{test} = \tilde U \tilde U^* x_{test}$


---
- notes in September 2023

- It is "statistical interpretation" of [[singular value decomposition|SVD]]. It gives us hierarchical coordinate system based on data, to capture the variance of your data. 

- PCA by SVD
	- 1. PCA as a special case of SVD
	- 2. SVD in PCA - The principal components obtained through PCA are equivalent to the right singular vectors of the SVD of the centered data matrix X (after subtracting the mean). These right singular vectors are stored in the V matrix of the SVD decomposition.
	- Variance and Singular Values: The singular values in the Σ matrix of the SVD are directly related to the amount of variance captured by each principal component in PCA. The squared singular values are proportional to the eigenvalues of the covariance matrix of X, which represent the variance along each principal component axis.

- Application:
	-  In PCA, you select a subset of principal components, while in SVD, you use a subset of singular values and associated vectors.
	- SVD can be applied to noise reduction in data by truncating the singular values and reconstructing the data with reduced noise. This is conceptually similar to retaining only the top principal components in PCA.

- SVD provides a mathematical foundation for understanding the relationship between variance and singular values, which are central to PCA's goal of capturing the most important information in the data.

---


- 27-10-2022 01:03: created

- What is principal components analysis?
	- source: https://stats.stackexchange.com/questions/134282/relationship-between-svd-and-pca-how-to-use-svd-to-perform-pca
	- Let real values matrix $X$ be of $n \times p$ size, where $n$ is the number of samples, and $p$ is the number of variables. (Assume $X$ is centered)
	- $p \times p$ covariance matrix $C$ is given by $C = \frac{X^TX}{(n-1)}$. 
		- It is symmetric so it can be diagonalized as $C = VLV^T$, where $V$ is a matrix of eigenvectors and $L$ is a diagonal matrix with eigenvalues $\lambda_i$.
		- The eigenvectors are called principal axes or principal directions of the data. 
		- Projections of the data on the principal axes are called principal components, also known as PC scores

- Application
	- 1. PCA has many applications; we will close our discussion with a few examples. First, [[compress]]ion. Representing $x^{(i)}$’s with lower dimension $y^{(i)}$’s is an obvious application. Such that we can visualize the data. (R1)
	- 2. To preprocess a dataset to reduce its [[dimension|dimensionality]] before running a [[supervised learning]] with $x^{(i)}$’s as inputs.
	- 3. Reduce the complexity of the hypothesis class considered and help avoid overfitting.
	- 4. As a noise reduction algorithm.
		- eg: face images, each point $x^{(i)} \in R^{100 \times 100}$ was a 10000 dimensional vector. 
		- Using PCA, represent each image $x^{(i)}$ with a lower dimensional $y^{(i)}$. 
		- We hope PCA found retain the interesting, systematic variation between faces that capture what a person really looks like, but not the "noise" in the images introduced by minor lighting variations, slightly different imaging conditions etc.
			- Measure distances between face $i$ and $j$ by working in the reduced [[dimensionality|dimension]], compute [[Least mean squares (LMS) algorithm]]. This resulted in a surprisingly good face-matching and retrieval algorithm. 

---
## Reference

1. [[(Course) CS229 Machine learning]]