---
alias: inner product
---

- Ideas of dot product:
	- 1. Requirements of making dot product valid:
		- Dot product is an algebraic operation that takes 2 "equal-length sequence" of numbers (usually coordinate vector) (matrix can be seen as a pack of vector) and returns a single number. 
		- We need "equal-length sequence" because the dot product is defined as the sum of products corresponding elements in two sequences, and this can only be performed when the sequences have the same length. 
	- 2. Dot product as scalar multiplication:
		- In Euclidean geometry, dot product $A \cdot B$ is defined as $|A||B| cos \theta$.
		- Geometric interpretation:
			- if you vectors in the exact direction, it would be a scalar multiplication, if it is not in the exact direction, then the projection of one of the vector would take part in the calculation. 
	- 3. Dot product as a sum of their Cartesian coordinates
		- In modern presentations of Euclidean geometry, the points of space are defined in terms of their Cartesian coordinates. 
			- 2a. Euclidean space itself is commonly identified with the real coordinate space $R^n$.
			- 2b. The dot product of two vectors specified with respect to an orthonormal basis, is defined as: 
				- $a \cdot b = \sum_{i=1}^n a_i b_i = a_1 b_1 + a_2 b_2 + \cdots + a_n b_n$
				- $x \cdot y = \sum_{i=1}^m {\bar x}_i y_i$
	- 4. The inner product of a vector $x$ with itself gives the squared norm (also known as the squared magnitude or squared length) of that vector. 
		- $|| x ||^2 = \langle x, x \rangle$


- Compute dot product in python: `dot(A,x)`
- Review of $A$ times $\vec x$
	- $A \vec x = \vec b$ , A matrix times a vector gives a vector.
	- $Ax$ is a combination of the columns of $A$
	- To compute each components, we use the row form of matrix multiplication
	- Components of $Ax$ are dot products with rows of $A$, i.e. $\sum_{j=1}^n a_{ij}x_j$
- Property
	- 1. Extending the transpose characteristics of dot product 
		- Let $A$ be $m \times n$ matrix. for $x \in R^n$ and $y \in R^m$:
			- $(Ax) \cdot y = x \cdot (A^Ty)$
---
Certainly! Let's expand the given equation step by step using matrix-vector multiplication and the properties of the dot product. 

Given $A$ is an $m \times n$ matrix, $x$ is a column vector in $R^n$, and $y$ is a column vector in $R^m$, the equation to be proved is:
$$(Ax) \cdot y = x \cdot (A^Ty)$$

Here's the expansion of the steps:

1. **Matrix-Vector Multiplication:**
   
   First, we perform the matrix-vector multiplication $Ax$. Let $A$ be represented as:
$$A = \begin{bmatrix}
   a_{11} & a_{12} & \dots & a_{1n} \\
   a_{21} & a_{22} & \dots & a_{2n} \\
   \vdots & \vdots & \ddots & \vdots \\
   a_{m1} & a_{m2} & \dots & a_{mn}
   \end{bmatrix}$$

   And $x$ as a column vector:
$$x = \begin{bmatrix}
   x_1 \\
   x_2 \\
   \vdots \\
   x_n
   \end{bmatrix}
$$
   The result of $Ax$ is a column vector $B$ in $R^m$ obtained by multiplying each row of $A$ by the corresponding element of $x$ and summing them up:
$$B = \begin{bmatrix}
   (a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n) \\
   (a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n) \\
   \vdots \\
   (a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n)
   \end{bmatrix}
$$
2. **Dot Product with $y$:**

   Next, take the dot product of the obtained vector $B$ with $y$:
$$(Ax) \cdot y = (a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n) \cdot y_1 + (a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n) \cdot y_2 + \dots + (a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n) \cdot y_m\]$$

3. **Transpose of $A$**:

   Now, find $A^T$, the transpose of matrix $A$, which swaps its rows and columns.
$$A^T = \begin{bmatrix}
   a_{11} & a_{21} & \dots & a_{m1} \\
   a_{12} & a_{22} & \dots & a_{m2} \\
   \vdots & \vdots & \ddots & \vdots \\
   a_{1n} & a_{2n} & \dots & a_{mn}
   \end{bmatrix}$$

4. **Matrix-Vector Multiplication:**

   Multiply $A^T$ with $y$:
$$A^Ty = \begin{bmatrix}
   (a_{11}y_1 + a_{21}y_2 + \dots + a_{m1}y_m) \\
   (a_{12}y_1 + a_{22}y_2 + \dots + a_{m2}y_m) \\
   \vdots \\
   (a_{1n}y_1 + a_{2n}y_2 + \dots + a_{mn}y_m)
   \end{bmatrix}$$

5. **Dot Product with $x$:**

   Finally, take the dot product of the obtained vector with $x$:
$$x \cdot (A^Ty) = x_1(a_{11}y_1 + a_{21}y_2 + \dots + a_{m1}y_m) + x_2(a_{12}y_1 + a_{22}y_2 + \dots + a_{m2}y_m) + \dots + x_n(a_{1n}y_1 + a_{2n}y_2 + \dots + a_{mn}y_m)$$

