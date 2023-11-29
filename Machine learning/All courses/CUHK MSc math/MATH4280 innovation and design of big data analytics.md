

---

# Chapter 1 Singular value decomposition

- data:
	- tall-skinny matrix if $n >> m$
	- short-fat matrix if $n << m$


- Matrix approximation
	- rank
	- Frobenius norm
	- Least square
	- Truncation
	- [[singular value decomposition]]
	- Full SVD
	- SVD at a rank $r$
	- [[Matrix approximation or Truncated SVD]] (taking constant values on the infinite sums of SVD)
	- [[unitary matrices]]
	- [[Method of snapshots]]
	- Geometric interpretation
	- Unitary transformation
	- Invariance of the SVD to Unitary transformations
	- [[Cumulative energy]]

Mathematical properties and manipulations
- [[Pseudo-inverse matrix]], least-square, and regression
	- [[Under-determined|Underdetermined]]
	- [[over-determined|overdetermined]]
	- Nonzero singular value
	- [[column space]]
	- Orthogonal complement
	- [[row space]]
	- [[Kernel space]]
	- One-dimensional linear regression
	- Multi-linear regression
- [[Correlation matrix]]

- Principal component analysis
	- Computation of PCA
	- `pca` and `princomp` command
	- Noisy Gaussian data
	- Singular value
	- Examples
		- Cancer data
		- Eigenface data
- Truncation
	- Deciding how many singular values to keep
	- Optimal hard threshold
- Alignment of data
	- It is the central weakness of the SVD for dimensionality reduction and coherent feature extraction in data
- Randomized singular value decomposition
	- Steps of performing Randomized SVD
	- Oversampling
	- Power iterations
Tensor decompositions and N-way data arrays


---
# Chapter 2 Fourier and wavelet transforms

- why learn this?
	- Mathematical foundation for Hilbert spaces, operator theory, approximation theory, the subsequent revolution in analytical and computational mathematics. 
	- A cornerstone of computational mathematics, enabling real-time image and audio compression.
	- Fourier = Given way to tailored bases, such as data-driven SVD.

- Fourier interested in heat equation, but discovered fourier transform is a coordinate transformation that essentially diagonalizes the laplacian operator in heat equation. He made the heat equation simpler by transforming it to eigenvectors and eigenvalues coordinate systems. 

- [[function as vector]]
- [[Fourier series]] 
- [[complex fourier series]]
- [[dot product]]
- [[orthonormal]]

- Fourier series and fourier transform

- [[fourier transform]]

- Discrete fourier transform (DFT) and [[fast fourier transform]] (FFT)

- denoising
	- use FFT on the data and plot signal strength against frequency, and that is our power spectral density (PSD). 
		- the formula of PSD is `fhat * conj(fhat) / n`: the first part is the element-wise product of `fhat` and its complex conjugate. And dividing the result by `n`, scales the PSD to account for the number of samples. 
	- noisy data contains 2 peaks in the PSD. and zero out 


- Transforming partial differential equations
- Gabor transform and the spectrogram
- Wavelets and multi-resolution analysis
- 2D transforms and image processing


---
# Chapter 3 Sparsity and compressed sensing


Sparsity and compression
Compressed sensing
Compressed sensing examples
The geometry of compression
Sparse regression
Sparse representation
Robust principal component analysis
Sparse sensor placement

---

- Introducing new notations, with the content of chapter 1 and 2 
### Fourier Transform:
The Fourier transform represents a signal \( s \) as a linear combination of basis functions, denoted by \( \Phi \). Using matrix notation:
- $\begin{bmatrix} \vdots \\ x \\ \vdots \end{bmatrix}_{(n \times 1)} = \begin{bmatrix} \vdots & \vdots & \vdots \\ \vdots & \Phi & \vdots \\ \vdots & \vdots & \vdots \end{bmatrix}_{(n \times n)} \begin{bmatrix} \vdots \\ s \\ \vdots \end{bmatrix}_{(n \times 1)}$
In practice, the original signal \( x \) can be truncated to a lower dimension:
$\begin{bmatrix} \vdots \\ x' \\ \vdots \end{bmatrix}_{(r \times 1)}$

To restore the image, a lower-dimensional \(\Phi\) is utilized:
$s'_{(r \times 1)} = \Phi^{-1}_{(r \times r)} x'_{(r \times 1)}$

