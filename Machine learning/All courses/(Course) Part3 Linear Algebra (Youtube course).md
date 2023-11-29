- Source: https://www.youtube.com/watch?v=y2WqIXrjyC4&list=PLlXfTHzgMRUIqYrutsFXCOmiqKUgOgGJ5&index=2

- What makes a transformation linear?
- The order of multiplication and additions won't affect the transformation, then it is linear transformation
	1. $T(u+v) = T(u) + T(v)$
	- 2. $T(\alpha u) = \alpha T(u)$

---
- If it is linear transformation, we will also ask for
	- its eigenvector.
	- To ask that, we can learn something from the transformation. 


---

- The first linear transformation
	- To specify transformation, I have to give the rule for where each vector goes under the transformation. 
- Reflection: the first linear transformation
	- Out first example comes from the space of geometric vectors. 
	- The first transformation will be "reflection" with respect to a straight line that passes through the origin. 
- Test for linearity
	- Say we have 2 steps: (1) adds up 2 vectors, (2) reflects along the axis. If 2 steps are interchangeable that won't alter the outcome, it is linear. 
- Q: can you find a vector that remain parallel to themselves under transformation?
	- Parallel means, the image of that vector is a scalar multiple of itself. 
	- $R \vec v = \lambda {\vec v}$, where $R$ is the Transformation 
- Eigenvector
	- Eigenvector concepts related to the previous expression $R \vec v = \lambda {\vec v}$.
	- The word "Eigen" has German etymology, it means "cell" or proper, and the corresponding number is called eigenvalue. 
- To find eigenvector in the reflection problem, it is orthogonal to the axis.
- Successive reflection = identity transformation
	- 2 reflection returns the original image
	- $\vec R \vec R \vec v = \vec R^2 \vec v = {\vec v}$
	- $\vec R^2 = I$ , then R = -1 or 1
![[Pasted image 20221224135534.png|400]]
- Fig: reflection 
	- Image
	- Pre-image 

---
- Second example: Projection transformation
- Is it linear?
	- To test it, put 2 random vector on it. Try 2 actions in different order: (1) adds up vectors, (2) projection transformation. If we change the order, would that yield different result?
	- It is linear
- Eigenvector?
	- $\vec P \vec v_1 = \vec v_1, \lambda_1 = 1$
	- $\vec P \vec v_2 = \vec 0, \lambda_2 = 0$
	- So eigenvalue are 1 and 0.
- Any properties can be found?
	- Apply projection successively, $P^n = P$. Any transformation that has this property are all called projection. 
	- Solving $P_n = P$ gives us 1 and 0, which is the same as the eigenvalue of the transformation. 
![[Pasted image 20221224141431.png|400]]
---
- Third example: Rotation transformation 
- It is linear (same way to prove it)
- Eigenvector?
	- $x^4 = -1$ --> No real root. That will force us to talk about complex numbers. 
- ![[Pasted image 20221224142006.png|400]]

---
- Fourth example: Transformation of translation
	- Translation = adding a vector for any given input vector
- Linear?
	- 1. $T(\vec u + \vec v) = \vec u + \vec v + \vec a$
	- 2. $T(\vec u) + T(\vec v) = \vec u + \vec v + 2 \vec a$
	- It is not linear
	- 3. $T \vec 0 \neq \vec 0$
	- It is not linear
- If a transformation is not linear, all the rest question is not applicable. 

---
- Geometric transformation in space

---
- The derivative as a linear transformation
	- Derivative operator: $D$ 
	- We are thinking of functions as vectors. We call them eigenfunctions. But of course it's the same thing. 
- Is it linear?
	- Yes
	- $(f+g)' = f' + g'$
	- $(\lambda f)' = \lambda f$


---
- A linear transformation in $R^n$
- Linearity
	- Would switching a and b, and multiple c by 2, matters? Obviously no. So it is a linear transformation.
- By lucky guess, we can get 3 eigenvector and their corresponding eigen values. 


