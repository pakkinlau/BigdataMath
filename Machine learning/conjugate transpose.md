---
alias: conjugate transpose matrix
---
Q: is this the same as [[adjoint]]



- Definition: 
	- The need of developing [[conjugate transpose|hermitian]] / [[conjugate transpose|conjugate transpose matrix]] can be referred to determining the length of [[complex vector]]. The details please go to [[complex vector]] page. 
	- Notation:
		- $A^* = A$ or $A^H = A$  
			- $A^H$ is called "A Hermitian", but it is not [[hermitian matrix]]
			- ( I prefer the notation of right hand side)
- Property:
	- 1. Inner product:
		- Two choices:
			- a. $\bar a^T a = a^H a$ 
			- b. $a^T \bar a$ 
			- This is a free choice. 
		- While $a^Ta$ can only be applied on real vector multiplications, $a^Ha$ can be applied on both complex vectors and real vectors. Since the conjugate of real number is also a real number. 
		- Example
			- $u = \begin{bmatrix} 1 \\ i \end{bmatrix}$ and $v = \begin{bmatrix} 1 \\ i \end{bmatrix}$ don't look perpendicular, but they are. A zero inner product still means that the complex vectors are orthogonal. 

Here, �†A† represents the adjoint (conjugate transpose) of the operator A. In other words, an operator is Hermitian if it is equal to its adjoint.

Key Properties:

1. Real Eigenvalues: Hermitian operators always have real eigenvalues. This property is particularly important in quantum mechanics, where observable quantities (corresponding to Hermitian operators) must yield real-valued results.
    
2. Orthogonal Eigenvectors: Hermitian operators have orthogonal eigenvectors corresponding to distinct eigenvalues. This orthogonality property is fundamental in many applications, including spectral decomposition and quantum state representation.
    
3. Hermitian Matrices: In the context of linear algebra, Hermitian operators are represented by Hermitian matrices. A Hermitian matrix is one that is equal to its conjugate transpose (A = A*), where * denotes the complex conjugate.
    
4. Diagonalization: Hermitian matrices can be diagonalized by a unitary transformation, which simplifies various mathematical operations and analyses involving these matrices.
    

Applications:

1. Quantum Mechanics: In quantum mechanics, physical observables (such as position, momentum, and energy) are represented by Hermitian operators. The real eigenvalues of these operators correspond to measurable quantities, and the eigenvectors represent the quantum states of the system.
    
2. Signal Processing: Hermitian operators are used in signal processing, particularly in the context of Fourier analysis. The Hermitian nature of the Fourier transform allows for efficient and accurate signal decomposition.
    
3. Quantum Computing: Hermitian operators are essential in quantum computing algorithms, where they are used to represent quantum gates and perform unitary transformations on quantum states.
    
4. Spectral Theory: Hermitian operators are extensively studied in spectral theory, which deals with the decomposition of linear operators into their eigenvalues and eigenvectors. This theory has applications in diverse areas of mathematics and science.

