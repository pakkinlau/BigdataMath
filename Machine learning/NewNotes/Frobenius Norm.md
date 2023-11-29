---
category: []
alias: []
tags :[]
---

- 24-10-2022 19:26: created

- superset:
	- [[Norm]]

- What is Frobenius Norm?
	- 

- Compute Frobenius norm / Matrix norm.
	- Matrices or vectors embraced with double vertical lines above are Frobenius norm of it. Frobenius norm of vectors or matrices are measuring the magnitude or the norm of a matrix.
	- Let say we have a 2 word (rows), 2 dimensions (columns) English dictionary. $A = \begin{pmatrix} 2 & 2\\ 2&2 \end{pmatrix}$.
	- Frobenius norm: $$||A||_F=\sqrt{\sum_{i=1}^m \sum_{j=1}^n|a_{ij}|^2}$$
	- There is very weird to imagine the physical meaning of Frobenius norm of a matrix. Steve Brunton: Imagine reshaping a (n,m) matrix into a (n \times m,1) vector 
	- $||A_F||=\sqrt{2^2+2^2+2^2+2^2}=4$

- Euclidean distance versus Frobenious norm: 
	- Frobenious norm, is to calculate the distance between vectors. 
	- Recall Euclidean distance: $$d(\vec v)=\sqrt{\sum_{i=1}^n(u_i)^2}$$, which $i$ is the dimension of the vector space. This formula can be proven by Pythagorean theorem.
	- For Frobenious norm, we try to plug in 


---
## Reference

1. [[(Course) NLP  Natural Language Processing with Classification and Vector Spaces]]