
- Subset:
	[[Orthogonal Projector]]
	- Non-orthogonal projectors (oblique projector)
	- Complementary projectors

A **projector** in the realm of **linear algebra** refers to a fundamental concept with wide applications in various fields such as physics, computer graphics, and engineering. In this context, a projector is a linear transformation that maps vectors from a vector space onto a subspace. Understanding projectors is essential in the study of vector spaces and their structural properties.

- Definition:
	- A projector is a [[square matrix]] $P$ that satisfies $P^2 = P$, for $v = Px$ for some $x$. 
		- ($P^2 = P$ is also called "idempotent")
		- In the $v = Px$, $x$ is out input vector, $v$ is our output vector?
- Properties:
	-  1. Idempotent property
	- 2. Image property
		- If $v \in Range(P)$, then $v = Px$, so that $Pv = P(Px) = Px = v$  
			- a. The difference between projection and the vector itself equal to zero. $Pv - v = 0$ This means $Pv - v$ is a zero vector. 
			- b. Mathematically we see the idempotent property. We have $v = Px$. For some $x$ and $Pv = P^2x = Px = v$. 
			- $Pv = v$ only if our data $x$ is already align to the direction of $P$, or, in other words, $x$ already projected into the range subspace of $P$. In that moment, $Pv = v$, and $v$ lies exactly on its own shadow.
	- 3.  Orthogonal projection property
		- For any $v$, we have 
			- types
				- $P(Pv - v) = P^2v - Pv = 0$, so that $Pv - v \in null(P)$
				- $P(v - Pv) = Pv - P^2v = 0$, so that $v-Pv \in null(P)$
			- a. The idempotent property do not holds anymore, so $v \neq Pv$
			- b. $Pv$ is a projection of $v$ onto subspace spanned by columns of $P$. If $v$ is not in the column space / range space of $P$, it turns out giving a zero result. 
				- $P(Pv - v)=0$ that means $Pv - v \in null(P)$
			- c. $Pv - v$ orthogonal to the range of $P$

---
## Discussion

### why $P$ is a square matrix?
- 1. Compatibility of matrix multiplication
	- For a linear transformation $P: V \rightarrow V$, where $V$ is a vector space, the matrix multiplication $Pv$ must be valid for any vector $v \in V$. 
	- To construct projector $P: V \rightarrow V$, we need the column space of $A$ (which represents the range space of $A$) has the same dimension of the row space of $A$ (which represents the domain space of $A$). Therefore, $P$ must be a square matrix. 
	- Having the same dimension in input and output space, it means those two spaces are the same space. 
- 2. Idempotent property:
	- The idempotent property of $P$, $P^2 = P$, is a fundamental characteristic.
	- It means applying the projector twice is the same as applying it once. 
- 3. Eigenvalues and eigenvectors
	- For projectors, eigenvalues play a significant role. Specifically, a projector has eigenvalues 0 and 1, and the corresponding eigenvectors are associated with the subspace it projects onto and the subspace it projects away from, respectively.
	- Eigenvalues and eigenvectors are defined for square matrices. Therefore, to explore the eigenvalues and eigenvectors of a projector, it must be a square matrix.
	- Q1: Why eigenvalues are 0 and 1?
	- Q2: Why we cannot use SVD to study projectors?
		- a. To represent a linear transformation $P: V \rightarrow W$ with non-square matrix, the dimensions of $U$, $S$ and $V^T$ must allow for meaningful matrix multiplication
		- b. Idempotent property $P^2 = P$ in non-square matrix is not always well-defined. Achieving idempotent property is more challenging in non-square matrix.
		- c. Orthogonality: projectors often have orthogonal properties, such as orthogonal projectors having orthogonal image and kernel subspaces. Representing these orthogonal properties using non-square matrices can be mathematically complex and may not preserve the orthogonality relationships. 

##  Image property of projector ($v = Pv$) only holds when the number of application is bigger than 1
- For $n = 2, 3, 4$, and so forth, the equation $Pv = v$ is valid due to the inductive case. However, when $n = 1, Pv = v$ may not hold true because, in this scenario, the data might not align with the direction of $P$."