![[Pasted image 20221224151331.png|400]]
- Fig
---
- All transformation in $R^n$ can be represented by matrix products

![[Pasted image 20221224151638.png|400]]

---
- Why eigenvalues and eigenvectors are so important?
	- Eigenvalues / eigen vectors / the spectrum of the linear transformation as they are known collectively, tell us everything we need to know about the linear transformation'
	- They reduce linear transformation to its bare essentials, and they are communicating all of the relevant things about that transformation in the least amount of information. 
- Q: how many eigenvalues and eigenvectors there are?
	- Scenario 1: same eigenvalue and eigenvectors as the dimension of the space (eg: reflection)
	- Scenario 2: transformations with fewer eigenvalues and eigenvectors than the dimension of the space, namely the derivative. (eg: derivative)
	- Scenario 3: no eigenvalues and eigenvectors (eg: rotation)
	- Scenario 4 ? Never seen transformation with more eigenvectors to its dimension of the space. 
- That's very easy to prove scenario 4 is impossible. The reason is: 
	- Vectors that correspond to different eigen values are linearly independent., and it is very easy to show. 
	- because they're linearly independent and there cannot be more linearly independent vectors than the dimension of the space, there cannot be more independent vectors than the dimension of the space. Thus there cannot be more eigenvectors than the dimension of the space. 
- scenarios
	- 1. as many eigenvalues and eigenvectors as the dimension of the space:
		- we will have n linearly independent vectors, the eigenvectors in an M dimensional linear space. 
		- so they necessarily form a basis
		- when the number of linearly independent vectors matches the dimension of the space, and it's a spanning set, it can deliver any other vector in the space by a linear combination, and it therefore forms a basis. 
	- 2. Double counting eigenvalue and eigenvectors. 
		- eg: the dimension of the corresponding eigen space is more than 1, then we count that eigenvalue twice.... then allowed for more transformations to fit the pattern that they are exactly as many eigenvalues and eigenvectors as the dimension of the space. 
- Choosing eigenvectors as your basis is a very good choice
	- eg: geometric vectors, polynomials, vectors in RN
	- eg: 3D space and linear transformation T
		- T has 3 eigenvectors . $v = \alpha_1 e_1 + \alpha_2 e_2 + \alpha_3 e_3$, 
			- $e_i$ doesn't have any arrows in their head, because they are not necessarily geometric vector, and we preserve the arrow symbol for geometric vectors. 
			- The component space: 
				- It is where all of the computer action takes place, because in component space, everything is numbers, and it's only numbers that computer are really good at. 
		- Apply transformation to $v$, we have $Tv = \alpha_1 T e_1 + \alpha_2 T e_2 + \alpha_3 T e_3$ because of linearity. 
			- Important: Specifying what the linear transformation does for the basis vectors alone is sufficient to specify what it does for any vector Y because then you would just take that vector decompose it respect to this basis transform each one of the basis vectors and then rebuild the linear combination with the same coefficients and there you go you have your image of the vector V that is true for any basis
			- That is a way to reduce a transformation to somewhat essential, by specify what it does for every basis element.
			- If you know what happens to the basis, you know what happens to the entire space. 
		- So having a eigenbasis, which is a basis consisting of the eigenvectors.
		- So by knowing 3 numbers and 3 (eigenbasis) vectors, we can apply the linear transformation no matter how complicated it is. 

![[Pasted image 20221225031121.png]]



