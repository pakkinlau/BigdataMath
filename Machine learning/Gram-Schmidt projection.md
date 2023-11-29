- Here, we represent [[Unstable Gram-Schmidt process]] again, but this time we are using [[Orthogonal Projector]]/ [[Projection]]
- In the realm of linear algebra, the Unstable Gram-Schmidt process takes a fresh perspective when augmented with the concept of [[Orthogonal Projector]] or [[Projection]]. Consider a matrix $A \in \mathbb{C}^{m \times n}$ with full [[rank]], characterized by its columns $\{ a_j \}$. The [[Unstable Gram-Schmidt process]] process, under this new light, produces a sequence of normalized orthogonal vectors $\{ q_j \}$ where each $q_j$ is a projection of $a_j$.

---
### Definitions and Formulas

From textbook we have the following that discuss Gram-Schmidt projection formula: 

For each step $j$, the process defines $q_j$ as follows:
$$ q_j = \frac{P_j a_j}{||P_j a_j ||},q_j \in \mathbb{C}^j$$
To expand the expression, we have $q_1 = \frac{P_1 a_1}{||P_1 a_1 ||}$, $q_2 = \frac{P_2 a_2}{||P_2 a_2 ||}$, $\dots$, $q_n = \frac{P_n a_n}{||P_n a_n ||}$

- Idea 1: Understanding this formula by breaking details into 2 parts.
	- To make sense of Gram-Schmidt projection formula, we can recognize $P_j a_j$ takes vectors $a_j$ and projects it into a new direction defined by the previous orthogonalized vectors, creating a new collection of orthogonal vectors, say $\{ v_1, v_2, \dots, v_j \}$.
	- So $q_j = \frac{v_j}{||v_j||}$ is an easier way to represent the Gram-Schmidt process, where $v_j$ represents the vectors after projection. 

- Idea 2: Relationship to [[Projection formula]]
	- a. Norm
		- The above expression is related to [[Projection formula]], $\text{proj}_{u_i}(v) = c_i u_i = \frac{v \cdot u_i}{\|u_i\|^2} \cdot u_i$. The norm is raised to the power of 2 because the projection involved finding the components of $v$ in the direction of $u$ that scaling $u$ by that component. 
		- In Gram-Schmidt projection formula, we use [[projector]] to change directions of vectors. The norm is raised to the power of 1. 
		- Both process normalising the vector to ensure the resulting vector are of unit length.  
		- But we can see that Gram-Schmidt projection is simpler in computation. 

- Idea 3: The collection of [[Orthogonal Projector]] $P_j$ 
	- We follow 2 steps to determine $P_j$. 
	- Step 1: Determining $\hat Q_{j-1}$
		- Idea 3a: [[successive spaces]] of new directions $\hat Q_{j-1}$
			- The matrix $P_j$ can be explicitly represented. Let $\hat Q_{j-1}$ denote the $m \times (j - 1)$ matrix containing the first $j - 1$ columns of $\hat Q$, defined as: $$ \hat Q_{j-1} = \begin{bmatrix} q_1, q_2, \dots, q_{j-1} \end{bmatrix}$$
			- This matrix represents the orthonormal basis vectors that have been obtained up to the $(j-1)$-th step in the Gram-Schmidt process. 
			- These vectors are the building blocks for creating the orthonormal basis for the subspace spanned by the input vectors.
	- Step 2: Determining $P_j$: 
		- Then, the projector $P_j$ is given by: $$ P_j = I_{(m \times m)} - \hat Q_{j-1} \hat Q_{j-1}^*$$
			- Idea 3b: Reducing components from $I$:
				- $I$ is the identity matrix. It represents the entire space. 
				- When you subtract something from it, say, $I - M$, you effectively remove the component in the direction of that "something" ($M$). 
			- Idea 3c: Comparing $I - M$ to [[vector decomposition]]
				- This approach parallels the concept from [[vector decomposition]]. In the context of orthogonal decomposition, any vector $v$ can be expressed as a sum of its orthogonal projections onto $\{q_1, q_2, \dots, q_n\}$ as follows: $r = v - (q_1^*v)q_1 - (q_2^*v)q_2 - \dots - (q_n^*v)q_n$
				- In this expression, $r$ is orthogonal to $\{q_1, q_2, \dots, q_n\}$, showcasing the fundamental principle of orthogonality.
			- Idea 3d: $\hat Q_{j-1} \hat Q_{j-1}^*$ is outer product that is performing [[Projection]] 
				- $\hat Q_{j-1} \hat Q_{j-1}^*$ represents the projection onto the subspace spanned by the vectors in $\hat Q_{j-1}$. It does this by taking the outer product of the basis vectors and creating a matrix that represents this projection. The [[projection operator (QQT)]] $\hat Q_{j-1} \hat Q_{j-1}^*$ essentially "projects out" any component of the current vector that lies in the subspace spanned by the vectors in $\hat Q_{j-1}$.
- Idea 4: [[Stability]]
	- We remark that this formula is also not used in practice as it is not [[Stability|stable]].