### Are all projectors deduce dimensionality of the data?
- [[dimensionality reduction]] solely depends on the dimension of [[rank]] of the matrix, so we can check are all projector $P$ having less dimension, having same dimension, or having more dimensions.
- Having more dimension is not possible
	- It is because Projectors are square matrix.
- Having less dimension is possible
	- Because there might be some column vectors in $P$ are null
	- There are infinite possible $P$ that are reducing dimensionality of the data. 
- Having same dimension is possible
	- If that is the case, we can also check how $P$ perform.
	- One of the property is $Pv = v$ for all $x \in \mathbb{R}^m$, which means passing to the projector no matter how many times, the data would still be the same. 
	- Only identity matrix would satisfies such condition. 
	- So when the dimension of $Range(P)$ = the dimension of $Domain(P)$, the only possible projector would be $I$. 

### All projectors $P$ reduce dimension of data except $P = I$. But it seems contradictory to the property of projectors that $Pv = v$, where $v$ seems unchanged in this formula. Can you explain?
- When we have $Pv = v$ as a property of projector, it seems that $v$ remain unchanged before and after applying $v$. 
- How $v$ changes its dimension when it undergoes the effect from $P$ in $Pv = v$. Compare the dimension of $v$ before applying $P$, after applying $P$, applying $P$ n times?
	- Demonstration
		1. Before applying $P$:
		   - The dimension of vector $v$ is the same as its original dimension, denoted as $\text{dim}(v)$.
		2. After applying $P$:
		   - a. some rows of the data would be zeroed out. 
			   - Say the dimension of $domain(P)$ is $n$, dimension of $range(P$) is $n - r$. We are applying data $v$ (dimension of $v$ = $n$) into projector $P$. In that case, $P$ can be represented as $\begin{bmatrix} q_1, q_2, \dots, q_{n - r}, \dots, q_n \end{bmatrix}$. However, in general, we don't know which columns in $P$ is zero columns. The rows of $v$ inspecting to those zero columns in $P$ will be zeroed out after multiplying $P$. So one effect to $v$ from multiplying $P$ is that some rows of its data becomes zero. 
		   - b. the rows of data in $v$ that are not to be zeroed out 
			   - How about other rows of $v$ that are not going to be zeroed out? Would their value become bigger or smaller after multiplying $P$? 
			   - Orthogonal projectors
				   - those rows will be remain unchanged in magnitude. 
			   - Oblique projectors
				   - The rows of $v$ will generally experience a change in magnitude and direction. 
				   - The extent of the change in magnitude and direction depends on how closely the original vector $v$ aligns with the subspace represented by $P$. If $v$ is already closely aligned with this subspace, the change in magnitude will be relatively small. However, if $v$ is almost orthogonal to the subspace, the change in magnitude and direction will be significant.
		   - c. denoting the dimension for the whole process 
			   - we can express the dimension in such linear transformation as $\text{dim}(Pv) = \text{dim}(\text{range}(P))$, where this dimension is typically lower than the original dimension of $v$.
		   - To conclude, when applying an oblique projector $P$ to a vector $v$, the rows of $v$ that are not zeroed out will undergo a transformation to align with the subspace spanned by the columns of $P. This transformation can result in changes in both magnitude and direction, and the extent of these changes depends on the initial orientation of the vector with respect to the subspace.
		3. Applying $P$ repeatedly (n times):
		   - When you apply the projector $P$ to a vector multiple times, the dimension of the result stays the same. Therefore, applying $P$ n times to $v$ does not change the dimension of the result.

## Try to prove when projector $P$ is a full matrix, then $P = I$. 
- I had a discuss on this topic in the MSc classmate group. 

- My comments 
	- 1. $\mathbb{R}^m \mapsto \mathbb{R}^m$ does not implies $Pv = v$. 
	- 2. $Px = x$ is not generally true for all cases. 
		- $Pv = v$ only true when the data $v$ is already in the subspace of the range of $P$. (Which means the number of application of $P$, (name it as $k$) at least applied on data $x$ once, so $k > 1$, then $Pv = v$ holds) But when $k = 1$, $v = Px$ and our data is not necessarily align with the direction of $P$. That is, $x$ might not be in the subspace of the range of $P$. 
	- 3. $Range(P) \in \mathbb{R}^m$ , not $Range(P) = \mathbb{R}^m$

