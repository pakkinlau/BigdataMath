---
alias: Pseudo-inverse
---

- To-do list (not completed)
	- Watch lecture 33 (Left inverse, right inverse, pseudo-inverse)
	- https://www.youtube.com/watch?v=Go2aLo7ZOlU&list=PL221E2BBF13BECF6C&index=69

If $A$ has full rank, then the solution $x$ to the least squares problem is $x = (A^*A)^{-1}A^*b$. We call the matrix $A^+ = (A^*A)^{-1}A^*$ the pseudoinverse of the matrix $A$. 
- The derivation of this expression ($x = (A^*A)^{-1}A^*b$) please refer to [[Normal equation]]

**Introduction:**
- Used to deal with matrices that may not have a traditional inverse. 
- While regular matrix inverses exist for [[square matrix]], non-[[singular]] matrices, pseudo-inverses extend this idea to rectangular and [[singular matrix]] matrices, providing a way to approximate solutions in various applications, including solving linear systems, least squares problems, and data analysis.

Theoretical background:
- 1. Inverse function:
	- Say there are non-square matrix $A$ and a linear transformation $Ax = y$. We can see the transformation $A$ is actually one-to-one (i.e. if we have different $x_1$, $x_2$, it gives us different $Ax_1 \in range(A)$, $Ax_2 \in range(A)$). 
	- SO we can establish a inverse relationship for this:
		- $y = A^+(Ay)$
			- where $Ay$ is the data point we had in the range space when putting $y$ as the input.
			- We establish a pseudo-inverse $A^+$ to transform the collections of data from $range(A)$ back to $A$ 
- 2. Dimensions
	- When we talk about linear transform from matrix $A: \mathbb{C}^m \rightarrow \mathbb{C}^n$, we are actually taking care of $A: \mathbb{C}^r \rightarrow \mathbb{C}^r$. 

- Formulation:
	- $A^+ = V\Sigma^+U^T$ brings $Ax$ in the column space back to $x$ in the row space. 

**Properties of a Pseudo-Inverse:**

1. **Generalized Inverse:** The pseudo-inverse is a generalization of the matrix inverse. While a regular matrix inverse exists for square, non-singular matrices, the pseudo-inverse can be calculated for any matrix, whether it is square or not, and regardless of its rank.

2. **Not Necessarily Unique:** Unlike the standard matrix inverse, a matrix can have multiple pseudo-inverses. However, all pseudo-inverses share certain key properties.

3. [[Least Squares]]Solutions: One of the most common uses of the pseudo-inverse is in solving [[over-determined|overdetermined]] linear systems, where the number of equations exceeds the number of unknowns. The pseudo-inverse provides a solution that minimizes the sum of squared errors, making it useful in applications like linear regression.

4. **Moore-Penrose Conditions:** The four Moore-Penrose conditions define the properties of a valid pseudo-inverse:
   - **Left Inverse:** A valid pseudo-inverse A⁺ should satisfy A⁺A = I, where A represents the original matrix, and I is the identity matrix.
   - **Right Inverse:** A⁺A = I, where A⁺ represents the pseudo-inverse.
   - **Left Semi-Inverse:** AA⁺A = A, where A⁺ represents the pseudo-inverse.
   - **Right Semi-Inverse:** A⁺AA⁺ = A⁺, where A⁺ represents the pseudo-inverse.

**Calculating the Pseudo-Inverse:**
There are various methods to calculate the pseudo-inverse depending on the context and computational resources available. Some common techniques include the Singular Value Decomposition (SVD) method and the Moore-Penrose formula. The SVD method is widely used and is computationally efficient for both small and large matrices.

**Applications:**
The concept of a pseudo-inverse finds applications in diverse fields:
1. **Linear Regression:** It is used to find the best-fitting line or plane when solving over-determined linear systems.
2. **Data Compression:** In Principal Component Analysis (PCA), the pseudo-inverse helps reduce the dimensionality of data while preserving important information.
3. **Image Processing:** Pseudo-inverses play a role in image reconstruction and restoration.
4. **Control Theory:** In control systems, pseudo-inverses are used to find solutions for control problems, such as solving the inverse kinematics of robotic arms.
5. **Optimization:** Pseudo-inverses are used in optimization problems to find solutions that minimize error.

In summary, the pseudo-inverse is a valuable tool in linear algebra, extending the concept of matrix inversion to a broader range of matrices and finding applications in numerous fields where solving linear equations or approximating solutions is essential. Understanding its properties and how to compute it is crucial for various mathematical and engineering applications.