### Singular Value Decomposition (SVD):
Consider a library of faces represented by $X = U_r\Sigma_rV_r$. Using SVD, we can express a signal $x$ as a combination of basis vectors $U_r$ and coefficients $a$:
 $\begin{bmatrix} \vdots \\ x \\ \vdots \end{bmatrix}_{(n \times 1)} = \begin{bmatrix} \vdots & \vdots & \vdots \\ \vdots & U_r & \vdots \\ \vdots & \vdots & \vdots \end{bmatrix}_{(n \times r)} \begin{bmatrix} a \end{bmatrix}_{(r \times 1)}$
### Generalization:
The examples of Fourier Transform and SVD illustrate a broader concept: representing sparse data \( s \) as a more useful vector \( x \). This transformation allows us to truncate and infer information from \( s \) effectively.


- Sparsity
	- In the above example, we say that $s$ is sparse.  
	- Why image is small? 
		- for a 20 x 20 sparse image, $2^{400} > 10^{80}$, it has more combinations to the number of atoms in the universe. 
	- White noise (huge pixel space) and Natural image (smaller subspace)
		- white noise represent random signal matrix from the space
		- Natural image is a tiny subspace of white noise. The possibility of natural images showing within white noise. 
		- But natural image is not focus on one area of the space, it spreads across the whole space. 

- Big picture of compressed sensing
	- General expression of signal transformation 
		- $x = \Phi s$, 
			- where $x \in \mathbb{R}^n$ is our image or signal that is K-sparse in the basis $\Phi$
			- where $s$ is our sparse images, $\Phi$ 
		- This equation represents the original signal or image $x$ being transformed into a sparse representation $s$ in the basis $\Phi$.
		- The vector $s$ is sparse, meaning it has mostly zero values, indicating that the signal can be represented using a small number of non-zero coefficients. 
	- General expression of compressed sensing
		- $y = Cx$
			- $C$:
				- $C$ is our measurement matrix, or operator. It is typically captures the dots in randomized manner. 
				- In the context of imaging, this operation of $C$ can be thought of capturing an image though some form of sensing, which might indeed involve a camera. 
			- $y$:
				-  $y$ is our compressed measurements obtained, (by our camera?) (in the basis $\Phi$?)
			- $x$:
				- measurement / observation vector, which is obtained by compressing the original signal or image. 
			- $s$:
				- original signal / image, represented as a sparse or compressible vector in some domain.
	- Combining two expressions, we have
		- $y = C \Phi s$
			- We are collecting $y$ in our device, and we looks for reconstructing the original signal / image $s$. 
			- sometimes we write it is $y = \Theta s$. 
			- It is a [[Under-determined|Underdetermined]] inverse problem to find $s$ from $y$. 

- Mathematical formation 
	- $y = C \Phi s$
		- This question is a [[Under-determined|Underdetermined]] inverse problem to find $s$ from $y$. So there are infinitely many consistent solution $s$. 
	- Sparest solution
		- In compressed sensing, the sparest solution refers to the solution $\hat s$ of an underdetermined system of equations that has the fewest nonzero elements. 
		- In real-world application, the underlying signal can be represented by only a small number of significant components, with the rest being negligible or noise.
	- Sparsest versus compressed
		- Sparse doesn't mean the same as compressed. While both terms relate to the idea of having fewer non-zero elements, sparse emphasizes the small number of non-zero entries in a mathematical or numerical sense. 
	- $l_0$ pseudo norm:
		- which The notation $|| \cdot ||_0$ denotes the $l_0$ pseudo norm, defined as the number of nonzero entries of the variable inside of it. This can also referred to as the cardinality of $s$. 
	- $l_1$ norm:
		- $l_1 = ||v||_1 = \sum_{i=1}^n |v_i|$
		- In the context of compressed sensing, it represents the sparsity-promoting term.
	- $l_1$ minimization
		- The notation $|| \cdot ||_1$ denotes the $l_1$ norm, given by $||s||_1 = \sum_{k=1}^n |s_k|$
	- $l_2$ norm:
		- The $l_2$ morn of a vector $v = (v_1, v_2, \dots, v_n) \in \mathbb{R}^n$ is calculated as: $||v||_2 = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}$
		- $||C \Phi s - y||$ is the geometric distance between observed data point $y$ and the point in the space spanned by $C \Phi s$.
	- Finding sparest solution $\hat s$
		- $\hat s = \underset{s}{argmin}||s||_0$ subject to $c = C \Phi s$
			- $\hat s$ is the sparest solution
			- The notation $|| \cdot ||_0$ denotes the $l_0$ pseudo norm, defined as the number of nonzero entries of the variable inside of it. This can also referred to as the cardinality of $s$. 
		- This optimization is non-convex, and in general the solution can only by found with a brute-force search that is combinatorial in $n$ and $K$. In particular, all possible sparse vectors in $\mathbb{R}$ must be checked.
		- Relaxing the optimization
			- $\hat s = \underset{s}{argmin}||s||_0$ subject to $c = C \Phi s$
				- Under certain conditions on the measurement matrix $C$, it is possible to relax the optimization to a convex $l_1$ minimization 
				- The notation $|| \cdot ||_1$ denotes the $l_1$ norm, given by $||s||_1 = \sum_{k=1}^n |s_k|$