- My take: 
	- Instead, we shall prove it by contradiction. 
		- We set up a base case that is: Say we have projector $P$ is full rank and it is not an identity matrix, then there must exist a vector $v$ such that $Pv \neq v$ . It is obvious because $P$ is not identity matrix so this holds. (Remark, $Pv \neq v$ does not contradict to any definition of projectors)
		- However, when we multiply $P$ on both sides, we have $P^2v \neq Pv$. Now we can see it contradicts the definition of $P$. 
	- Therefore, $P$ must be an identity matrix. 

### Try to show that when passing data $v$ into oblique projectors $P$, those rows of $v$ that are not zeroed out will in general experience change in magnitude and direction

If $v$ is entirely within the subspace of range(P), it means v is aligned with the range(P). So the direction and magnitude of v would change. I am not trying to proof this.

Here we are concerning If $v$ is not aligned to the range of $P$. 

An oblique projector can be defined as follows:$$P = \frac{vv^T}{v^Tv}$$
Where:
- $P$ is the oblique projector matrix.
- $v$ is a nonzero vector.

Now, let's consider the effect of applying this projector to a vector $x$. The projection of $x$ onto the subspace defined by $v$ can be computed as follows:$$Px = \frac{vv^Tx}{v^Tv} = \frac{v(v^Tx)}{v^Tv}$$
- Remark: We can obtain this expression easily. Check chapter 4 of Gilbert Strang's book to know more. 

To analyze how this projection affects the magnitude and direction of the components of $x$, we can break it down into two parts: the magnitude and the direction.

1. **Magnitude Change:**
   - The magnitude of the projection of $x$ onto $v$ is given by:$$|Px| = \frac{|v^Tx|}{\|v\|}$$
   - Remark: how can we obtain this expression?

   - The magnitude change is proportional to the absolute value of the dot product between $x$ and $v$.
   - If $x$ and $v$ are orthogonal (i.e., $x^Tv = 0$), then the magnitude of the projection does not change.
   - If $x$ and $v$ are not orthogonal, the magnitude of the projection is scaled by the cosine of the angle between them, leading to a change in magnitude.

2. **Direction Change:**
   - The direction of the projection is given by the unit vector in the direction of $v$:$$\hat{v} = \frac{v}{\|v\|}$$
   - Remark: how can we obtain this expression?

   - The direction change can be significant when $x$ is not parallel to $v$. In this case, the projection changes the direction of the original vector $x$ to align it with $v$.


