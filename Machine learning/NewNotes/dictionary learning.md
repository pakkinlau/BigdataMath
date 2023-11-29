---
category: []
alias: [sparse dictionary learning, sparse coding]
tags :[]
---

- 24-10-2022 15:34: created

- Related: 
	- signal processing

- Application:
	- Compressed sensing
	- Signal recovery

- What is dictionary learning?
	- The goal of dictionary learning: (R2)
		- build a [[sparse]] representation of some input data
		- a linear combination of basic elements. These elements are called atoms.
		- a collection of atoms is called a dictionary. 
	- Atoms
		- Atoms in the dictionary are not required to be [[orthogonal]], and they may be an over-complete spanning set. (R1)
	- Complete basis: 
		- Set of vectors such that any vector space can be represented by a linear combination of vectors from the basis. 
	- Overcomplete basis:
		- Complete even one vector is removed. 
	- Sparse coding is a [[feature learning]] method which aims at finding a [[sparse]] representation of the input data (also known as sparse coding) in the form of a linear combination of basic elements as well as those basic elements themselves.  (R1)
		- These elements are called atoms, and they compose a dictionary. (R1)
		- This problem setup also allows the dimensionality of the signals being represented to be higher than the one of the signals being observed. (R1)
		-  The above two properties lead to having seemingly redundant atoms that allow multiple representations of the same signal but also provide an improvement in sparsity and flexibility of the representation. (R1)

---
## Formulation

- $$X \sim DR $$, where
- $$X = [x_1, x_2, \dots, x_K], x_i \in R^d$$
- $$D \in R^{d \times n}: [d_1, d_2, \dots, d_n]$$
- $$R = [r_1, r_2, \dots, r_K], r_i \in R^n$$
- $X$: Input data (d is the dimension of the data)
- $D$: Dictionary to be learned (n is the dimension of the dictionary.)
- $R$: Representation (has $K$ vectors, one for each input data sample, and these vectors are in n-dimensional space, where $n$ is the number of atoms in the dictionary.)

---
## Training in dictionary learning

- The goal of dictionary learning is to minimize the "reconstruction error". 
	- $min||X-DR||_F^2$, 
	- $r_i$ sparse.


- All of this comes together in this optimization: 
		- Related: [[argmax (arguments of the maxima)]]
		- We want to fine $D$ and $r_i$ such that $$\underset{D \in C, r_i \in R^n}{argmin} \sum_{r=1}^K ||x_i - Dr_i||_2^2 + \lambda ||r_i||_0$$
		- $$C := \{ D \in R^{d \times n}: ||d_i||_2 \leq 1 \forall i = 1, \dots, n \}$$
		- $$\lambda > 0$$
		- New variables: 
			- $C$: a constraint that keeps $d$ from becoming arbitrarily large for very small values of $r$. 
			- $\lambda$: A variable that controls the trade-off between sparsity and error minimization. 

---
- Optimization method
	- [[Frobenius Norm]]


`$\begin{align*} a &\myeq b \\ &=c \\ &= d.\end{align*}$`

$$\begin{align*} a &\myeq b \\ &=c \\ &= d.\end{align*}$$

---
## Reference

1. Wikipedia
2. prof. Emily Hand, youtube https://www.youtube.com/watch?v=Ri0ComuqS7Y