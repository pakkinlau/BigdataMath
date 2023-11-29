
- Definition:
	- The process of multiplying an $m \times n$ matrix $A$, by an n-dimensional column vector $x$, resulting a n-dimensional column vector $b$. 
- [[Dimension]] compatibility:
	- To ensure that the number of column of $A$ is equal to the number of rows of $b$. 
	- If we express their dimension, that would be: $(m \times n) (n \times 1)$
		- The number of the inner part should be matched 
- Computation:
	- Each element $b_i$ is obtained by taking the [[dot product]] of the $i^{th}$ row of the matrix $A$ and vector $x$. 
	- $b_i = \sum_{j=1}^n (a_{ij} \times x_j)$
		- Here, $a_{ij}$ represents the element in the i-th row and j-th column of matrix $A$. 
- Geometric interpretation:
	- $b$ is a [[linear combination]] of the columns of $A$, where $x$ is taking part as varying parts of the combination. 
	- how does changing **x** affect the result **b** in practical terms?
		- [[Linear transformation]]:
			- when you change vector x, you are essentially specifying how much of each transformation component you want to apply.
		- Weighting of components:
			- Changing the values in x effectively changes the weighting or contribution of each component of the transformation. 
		- Interactive applications:
			- In interactive applications, such as computer games or simulations, changing x can be controlled by user input.
		- Data analysis:
			- In data analytics and machine learning, x might represent coefficients or weights applied to input features. Changing x can have a profound impact on the outcome of the analysis or the performance of a model. 
			- In [[linear regression]], each element of x corresponds to the weight of a feature, and changing these weights affects the prediction made by the model.
			- In image processing, x can represent filter values used for convolution operations, altering the image's appearance.

- [[row picture]]
- 

- [[column picture]]
![[Pasted image 20230909231113.png]]

- Applications:
	- Linear transformation
	- Solving linear systems
	- Computer graphics
	- Data analytics