Comparing this with the earlier expression for $(Ax) \cdot y$, you can see that $(Ax) \cdot y = x \cdot (A^Ty)$, verifying the given equation.

---
	- 2. $v^Tw = v \cdot w$
		- This property connect [[transpose]] matrix, vector multiplication, and dot product. 
		- This property is true because algebraically they are equivalent.  $v^Tw = \begin{bmatrix} v_1 \cdots v_n \end{bmatrix} \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix} = v_1w_1 + \cdots + v_nw_n = v \cdot w$
		- This property reinforces the idea that the dot product is a special case of [[Matrix-Vector Multiplication]].
	- 3. 
- Relationship of other linear algebra entities
	- Euclidean [[Vector Norm]]
		 - The length of a vector is defined as: $\sqrt{A \cdot A} = (\sum_{i=1}^m |x_i|^2)^{\frac{1}{2}}$
	 - The cosine angle between two unit vector is $A \cdot B$. 
		- Zero is a special value in dot product.
		- In dot product, it means 2 vectors are perpendicular if 2 vectors have length.

- hermitian inner product
- hermitian inner product for functions in $[a,b]$

![[Pasted image 20230927124059.png]]

![[Pasted image 20230927124225.png]]

---

- 27-9-2022: created

- [[Linear algebra]]

- In engineering, we don't have the solution exactly on the plane, but we also want the closest solution. So we calculate inner product. (R2)
	- To calculate that, we need the concept of length. 
		- For a vector, the length of the yellow arrow $v = \sqrt{x^2 + y^2 + z^2}$. (R2)
		- For a polynomial (eg: $x^2-x+3$), the way of doing it, is not by defining length directly. We can't use length. (R2)
	- Inner product, in geometric vectors are called scalar product / dot product. That will give us clue on how to carry that over to other spaces.  (R2)
	- Then we can learn that inner product is much more fundamental than length. Length and angles follow from the inner product.  (R2)

![[Pasted image 20221008195205.png]]

---
## Review of dot product (R2)
- Dot product: 
	- $$\vec{a} \cdot \vec{b} = len(\vec{a}) \cdot len(\vec{b}) \cdot cos\theta \tag{1}$$
	- $\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a} \tag{2}$
	- $$(\vec{a} + \vec{b})\cdot \vec{c} = \vec{a} \cdot \vec{c} + \vec{b} \cdot \vec{c} \tag{3}$$
- Decomposition of dot product:  Assume decomposing a vector into basis vectors: (R2)
- $\vec{v} = \alpha_1 \vec{e_1} + \alpha_2 \vec{e_2} + \alpha_2 \vec{e_3}$
- $e_1\vec{v} = e_1 \cdot (\alpha_1 \vec{e_1} + \alpha_2 \vec{e_2} + \alpha_2 \vec{e_3})$
- $e_1\vec{v} = \alpha_1 |\vec{e_1}|^2 + 0 + 0 = \alpha$
- $\alpha_1 = \vec{v} \cdot \vec{e_1}$
- Change the basis: $\alpha_i = \vec{v} \cdot \vec{e_i}$
- To make it could feed back to original equation, we have: $$\alpha_i = {\vec{v} \cdot \vec{e_i} \over \vec{e_i} \cdot \vec{e_i}}$$
---
## Requirements (R2)

- As long as you satisfy these properties, you have dot product / inner products:
	- 1. Positive definiteness 
		- -- that you can execute eqn 1.
	- 2. Commutative 
		- -- that you can execute eqn 2.
	- 3. Distributive  
		- -- that you can execute eqn 3.


---
## Really introducing inner product (R2)

- Notation is different: 
	- For dot products, it is $\vec{a} \cdot \vec{b}$.
	- For inner product, parenthesis = c-dot. 
		- it is $(a,b) = (b,a)$, 

- Inner product is a generalization of the dot product.
	- $\langle u + v, w \rangle$ = $\langle u,w \rangle$ , $\langle v,w \rangle$
	- $\langle \alpha v, w \rangle$ = $\alpha \langle v, w \rangle$
	- $\langle v, w \rangle$ = $\langle w, v \rangle$ 
	- $\langle v,v \rangle \geq 0$ and equal if and only if $v = 0$.
	- len(a) $a \overset {def}{=}$ $\sqrt{(a,a)}$ (In linear algebra we can derive it, but in inner product, here it comes the definition of "length" since this space don't have this concept yet)
	- 

$A \overset{SDS}{DS} B$


- The innear product of two vectors in the space is a scalar, often denoted with angle brackets such as $\langle a,b \rangle$.





---
## Reference

1. Wolfram mathworld: https://mathworld.wolfram.com/InnerProduct.html
2. 8:00 of MathTheBeautiful youtube: https://www.youtube.com/watch?v=Ww_aQqWZhz8