---
- Complementary projectors
	- $I - P$ is called the complementary projector to $P$. 
	- Properties:
		- 0. Projectors defined as any square matrix that satisfies $P^2 = P$ 
			- 0a. If $v \in Range(P)$, then $v = Px$, so that $Pv = P(Px) = Px = v$  
			- 0b. $P(Pv - v) = P^2v - Pv = 0$, so that $Pv - v \in null(P)$
		- 1. If $P$ is a projector, $I - P$ is also a projector
			- $(I - P)^2 = I - 2P + P^2 = I - 2P + P = I - P$
		- 2. $range(I - P) = null(P)$
			- This property discusses the range of $I - P$ is equal to the null space of $P$, denoted as $null(P)$. 
			- a. $range(I - P) \supseteq null(P)$. 
				- If $v \in null(P)$, then $Pv = 0$. rearrange it, it becomes $(I - P)v = v$, so $v \in range(I - P)$
			- b. $range(I - P) \subseteq null(P)$
				- If $v \in range(I-P)$, then $v = (I - P)x$. Multiplying $P$ on both sides, we have  $Pv = P(I-P)x = Px - P^2x = 0$, which implies $v \in null(P)$. 
				- Another interpretation (wrong!): 
					- a. $range(I - P) \supseteq null(P)$. 
						- This states that the range of the complementary projector $I-P$ contains the nullspace of $P$. In other words, $\{ v: Pv = 0 \}$ will belong to the range of $I - P$. 
						- This is because when you apply $(I-P)$ to $v$, $(I-P)v = v - Pv = v$, which implies $v$ is in the range of $I - P$. 
					- b. $range(I - P) \subseteq null(P)$
						- This states that the range of complementary projector $I - P$ is the subset of the null space of $P$. 
						- It means $\{ u: range(I - P)\}$ satisfies $(I - P)u = 0$, which implies $u = Pu$. Hence, $u$ is in the null space of $P$. 
							- Demonstration:
								- Let $u$ be vector in the range of $I - P$, which means there exists a vector $v$ such that $(I - P)v = u$. We want to show that $(I - P)u = 0$
								- Multiplying $(1-P)$ on $(1-P)v = u$ to obtain $(I - P)u$, we have $(I-P)(I-P)v = (I-P)u$. 
								- $\Rightarrow (1-P)u = (1-P)v$  (by the property of complement projector)
								- With $(1-P)u = (1-P)v$, we know for any vector $u$ in the range of $I - P$, there exists a vector $v$ such that $(I - P)v = u$. Therefore, $(I - P)u = 0$ for any vector $u$ in the range of $I - P$. 
			- c. Combining a and b, we have got $range(I - P) = null(P)$
		- 3. By writing $P = I - (I - P)$, we derive the complementary fact: $null(I - P) = range(P)$
			- That is the opposite direction of property 2. 
		- 4. $range(P) \cap null(P) = \{0\}$
			- We see $null(I - P) \cap null(P) = \{ 0 \}$. 
			- Any vector $v$ in both sets (that is, ($I - P$) and $P$), satisfies 
			- $v = v - Pv$ (because $v \in null(P)$)
			- $\Rightarrow  v = (I - P)v$. 
			- $\Rightarrow v = 0$ (because $v \in range(P) = null(I-P)$
			- So another way of stating this fact is: $range(P) \cap null(P) = \{0\}$
		- 5. These computations show that a projector separates $\mathbb{C}^m$ into two spaces. 
			- Let $S_1$ and $S_2$ be two subspace of $\mathbb{C}^m$ such that $S_1 \cap S_2 = \{ 0 \}$ and $S_1 + S_2 = \mathbb{C}^m$, where $S_1 + S_2$ denotes the span of $S_1$ and $S_2$, that is the set of vectors $s_1 + s_2$ with $s_1 \in S_1$ and $s_2 \in S_2$. Then there is a projector $P$ such that $range(P) = S_1$ and $null(P) =S_2$. We say that $P$ is the projector onto $S_1$ along $S_2$. 
	- Are more details, skip for now.

---
[[Orthogonal Projector]]



---

**Key Points:**

**1. [[Linear transformation]]:**
   - A projector is a linear transformation $P: V \rightarrow V$, where $V$ is a vector space.
   - It satisfies two essential properties:
     - **Idempotent**: Applying the projector twice yields the same result as applying it once, i.e., $P^2 = P$.
     - **Linearity**: For any vectors $u$ and $v$ in the vector space $V$ and scalar $c$, $P(cu + v) = cPu + Pv$.

**2. [[column space|image]] and [[Kernel space]]:**
   - The **image** of the projector, denoted as $Im(P)$, is the subspace of $V$ onto which $P$ projects vectors.
   - The **kernel** of the projector, denoted as $Ker(P)$, is the subspace of vectors that are mapped to the zero vector by $P$.

**3. Orthogonal Projectors:**
   - A projector is called **orthogonal** if its image and kernel are orthogonal subspaces, meaning that every vector in the image space is orthogonal to every vector in the kernel.

**4. Applications:**
   - **Least Squares Problems**: Projectors are used in solving least squares problems, where the goal is to minimize the squared differences between observed and predicted values.
   - **Computer Graphics**: Projectors are employed in computer graphics for rendering and shadow calculations.
   - **Signal Processing**: In signal processing, projectors are used for noise reduction and feature extraction.

**5. Eigenvectors and Eigenvalues:**
   - Projectors have a clear connection with eigenvectors and eigenvalues. The eigenvectors corresponding to eigenvalue 1 are precisely the vectors in the image of the projector.

**6. Projection Matrix:**
   - Every projector can be represented by a **projection matrix**. For an $n \times n$ projector $P$, its projection matrix is symmetric and idempotent ($P^2 = P$).