- Null space of a linear transformation
	- We have experienced null space before. 
	- Null space = the set of vectors as the collection of all possible linear combinations of those vectors that produce the zero vector. 
		- $\{ v_1, v_2, v_3, v_4\}$ (a set of vectors)
		- $\begin{bmatrix} \alpha_1 \\ \alpha_2 \\ \alpha_3 \\ \alpha_4 \end{bmatrix}$ (a set of collections of all possible combinations of those vectors)
		- $\alpha_1 v_1 + \alpha_2 v_2 + \alpha_3 v_3 + \alpha_4 v_4 = 0$ (complete form, that produces zero vector)
	- This collection of linear combinations turned out to be a linear space in its own right. 
	- Characteristics
		- 1. It is closed under addition and multiplication by a scalar
			- If we have two linear combinations that produce the zero vector, the sum of those two linear combinations would be another linear combination those vectors that produces the zero vector. (eg: $v_1 + v_2$)
			- the same for multiplication by a constant so the collection of linear combinations that produce the zero vector is a vector space in its own right (eg: $\alpha_1 v_1$)
		- 2. it's dimension depends on the number of relationships among the vectors
			- if the vectors are linearly independent then the null space consists of the trivial linear combination alone and is therefore called the trivial null space 
			- if there is one relationship among the vectors then the null space is one dimensional
			- the more independent relationships among the vectors the greater the dimension of the null space 
- Null space with respect to a linear transformation.
	- 1. It will be the null space of that linear transformation 
		- at first it may appear to only be loosely related but once we talk about RN where each linear transformation is represented by matrix we'll be able to connect the concepts of the null space of a linear transformation and the null space of a set of vectors
	- 2. we have already talked about the null space of a matrix but when we talk about the null space of a matrix we merely consider the matrix as a collection of columns
- Define what the null space of a linear transformation is.
	- 1. Given a linear transformation T, consider the set of all vectors that's being sent to zero by this transformation so it's the set of all possible vectors v such that v under this linear transformation equals zero $Tv = 0$. And we focus on $v$, $v$ is the null space if a vector satisfies this property, it's in the null space. 
		- eg: Zero vector is always in the null space. 
	- 2.  the null space is the set of all such vectors that are being sent to 0 by T but is it a vector space 
	- 3. let's show that this set is closed under addition and multiplication by a scalar so in other words if you have two vectors that are being sent to zero by a linear transformation then there's some and scalar multiple will also be sent to zero
		- suppose V 1 has that property and V 2 as the property can we add them together and apply the transformation to the sum well because the transformation is linear it will be the same as applying T to V 1 and then T to V 2 and then adding the two images  $T(v_1 + v_2) = Tv_1 + Tv_2 = 0$.
		- $T(\alpha v) = \alpha Tv = 0$
		- So we have proof that the null space justifies its name it's indeed a vector space
- Few examples of null space
	- 1. Reflection:
		- No vectors send to 0, except zero vector itself. 
		- So the null-space of reflection is the trivial null space
	- 2. Projection:
		- Any vectors that are perpendicular sends to zero.
		- So we have a diagram of null space for Projection transformation.
	- 3. Rotation:
		- Only zero vector send to 0, so it is trivial null space
	- 4. Translation
		- It is not linear. So the concept of null space is inapplicable. 
	- 5. $R^3$
	- 6. Derivative transformation.

![[Pasted image 20221225115130.png|300]]
- Fig: the null space for projection transformation. The whole space is perpendicular to the ...

- the null space can also be considered as the eigen space corresponding to the zero eigenvalues  ($\lambda = 0$)
	- we know that eigenvectors corresponding to the same eigen values form a linear space of their own, AND
	- null space is a linear space
- So 


---


- The inverse of a linear transformation
- Two closely related and crucially important concepts

- Inverse of transformation (skip)

- The eigenvalue algorithm (skipped)


- generalized eigenvectors
- Why they are defective
	- 1. defective matrices do fail to do they fail to provide a basis consisting of eigenvectors why well simply because when dealing with a defective matrix there are fewer eigenvectors than the dimension of the space so there just aren't enough eigenvectors to build a basis 
		- in other situations including solving linear ordinary differential equations with us and coefficients this proves to be a major stumbling block
	- 2. fortunately defective matrices provide a very natural ways of completing the basis and it's a very special property of defective matrices that make that possible
![[Pasted image 20221225095621.png]]
- Fig: eg: this matrix gives us repeated lambda. So it is defective eigenvector because it is failed to provide us enough basis to form the space. 

