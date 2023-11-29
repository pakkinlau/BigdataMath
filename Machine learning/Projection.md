- subset:
	- orthogonal projection

Projections are a fundamental concept in linear algebra that plays a crucial role in various mathematical and practical applications. 
- The projection of a vector onto an orthogonal subspace is mathematically well-defined and relatively easy to compute.

Projection vector

- Projection is an action to reduce dimension of the problem.
- The key to projection is orthogonality. 
- Projection vector $p = Pb$, project to a subspace.  
	- $b$ is the vector we are going to project. 
	- $p$ is the resultant vector we want to have. 
	- $P$ is a $m \times n$ projection matrix that projects that group of vectors into the subspace we want. 
	- $a \in  W$  $a$ is the reference point we have for the space $W \in R^m$. 
- Applications:
	- Say we have a plane, and a line that is not in the plane. 
	- We are looking for a nice formula to project the vector into the plane.


- [[Projection formula]]


---

They are primarily used to understand how vectors can be broken down into [[component]]s along a specific direction or onto a particular subspace within a vector space. Here, we'll delve into the key aspects of projections in the context of linear algebra.

1. **Definition of Projection**:
   - In linear algebra, a projection is a [[linear transformation]] that maps a [[vector|vector]] onto a [[subspace]]. It essentially represents the closest approximation of a vector onto that subspace.

3. **Orthogonality between Projection vector and Shadow of Components**:
   - When a vector is projected onto a subspace, it can be split into two components: the component that lies within the subspace (the shadow) and the component that is orthogonal to the subspace.
   - This decomposition is useful for various applications, such as solving linear systems, least squares problems, and understanding geometric relationships.
   - The key characteristic of an orthogonal projection is that the projection vector is orthogonal (perpendicular) to the subspace onto which it is projected. This means the dot product of the projection vector and any vector in the subspace is zero.
   - Mathematically, if v is the original vector, and u is the projection of v onto a subspace S, then (v - u) is orthogonal to S.
---

2. **Orthogonal Projections / Orthogonal decomposition**:
   - One of the most common types of projections is orthogonal projection. In this case, the subspace onto which the vector is projected is orthogonal (perpendicular) to the subspace from which the vector originates.



- relationships between orthogonality and projection
	- projection is like orthogonal decomposition 
	- projection is like "extracting what is relevant of some vectors to some spaces". By relevant, we mean the parts that is orthogonal to that space is not relevant to that space. 




3. **Applications**:
   - Orthogonal projections have numerous practical applications. They are used in computer graphics to simulate shadows and reflections, in statistics for regression analysis, and in engineering for signal processing.
   - They are also fundamental in solving linear systems and finding the least squares solutions.

4. **Orthogonal Complement**:
   - The orthogonal complement of a subspace S, denoted as S⊥, consists of all vectors that are orthogonal to every vector in S. It is a subspace itself and is often used in solving problems involving orthogonal projections.

5. **Orthogonal Projection Theorem**:
   - This theorem states that for any vector v and subspace S, there exists a unique vector in S that is the orthogonal projection of v onto S.

In summary, orthogonal projections in linear algebra are a powerful tool for understanding vector spaces and decomposing vectors into components. They are essential in various mathematical and practical applications, providing a deeper insight into the geometry and structure of vector spaces.

---

4. **Applications**:
   - Projections are used in a wide range of fields, including physics, computer graphics, engineering, and statistics.
   - In physics, projections are used to calculate the work done by a force in a specific direction or to find the component of a vector responsible for a particular effect.
   - In computer graphics, projections are crucial for rendering 3D scenes onto 2D screens, creating realistic shadows and reflections.
   - In statistics, projections are used in techniques like [[principal component analysis]] (PCA) for [[dimensionality reduction]].

5. **Matrix Representation**:
   - Projections can be represented by matrices, known as projection matrices. These matrices are often [[Orthogonal vector|orthogonal]] if the projection is orthogonal.
   - The projection matrix allows for efficient computation of projections, making it a valuable tool in numerical calculations.

6. **Properties of Projections**:
   - Projections satisfy a number of important properties, including idempotence (a vector projected twice remains the same), commutativity, and linearity.

---
### Old notes

- If $b$ is projected onto a line, its projection $p$ is the part of $b$ along that line.
- If $b$ is projected onto a plane, $p$ is the part in that plane. The projection $p = Pb$. 
- The key to projection is orthogonality -- the line from b to p is perpendicular to the vector a. 

---
### Projection matrix
- A projection matrix $P$ is an $n \times n$ square matrix that gives a vector space projection from $R^n$ to a subspace $W \in R^m$. 
- The projection of $b$ is $Pb$. 
- It looks like identity matrix, but only the dimension we want to preserve has value 1 in that corresponding row. 
- The functionality of projection matrix is, reducing certain dimensions / vector to zero. 
- Properties:
	- 1. The columns of $P$ are the projections of the standard basis vectors, and $W$ is the image of $P$.  
	- 2. They are square matrix
	- 3. Same as identity matrix, they are symmetric matrices with $P^2 = P$
	- 4. A projection is orthogonal iff $P = P*$, where $P*$ denotes the adjoint matrix of $P$. 
	- 5. $\langle v, Pw \rangle = \langle v_w,Pw\rangle = \langle Pv,w\rangle$
		- Proof:
			- 1. $v = v_W + v_{W^{\perp}}$
	- 6. If 2 projection matrix produces the lines or planes that are orthogonal complements to each others (that means the sum of the dimension of the products from those projection matrix is equal to n), then $P_1 + P_2 = I$, $p_1 + p_2 = b$. 
	- 7. Every subspace of $R^m$ has its own $m \times m$ projection matrix. 
- Examples:
	- $P = \begin{bmatrix} 0&1\\0&1 \end{bmatrix}$, which projects onto the line $y=x$. 
	- $P_1 = \begin{bmatrix} 0&0&0 \\ 0&0&0 \\ 0&0&1 \end{bmatrix}$ (Onto the z axis)
	- $P_2 = \begin{bmatrix} 1&0&0 \\ 0&1&0 \\ 0&0&0 \end{bmatrix}$ (Onto the xy plane)


---

### Performing projection (Projecting)
- say a, b are the directions.
- p is the projection vector (b onto a). Its length is related to b, and its direction is related to a.
![[Pasted image 20230107192920.png|600]]

### Projecting into a line
- The projection of a vector $b$ onto the line through $a$ is the closest point $p = \hat x a =a(a^Tb / a^Ta)$, which $\hat x$ is the ratio of length b to a, with respect to the angle between a and b. 
- Error vector
	- The error $e = b -  p$ is perpendicular to $a$: Right triangle $b\ p\ e$ has $||p||^2$ + $||e||^2$ = $||b||^2$

![[Pasted image 20230107204435.png]]

- $\hat x$ is not a vector. 
	- Attempt 1: 
		- At first we don't know $\hat x$ is whether a scalar or a vector, we have the formula by vector addition $e = b - \hat x a$ , and $a \cdot b - \hat x a \cdot a = 0$.
		- By looking at the output of $a \hat x$, it produces a vector.
		- Vector multiplication always produces a scalar. 
	- Attempt 2:
		- We don't know which 

### Projecting a full dimensional point into a subspace (dim = n)
![[Pasted image 20230113214642.png]]
-  $p = A  \hat x$