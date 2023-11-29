
Long expression of projection formula: 
- $v = (\frac{v \cdot u_1}{||u_1||^2})u_1 +(\frac{v \cdot u_2}{||u_2||^2})u_2$ + $\dots$ + $(\frac{v \cdot u_k}{||u_k||^2})u_k$

---
## Derivation of projection formula

### Vector projection, dimension = n case

---

Sure, here is the edited version of the original article:

- Formula:
    - The projection of $x$ onto $v$ is given by: $$
\text{proj}_v(x) =\frac{v \cdot x}{v \cdot v} \cdot v
$$ This expression consists of a scalar multiple of the vector $v$. The fraction $\frac{v \cdot x}{v \cdot v}$ represents a scalar value that measures the extent to which $x$ aligns with $v$, normalized by the length of $v$. Finally, multiplying by $v$ rescales the direction of $v$ by the computed amount, yielding the projection of $x$ onto $v$. 
    - When represented in matrix form, we treat $x$ and $v$ as column vectors, and $v \cdot x$ becomes $v^* x$, where $v^*$ is the [[adjoint|hermitian transpose]] of $v$. This results in: 
    - $$
\text{proj}_{v}(x) = \frac{v^* x}{v^* v} \cdot v
$$
    - It's critical to understand that the term $v \cdot v^*$ is a rank-one matrix (assuming $v$ is a column vector), not a scalar. Therefore, $v \cdot v^*$ and $v^* \cdot v$ cannot be directly divided. 
    - In the expression $\frac{v^* x}{v^* v} \cdot v$, the fraction does not represent a matrix division, but a scalar multiple of the vector $v$. The fraction $\frac{v^* x}{v^* v}$ is a scalar, determined by the inner product of the vectors $v$ and $x$ divided by the norm square of $v$. This scalar is then multiplied by the vector $v$ to give the projection of $x$ onto $v$. 
    - The correct formula for the [[orthogonal projector]] onto a one-dimensional subspace spanned by vector $v$ is: $$ 
P = \frac{v v^*}{v^* \cdot v}
$$ This formula results in a matrix $P$ which projects any vector onto the subspace spanned by $v$.
    - In the expression $P = \frac{v v^*}{v^* \cdot v}$, 
	    - the numerator, $v v^*$, is a rank-one matrix that represents the [[outer product]] of $v$ with its adjoint $v^*$. It encodes the direction of $v$ but not its magnitude. 
	    - The denominator, $v^* \cdot v$, is the norm square of the vector $v$, which corrects for the magnitude of $v$. The overall fraction thus represents the projection onto the line spanned by $v$, taking into account both the direction and magnitude of $v$.
    - Notably, the resulting matrix $P$ is an [[orthogonal projector]] or projection matrix, meaning that it satisfies two important properties: $P^2 = P$ (idempotent) and $P^* = P$ (self-adjoint or Hermitian). This is characteristic of all projection matrices. It projects any vector in the space onto the subspace spanned by $v$, leaving vectors in the subspace unchanged and orthogonalizing vectors not in the subspace.

---
- Formula:
	- The projection of $x$ onto $v$ is given by: $$
proj_v(x) =\frac{v \cdot x}{v \cdot v} \cdot v
$$, where the fraction gives us a scalar value that measures the extent to which $x$ aligns with $v$, normalized by the length of $v$. Lastly, multiplying by $v$ rescales the direction of $v$ by the computed amount, giving the projection of $x$ onto $v$. 
	- In matrix representation, we treat $x$ and $v$ as column vectors, so $v \cdot x$ become $v^* x$, which $v^*$ is [[adjoint|hermitian transpose]] of $v$. We have: 
	- $$proj_{v}(x) = \frac{v^* x}{v^* v} \cdot v$$
	- Because $v^* x$ is a scalar and matrix multiplication is associative, we have $$
\text{proj}_{v}(x) = \frac{v \cdot v^*  x}{v^* v} = \frac{v \cdot v^* }{v^* v} x$$
	- Using $a \cdot b = a^* b$ again, we have $$
