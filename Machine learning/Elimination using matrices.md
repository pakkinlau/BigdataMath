---
alias
---

### Elimination matrix

- Introduction of ideas:
	- Elimination matrix: $E_{ij}$
		- Example: $E_{31} = \begin{bmatrix} 1&0&0 \\ 0&1&0 \\ -2&0&1 \end{bmatrix}$
			- This is an elimination matrix that subtracts 2 times row 1 from row 3. Row 1 and 2 stay the same. 
	- Upper [[triangular matrix]]
		- Producing a [[triangular matrix]] could solve the [[systems of linear equations|systems of linear equation]]. And that is the goal of elimination using matrices. 
	- [[backward elimination]]
		- Then the system is solved from the bottom upwards, it is called back substitution.
	- [[pivot]]
		- It serves as a reference point during various operations of matrices. 
	- Multiplier 
		- (Entry to eliminate) divided by (pivot)
	- [[Breakdown]]


- Formulation of the problem:
	- Solve $n$ equations in $n$ unknowns (for any $n$)
	- The end point of the algorithm is having $EA = U$, which $U$ is upper [[triangular matrix]]
	- No row exchanges are needed, the only step allowed is to multiply $A$ by $E_{21}, \dots, E_{n1}$, then $E_{32},\dots, E_{n2}$, as $A$ becomes $EA = U$.
		- Example of the algorithm: dealing a $3 \times 3$ matrix:
			- $U$ is upper triangular, we wants $EA = U$. 
			- The production is $E_{32}E_{31}E_{21}A = U$

### Elimination using matrices
- Elimination using matrices
	- We have $Ax = b$ 
	- Multiple matrix $E_{21}$ on both sides to produce   $E_{21}Ax = E_{21}b$
		- The notation of $E_{ij}$ means the matrix is aiming to eliminate the $a_{ij}$ element of the matrix $A$. 
	- $E_{21}A$ has a zero in bottom left corner because $x_1$ is eliminated from equation 2. 
	- $E_{21}$ is the identity matrix minus the multiplier $a_{21} \over a_{11}$ in bottom left corner. 
	- $EA = [Ea_1, \dots, Ea_n]$
	- After we saw how each step is a matrix multiplication, we assemble each $E_{ij}$ into one elimination matrix $E$
	- $E_{ij}Ax = E_{ij}b$
	- After we saw how each $E_{ij}$ is inverted by its inverse matrix $E_{ij}^{-1}$, assemble all those inverses  $E_{ij}^{-1}$ (in the right order) into $L$. 

- Possible results:
	- 1 intersecting point = OK
	- 2 parallel line: 0y = 8 (Zero is never allowed as a pivot)
	- infinitely any solutions: 0y = 0 

- The sequence of Gaussian elimination (old school method)
	- The first pivot is upper left of the matrix $A$
		- Multiply the "pivot equation" by $l_{21} = a_{21} / a_{11}$ and subtract
		- If the matrix is a bigger square matrix, repeated apply the previous step to the rest of other rows
	- The second pivot is $a_{22}$
	- Repeat, until we have made the lower bottom triangle is all zeros. 
	- The diagonal elements do not have to be value = 1.