- Another formulation:
	-  $\hat s = \underset{s}{argmin}||s||_0$, subject to $||C \Phi s - y||_2 < \epsilon$
	- A closely related convex optimization is the following:
		- $\hat s = \underset{s}{argmin}||C \Phi s - y||_2 + \lambda||s||_1$
			- where $\lambda \geq 0$ is a parameter that weights the importance of sparsity.
			- The first term measures the accuracy of the estimation, the second term encouraging sparsity.
			- $\lambda$ balances the trade-off between these two terms. 
			- A larger $\lambda$ will result in sparser solutions, because the penalty of non-zero element is larger. 

- Revision of [[Vector Norm]]


- Sparse representation for classification
	- Leverage sparsity to cross-reference images
		- in addition to a signal being sparse in an SVD or Fourier basis, it may also be sparse in an overcomplete dictionary whose columns consist of the training data itself. 
		- in essence, a test signal being sparse in generic feature library $U$ from the SVD, $X = U\Sigma V^*$, it may also have a sparse representation in the dictionary $X$.  
	- 1. coarse version (downsample) of images
		- our target is having more columns than our rows.
		- which makes it to be a underdetermined optimization problem 
	- 2. stack it to be tall skinny vector
	- 3. do it for every single images


- Robust PCA

- draft of notes
- subtract the mask of the image, ni longer use mask to hide from the cops.
- that only works if we are working for an image of a person.

- face example
	- blocking 20% of the picture (i.e. outliner)
	- how to split wrong data out of true data?
	- you could split it, if you have a library of faces, that learns what is a human face
		- rigid library: taking photos under 64 angles

- decomposing our data
	- $X = L + S$
		- $X$: 
		- $L$: low rank, meaning it is described by principal components:
		- $S$: Sparse matrix, with all of the corruptions
	- There are many ways to split $X$ into $L$ and $S$. , so $X = L + S$ is ill-posed problem.
	- $\underset{L,S}{min}\ rank(L) + ||S||_0$, subject to $L + S =  X$
		- The first part wants the image to be explained by principal components. 
		- The second part wants the $S$ to be sparse, because we do not believe that much of our image is corrupt. 
	- $\underset{L,S}{min}\ ||L||_* + \lambda_0 ||S||_1$, subject to $L + S =  X$
		- This is a relaxation version, so convex optimization can be achieved. 
		- Paper: Candes, Li, Ma, Wright, J.ACM, 2011.

---
Ch 4 - 6: Machine learning and data analysis

# Chapter 4 Regression and model selection

[[regularization]]
[[model complexity]]
[[cross-validation]]
[[objective|objective function]]

Classic curve fitting 
- [[regression]]
- [[Generic Regression]]

[[Gradient descent]]

Nonlinear regression and gradient descent
[[linear regression]]
[[Generic Regression]]
[[over-determined|overdetermined]]
[[Under-determined|Underdetermined]]
Optimization as the cornerstone of regression
The pareto front and LEx parimoniae
Model selection
[[cross-validation]]
Information criteria

---
# Chapter 5 Clustering and classification

Feature selection and data mining
Supervised versus Unsupervised learning
K-means clustering
Dendrogram
Mixture models and the expect-maximization algorithm
Linear discriminants
Support vector machines (SVMs)
Classification tress and random forest
Top1 10 algorithms in data mining 2008

---
# Chapter 6 Neural networks and deep learning

