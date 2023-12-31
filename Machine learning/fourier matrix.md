- $F_n = \begin{bmatrix} 1 & 1 & 1 & \dots & 1 \\ 1 & W & W^2 & \dots & W^{n-1} \\ 1 & W^2 & W^4 & \dots & W^{2(n-1)}\\ \vdots & \vdots & \vdots & \vdots & \vdots \\ 1 & W^{n-1} & W^{2(n-1)} & \ddots & W^{(n-1)^2} \end{bmatrix}$
	- The first column is $1$
- entries of the matrix
	- $(F_n)_{ij} = W^{ij}$, $i,j = 0,1,2,\dots, n-1$
- involving angle
	- $W = e^{i 2\pi /n} = cos(2 \pi / n) + i sin(2 \pi / n)$
	- $W^n = 1$
		- Consider $cos(2 \pi / n) + i sin(2 \pi / n)$ forms a circle. 
	- In a complex plane, $cos()$ component contributes the x-axis, or, the real part of the component. 
- try changing $n$ of $W$
	- when $n = 4$, $W^4 = 1$
		- recall $e^{i \theta} = i$
		- and we have $n =4$, so $\theta = 2\pi / 4$, 
		- $W^2, W^3, \dots$ = $e^{i(2 \pi / 4)}, e^{i(3 \pi / 4)}, \dots$ = $i,-1, -i, 1$. These values can be obtained in the unit circle of the complex plane. 
- why Fourier matrix is so remarkable
	- 1. fourier matrix is a unitary matrix
	- 2. since it is unitary matrix, it means its conjugate transpose is its inverse. 
		- The second and fourth column of $F_4$ is orthogonal.
		- they are not quite orthonormal. 
		- this property is crucial, including discrete fourier transform(DFT), where ensures the transformation is reversible without information loss. 
	- 3. Eigenvalues: 