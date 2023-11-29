13/11/2023

Related: [[Data fitting]], [[Least Squares]]

In linear algebra, the residual vector and error are fundamental concepts that play a crucial role in understanding the accuracy and precision of mathematical models, particularly in the context of solving linear systems of equations.

Residual vector always orthogonal to the range of $A$, which implies $r$ lies in the nullspace of $A^*$. 

In [[Data fitting]], [[Least Squares]], residual vector is applied as follow: 
- Given $A \in \mathbb{C}^{m \times n}$, $m \geq n$, $b \in \mathbb{C}^m$, find $x \in \mathbb{C}^n$ such that $|| b - Ax||_2$ is minimized. 

1. **Residual Vector:**
   - The residual vector is a vector that represents the difference between the observed values and the values predicted by a model. 
   - In the context of linear algebra, consider a system of linear equations $Ax = b$, where $A$ is a matrix, $x$ is a vector of unknowns, and $b$ is a vector of constants. The residual vector, denoted as $r$, is given by $r = b - Ax \in \mathbb{C}^m$.
   - Geometrically, the residual vector points from the predicted point (the point on the hyperplane determined by $Ax$) to the actual observed point $b$.

2. **Error:**
   - The error in the context of linear algebra refers to the discrepancy between the predicted values and the actual observed values. It is often quantified by the norm of the residual vector.
   - The error ($e$) can be expressed as the norm (magnitude) of the residual vector: $e = \|r\|$, where $\|\cdot\|$ denotes the norm.
   - Minimizing the error is a key objective in various applications, as it signifies achieving a solution that is close to the observed data.

3. **Minimizing Error and Solving Systems:**
   - In solving linear systems of equations, the goal is often to find a solution $x$ that minimizes the error or the norm of the residual vector.
   - The least squares method is a common approach to minimize the error. It seeks to find the values of $x$ that minimize the sum of the squared magnitudes of the residuals.

---
## Theorem: Deriving normal equation

Figure:
![[Pasted image 20231126210011.png|300]]

- Let $A \in \mathbb{C}^{m \times n}$, and $b \in \mathbb{C}^m$. A vector $x \in \mathbb{C}^n$ minimizes the residual $||r||_2 = ||b - Ax||_2$ if and only if $r \perp range(A)$, that is $A^*r = 0$.  
- (If r is not orthogonal to $Range(A)$, then $r'$ would be longer than $r$. )

- There are 3 equivalent expressions 
	- $A^* r = 0$ 
	- $A^* Ax = A^*b$ 
	- $Pb = Ax$, where $P \in \mathbb{C}^{m \times m}$ is the [[Orthogonal Projector]] onto $range(A)$.
- The equivalence of expression 1 and 3 derives from the properties of [[Orthogonal Projector]].
	- We can use [[Rank-Nullity Theorem|Dimension theorem]] to derive this.
	- If $r$ is in the null space of $A^*$, then $r$ is in the range of $P$ (the orthogonal projector onto the range of $A$). Thus $Pb = Ax$. 
- And the equivalence of expression 1 and 2 derives from the definition or $r$. 
	- Showing this is true simply by substituting $r = b - Ax$. 

---
Solve for $x$
- Say $A^* Ax = A^*b$, then $x = (A^*A)^{-1}A^*b$  

Uniqueness of solution $x$
- If $A$ is full rank if and only if the solution $x$ is unique. 


---

4. **Applications:**
   - Residual vectors and errors are prevalent in various fields, including statistics, machine learning, and engineering.
   - In regression analysis, for example, minimizing the error is equivalent to finding the best-fitting line to a set of data points.
   - In numerical methods, understanding and managing errors are crucial for ensuring the stability and accuracy of algorithms.

Understanding the concepts of residual vectors and errors in linear algebra provides a foundation for evaluating the performance and accuracy of models, making informed decisions in data analysis, and improving the reliability of computational methods.