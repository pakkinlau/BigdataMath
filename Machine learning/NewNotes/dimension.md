---
alias: dimensionality
---

 - Related: [[topological method]]

- subset:
	- High-dimension
	- Low-dimension


---
- In linear algebra:
	- The [[column space]] $C(A)$ and the [[row space]] $C(A^T)$ both have dimension $r$ (the [[rank]] of $A$)
	- The [[nullspace]] $N(A)$ the dimension $n-r$. The nullspace $N(A^T)$ has dimension $m -r$ 
	- [[backward elimination]] produces bases for the row space and nullspace of $A$: they are the same as for $R$. 
---


- What are dimensionality?
	- The number of input variables or features for a dataset is referred as its dimensionality (R1)

- Example:
	- One-hot vector: 
		- $R^{|V| \times 1}$ dimension, V is the size of our vocabulary. Each word as a completely independent entity. If we merge all one-hot vector into a table, it is just a diagonal matrix. 
	- [[SVD]] based vector: 
		- $R^{|V| \times M}$ . The vector scales with the number of documents M. If we have more information about the similarity of documents (eg: similar topic documents), more words appears more often, thus we can come up with information by such statistics. 
		- Word-document matrix
		- Window-based co-occurrence matrix
	- Input and output data dimension for $m \times n$ sized matrix $A$
		- In transformation problem, we have $Ax = b$. 
		- Input data:
			- $A$ receives input data from its domain space. To make the multiplication works, the data has a dimension of $m$ because the row space is spanned by the [[linear combination]] of  independent rows in $A$. 
			- The dimension for the row space of $A$ though is $min(r,m)$ because there might be some zero rows within $A$ that reduces the dimension of $A$. 
			- So we have $dim(Domain(A)) = dim(C(A^T)) = m$. 
		- Output data: 
			- Similarly, the dimension of output data follows the column space of $A$ (without considering whether $A$ is a full rank matrix.)
			- So we have $dim(Range(A)) = dim(C(A)) = n$

- Application
	- Data visualization
		- : High-dimensionality statistics and [[dimensionality reduction]] techniques are often used for data visualization. 
	- [[classification]]
		- Nevertheless these techniques can be used in applied machine learning to simplify a [[classification]] or [[regression]] dataset in order to better fit a predictive model. (R1)

- Curse of dimensionality (wiki) ^eae603
	-  The common theme of these problems is that when the dimensionality increases, the volume of the space increases so fast that the available data become [[sparse]].
		- In order to obtain a reliable result, the amount of data needed often grows exponentially with the dimensionality. 
		- Also, organizing and searching data often relies on detecting areas where objects form groups with similar properties; in high dimensional data, however, all objects appear to be sparse and dissimilar in many ways, which prevents common data organization strategies from being efficient.
	- However, all objects appear to be sparse and dissimilar in many ways, which prevents common data organization strategies from being efficient.
	- Q: How word vector having 100+ dimension, and works normally?

- Typical Dimensions for [[tasks]]
	- images CNNs: 
		- [[AlexNet]] (2012): total number of parameters 61 millions. With [[Pruning]] -- 6.7 million. With no decrease in classification accuracy. 
![[Pasted image 20221027014816.png]]
- Fig: A demonstration of calculating dimensions for a neural network. (R2)

- Solutions:
	- [[dimensionality reduction]]

- Domains: (wiki)
	- combinatorial explosion
		- In some problems, each variable can take one of several discrete values, or the range of possible values is divided to give a finite number of possibilities. Taking the variables together, a huge number of combinations of values must be considered. 
		- even in binary variables, the number of possible combinations already $2^d$, exponentially in the dimensionality.
		- Naively, each additional dimension doubles the effort needed to try all combinations. 
	- Sampling
		- There is an exponential increase in volume associated with adding extra dimensions to a  [[General space|mathematical space]].
		- 2D: Requires $10^2$ evenly spaced sample points suffice to sample a unit interval (a "1-dimensional cube") with no more than 10−2 = 0.01 distance between points. 
		- 10D: Requires $10^{20}$ sample points, 
		- In general the volume difference is ${(10^n)}^{10}$ / $(10^n)$ larger.
	- Optimization
		- When solving dynamic optimization problems, the objective function must be computed for each combination of values. This is a significant obstacle when the dimension of the "state variable" is large. 
	- Machine learning
		- Involving learning a "state-of-nature" from a finite number of data samples in a high-dimensional feature space with each feature having a range of possible values, typically an enormous amount of training data is required to ensure that there are several samples with each combination of values.
		- Peaking phenomenon / Hughes phenomenon:
			- With a fixed number of training examples, the average predictive power of a classifier or regressor first increases as the number of dimensions or features used is increased, but beyond a certain dimensionality it starts deteriorating instead of improving steadily.
			- In the context of simple [[classifier]]



---
## Reference
1. Brownlee's blog: https://machinelearningmastery.com/dimensionality-reduction-for-machine-learning/
2. learnopencv's blog: https://learnopencv.com/number-of-parameters-and-tensor-sizes-in-convolutional-neural-network/#:~:text=In%20a%20CNN%2C%20each%20layer,of%20parameters%20%3A%20weights%20and%20biases.