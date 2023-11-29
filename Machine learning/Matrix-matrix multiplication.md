
- Definition:
	- The process of multiplying an $m \times n$ matrix $A$, by an $n \times p$ matrix $C$, resulting a $m \times p$ matrix $B$. 
- Notation:
	- It is often represented using the [[dot product]] symbol ($\cdot$), or simply placing matrices adjacent to each other. 
	- $B = A \cdot C$ , or $B = AC$. 
- Dimension:
	- To ensure that the number of column of $A$ is equal to the number of rows of $C$. 
	- If we express their dimension, that would be: $(m \times n) (n \times p)$
		- The number of the inner part should be matched 
- Computation:
	- Take the [[dot product]] of the first row of $A$ and the second column of $C$ to get `B[1][2]`.
	- Continue the process for all elements of C. 
	- $b_{ij} = \sum_{k=1}^m a_{ik}c_{kj}$ , for $1 \leq i \leq l$, $1 \leq j \leq n$. 
		- Here, $a_{ik}$ represents the element in the i-th row and k-th column of matrix $A$. 
 - Geometric interpretation:
	 - $b_1$ (each column of $B$), is the [[linear combination]] of $A$, with the coefficients given by the column $c_1$ 
	 - how does changing c affect the result B in practical terms?
		 - Scaling:
			 - If you scale matrix $C$, it will scale the corresponding columns of matrix B. For example, if you double all the elements in C, each column of B will also be doubled.
			 - Say $c'_{ij}$ = $2 \cdot c_{ij}$, the resulting matrix $B$ would be doubled. 
		 - Rotation:
			 - Changing values of $C$ also could lead to how each columns of $A$ contributes to each column of $B$. This can be thought of as a rotation or reorientation of the original data in A. Different values in C will lead to different linear combinations of the columns of A, affecting the direction and magnitude of each column in B.
			 - Types of matrix:
				 - Identity matrix: no rotation
				 - non-identity matrix: rotation
				 - [[orthogonal]] matrix: orthogonal transformation
					 - If C is an orthogonal matrix, it represents a special kind of rotation that preserves distances and angles between vectors. This is commonly used in applications like principal component analysis (PCA) for dimensionality reduction.
		 - [[Linear transformation]]
		 - [[Matrix inversion]]

- L row & R column --> element-wise multiplication --> n^2 elements --> old method
	- [[row picture]]
- L column & R row -->a summation of column vectors:
	- $BC = c_1(column\ 1) + c_2(column\ 2) + \dots + c_n(column\ n)$, which $c_k$ could be row vectors. 
	- [[column picture]]
- "New way" of multiplying matrices
![[Pasted image 20230913030338.png]]
![[Pasted image 20230912000607.png]]


- Applications:
	- Linear transformation
	- Solving linear systems
	- Computer graphics
	- Data analytics