\text{proj}_{v}(x) = \frac{v \cdot v^*}{v^* \cdot v} x$$, where in this expression, we can extract away [[Orthogonal Projector]] (the fraction) from $x$. 
	- So the [[Orthogonal Projector]] $v = Px$, $P$ would be: $$\frac{v \cdot v^*}{v^* \cdot v}$$
	- We can further discuss the numerator and denominator of this projector:
	- The numerator is outer product, which
	- The denominator is inner product, which 


- , Another expression (based on basis direction) would be like this: $$
v =\sum_i c_i u_i = \sum_i (\frac{v \cdot u_i}{\|u_i\|^2}) \cdot u_i$$
- The $n$-dimension space lies in the summation of all projection components

- Vocabularies:
	- $v$: the original vector
	- $u_i$: one of the basis of the subspace that we want to project our vector $v$. 
	- $u_i'$: The projection of the vector $v$ onto the vector $u_i$
	- $c_i$: the coefficient of this projection, which represents how much of $v$ lies in the direction of $u_i$.
	- $v \cdot u_i$ is the dot product of vectors $v$ and $u_i$.
	- $\|u_i\|^2$ is the squared magnitude of vector $u_i$.

To derive the equation $u'_i = c_i u_i = \frac{v u_i}{\|u_i\|^2} u_i$ in the context of linear algebra and vector projections, we can break it down step by step.

- 1. Determination of component length, $c_i$ 
	- We want to express $c_i$ in terms of the projection of $v$ onto $u_i$. To do this, we use the definition of vector projection:
	- Now, we can see that $c_i$ is indeed given by the expression you provided:$$
c_i = \frac{v \cdot u_i}{\|u_i\|^2}$$
- 2. Determination of component direction, $u_i$
	- the direction of $u_i$​ is determined by the vector $u_i$ itself.


---

### Old notes

   - To compute the projection of a vector $v$ onto a subspace spanned by a set of orthogonal basis vectors $\{u_1, u_2, ..., u_k\}$, you can use the [[projection]] formula:
	 - $v = (\frac{v \cdot u_1}{||u_1||^2})u_1 +(\frac{v \cdot u_2}{||u_2||^2})u_2$ + $\dots$ + $(\frac{v \cdot u_k}{||u_k||^2})u_k$
		 - The notion is that we use [[cosine distance]] to find the length of each components, and [[Basis]] are assumed orthogonal?
		 - Remark:
			 - [[cosine distance]] $cos \alpha = \frac{x \cdot y}{||x|| ||y||}$ look similar to the projection formula but they are actually serving different purpose. 
			 - So, the projection formula could also be written as $v = u_1 cos \alpha_1 + u_2 cos \alpha_2 + \dots + u_k cos \alpha_k$ 
		 - Derivation of projection formula:
			 - 1-Dimension scenario:
				 - Say we have arbitrary vector $v$ projecting into sub-space $u$.
				 - The projection vector $u'_i = c_i u_i$ of $v$ lies on the subspace of $u_i$. Which $c_i$ is a scalar.
				 - Use the orthogonal vector (the difference between new and old vectors, $v - u'_i$) and take [[dot product]] with the projection vector. 
					 - Solve scalar $c_i$
						 - $(v - u'_i)(u_i) = 0$; $vu_i -u'_iu_i = 0$
						 - $vu_i = c_iu_i u_i$
						 - $c_i = vu_i / ||u_i||^2$
						 - Turns out we discovered that the scalar is [[cosine distance]] between new and old vector.
					 - Solve $u'_i$:
						 - $u'_i = c_i u_i = (vu_i / ||u_i||^2)u_i$
			 - For n-dimension scenario:
				 - Because each basis of the space is orthogonal, therefore we can just simply add up each components 
   - Here, "$\cdot$"" represents the dot product, $||u_j||$ is the norm (magnitude) of the basis vector $u_j$, and $u$ represents the orthogonal projection.