[[neural network]]: 1-layer networks

- [[expressive power]]
Mapping
- [[linearity]]

multi-layer networks and [[activation]] functions
The [[backpropagation]] algorithms
The [[stochastic gradient descent]] algorithm
Deep convolutional neural networks
- [[Convolutional]] layers
- [[pooling]] layers
Neural networks for dynamic systems
The diversity of neural networks

---

Ch 7: dynamics and control
# Chapter 7 Data-driven dynamical system

- why learning this?
	- Dynamical systems provide a mathematical framework to describe the world around us, modelling the rich interactions between quantities that co-evolve in time. 
- overview
	- how to characterize them using data science and machine learning and regression
	- background: the amount of data we could have is growing
	- 1. current limitations  data-driven dynamical systems
	- 2. goals of DMD
	- 3. techniques emerging to characterize these systems

$\dot{x} = f(x,t,u ; \beta)$

- Overview, motivations and challenges
	- [[Dynamic systems]]
		- examples
			- Lorenz
		- subset
			-  [[Discrete-time systems]]
	- [[Linear dynamics]]
	- The way of solving differential equations 
		- `ode45`
		- [[spectral decomposition]]

- Approaches
	- Operator theoretic representations
	- Data-driven regression and machine learning
- [[Proper orthogonal decomposition]]
- [[Dynamic mode decomposition]]
	- [[linear operator]]
	- DMD algorithm
	- Historical perspective
	- Sparse dynamic mode decomposition
		- Sparse sampling in time / space
		- How to select relevant modes 
	- Spectral decomposition and DMD expansion
	- Extensions, applications and limitations
		- Compression and randomized linear algebra
		- Inputs and control
		- Nonlinear measurements
		- De-nosing
		- Multiresolution
		- Delay measurements
		- Streaming and parallelised codes
- Applications
	- Fluid dynamics
	- Epidemiology
	- Neuroscience
	- Video processing
	- Robotics, finance, plasma physics
- [[Sparse identification of nonlinear dynamics]] (SINDy)
	- Generalized linear model
	- Automated discovery of governing equations and dynamical systems
	- `poolData`
	- Discovering partial differential equations
	- Extension of SINDy for rational function nonlinearities
	- General formulation for implicit ODEs
	- Information criteria for model selection
- [[Koopman spectral analysis]]
	- Koopman operator
	- Mathematical formulation of Koopman theory
	- Observables
	- Observability from control theory
	- Koopman eigenfunctions and intrinsic coordinates
	- Koopman mode decomposition and finite representations
	- Koopman mode
	- Hilbert space
	- Invariant eigenspaces and finite-dimensional models
	- Koopman-invariant subspace
	- Koopman embeddings
	- Intractable representation
	- Analytic series expansions for eigenfunctions
	- Quadratic nonlinear dynamics
	- Polynomial nonlinear dynamics
- Data-driven Koopman analysis
	- Extended DMD
	- Approximating Koopman eigenfunctions from data
	- Sparse identification of eigenfunctions
	- Duffing system
	- Data-driven Koopman and delay coordinates
	- Neural networks for Koopman embeddings



---


- Resource: 
	- Book 1 - Data-driven science and engineering - Machine learning, Dynamical systems and control
		- A lot of videos: https://databookuw.com/page-2/page-4/
		- A lot of github source codes: https://github.com/dynamicslab
	- Textbook: https://www.doc88.com/p-0681727468461.html
	- CU lib version:
		- https://julac-cuhk.primo.exlibrisgroup.com/discovery/fulldisplay?docid=alma991039575269503407&context=L&vid=852JULAC_CUHK:CUHK&lang=en&search_scope=All&adaptor=Local%20Search%20Engine&isFrbr=true&tab=default_tab&query=any,contains,%20Data-driven%20science%20and%20engineering%20-%20Machine%20learning,%20Dynamical%20systems%20and%20control&sortby=date_d&facet=frbrgroupid,include,9045474545672049446&offset=0
	- Book 2 Python for programmers with introductory AI case studies
		- Textbook: https://www.doc88.com/p-92929299851986.html

- Course resource:
last year powerpoint: [https://www.math.cuhk.edu.hk/course/2223/math4280](https://www.math.cuhk.edu.hk/course/2223/math4280)  
ID: math4280  
pw: math4280#2324*term1

ID: math4280
pw: math4280#2223*sem1
