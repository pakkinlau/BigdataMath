---
date created: Monday, September 26th 2022, 6:21:00 am
date modified: Thursday, October 27th 2022, 3:37:38 am
---
- 26-9-2022: created

- superset:
	- [[Embedding]]

- subset:
	- [[Global matrix factorization methods

- related:
	- [[singular value decomposition]]

- What is it?
	- This should be explained in various ways. One is in linear algebra. One is in machine learning. 
- MF in linear algebra
	- Gaussian elimination factors A into $LU$. 
- MF in machine learning
	- MF is a simple embedding model. Given the feedback matrix $A \in R^{m \times n}$, where $m$ is the number of users (or queries), and $n$ is the number of items, the model learns: (R4)
		- A user embedding matrix $U \in R^{m \times d}$, where row $i$ is the embedding for user $i$.
		- An item embedding matrix $V \in R^{n \times d}$, where row $j$ is the embedding for item $j$. 
	- MF is a class of [[collaborative filtering]] algorithm used in [[recommender system]].
	- MF is a kind of [[Unsupervised learning|unsupervised]] [[feature learning]] that generate [[shallow]] [[Embedding]].
	- These methods utilizes low-rank approximations to decompose large matrices that capture statistical information about a corpus. (R2)
	- [[Random walk]], matrix factorization, and [[node embedding]]s are closely related. (R1)
	- This family of method became popular during the Netflix prize challenge due to its effectiveness as reported by Simon Funk in 2006.
	- The prediction results can be improved by assigning different regularization weights to the [[latent]] factors based on items' popularity and users' activeness.
- How it works?
	- Decomposing the user-item interaction matrix into the product of two lower [[dimensionality]] rectangular matrices.
	- The technique is to represent users and items in a lower dimensional [[latent]] space.
- Objective function: (R4)
	- The embeddings are learned such that $UV^T$ is a good approximation of the feedback matrix $A$. 
	- $$\underset{U \in R^{m \times d}, V \in R^{n \times d}}{min} \sum_{(i,j) \in obs}(A_{ij} - \langle U_i,V_j \rangle)^2$$
	- where A is the feedback matrix $A \in R^{m \times n}$, where $m$ is the number of users (or queries), $n$ is the number of items.
	- where $U \in R^{m \times d}$ is the user embedding matrix, $i$ is in the range of $m$
	- where $V \in R^{n \times d}$ is the item embedding matrix, $j$ is in the range of $n$
- Algorithms
	- Stochastic gradient descent
	- Weighted alternating least squares
- Funk MF
	- The predicted rating is computed as $R=HW$, where $R \in R^{users \times iterms}$ is the user-item rating matrix, $H \in R^{users \times latent\ factors}$ contains the user's latent factors and $W \in R^{latent\ factors \times items}$ is the item's latent factors.
	- Specifically, the predicted rating user $u$ will give to item $i$ is computed as: $$r_{ui} = \sum_{f=0}^{nfactors}H_{u,f}W_{f,i}$$
---

# Applications

- Applied:
	- [[Page rank algorithm]] (how?)
	- Obtain node embeddings via matrix factorization
	- Collaborative filtering algorithm used in recommender systems.

- Node embeddings
	- For an edge, [[node similarity]] $z_v^Tz_u=A_{u,v}$. Which is the $(u,v)$ entry of the graph.
	- Exact factorization $A=Z^TZ$ is generally not possible.
	- Learn $Z$ approximately by $\underset{Z}{min} ||A-Z^TZ||_2$ (R1)
		- We optimize $Z$ such that it minimizes the L2 norm ([[Frobenius Norm]]) of $A-Z^TZ$.
	- Conclusion: [[dot product]] [[Decoder]] with [[node similarity]] defined by edge connectivity is equivalent to matrix factorization of $A$.

- [[collaborative filtering]] (R3)
	- Given a feedback matrix $A \in R^{m \times n}$, where $m$ is the number of users (or queries), and $n$ is the number of items, the model learns:
		- A user embedding $U \in R^{m \times d}$, where rows $i$ is the embedding for user $i$.
		- An item embedding $V \in R^{n \times d}$, where rows $j$ is the embedding for user $j$.
		- These embeddings are learned such that the product $UV^T% is a good approximation of the feedback matrix $A$. Observe that $(i,j)$ entry of $U.V^T$ is simply the dot product $\langle U_i, V_j \rangle$ of the embeddings of user $i$ and item $j$.
	- Objective function:
		- $$\underset{U \in R^{m \times d}, V \in R^{n \times d}}{min} \sum_{(i,j) \in \text{obs}} (A_{ij} - \langle U_i, V_j \rangle)^2$$


---

# Reference

- [[(Course) CS224W - Machine learning with graphs (stanford)]]
- [[(Paper) Pennington, J., Socher, R., & Manning, C. (2014). GloVe Global Vectors for Word Representation]]
- [[(Course) google developers - machine learning courses]]
- Google developer notes: https://developers.google.com/machine-learning/recommendation/collaborative/matrix
