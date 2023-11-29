---
alias: kernel
---


- 26-9-2022: Created

- related: [[kernel method]]

---
## In mathematics
- See [[nullspace]]

Title: The Concept of Kernels in Linear Algebra

Introduction:
In the realm of linear algebra, the term "kernel" holds significant importance and is a fundamental concept in the study of vector spaces, linear transformations, and matrix operations. The kernel, also known as the null space or null set, plays a pivotal role in understanding the properties and behavior of linear transformations and their associated matrices.

Definition:
The kernel of a linear transformation is a subset of the vector space on which the transformation is defined. More formally, if T: V → W is a linear transformation between vector spaces V and W, the kernel of T, denoted as Ker(T) or null(T), is defined as:

Ker(T) = {v ∈ V : T(v) = 0}

In simpler terms, the kernel consists of all the vectors in the domain V that, when transformed by T, result in the zero vector (the additive identity) in the codomain W.

Key Properties and Characteristics:
1. Linearity: The kernel is a subspace of the domain vector space V. This means that it satisfies the three fundamental properties of a vector space: closure under addition, closure under scalar multiplication, and contains the zero vector.

2. Dimension: The dimension of the kernel provides valuable information about the linear transformation and the associated matrix. The dimension of Ker(T) is also known as the nullity of the transformation and is closely related to the rank-nullity theorem.

3. Solving Linear Equations: In practical terms, finding the kernel of a matrix or a linear transformation can be used to solve systems of linear equations. The solutions to homogeneous systems Ax = 0, where A is the coefficient matrix and x is the vector of unknowns, can be found by computing the kernel of A.

4. Orthogonality: In some contexts, particularly in the study of inner product spaces, the kernel is associated with the concept of orthogonality. The vectors in the kernel of a certain linear transformation are orthogonal to the vectors in its image or column space.

Applications:
Kernels are widely used in various branches of mathematics, science, and engineering. Some common applications include:

1. Machine Learning: In machine learning, the kernel trick is used to transform data into a higher-dimensional space, making it easier to separate and classify data points.

2. Image Processing: Kernels play a critical role in image convolution, a fundamental operation used in image processing and computer vision.

3. Differential Equations: Kernels are used in solving linear partial differential equations, where they represent fundamental solutions to differential operators.

Conclusion:
In linear algebra, the concept of kernels provides essential tools for understanding the behavior of linear transformations, solving systems of linear equations, and exploring the properties of matrices. Whether you're studying linear algebra for its theoretical foundations or practical applications in fields like data science or engineering, a solid grasp of kernels is essential.

---
## In machine learning

- In [[machine learning]], [[kernel method]] is a class of algorithms for pattern analysis, whose best known member is the [[Support vector machine]]. Less commonly known algorithm: Importance vector machine, and Kernel PCA. (wiki)
- The general [[tasks|task]] of [[pattern]] is to find and study general types of relations (eg: clusters, rankings, principal components, correlations, classifications) in datasets. 

---
## In [[Knowledge graph completion]]

- TransR -- Kernel space of matrix $M$ : $h \in Ker(M)$ , then $Mh = 0$.
---
## In category theory
- In [[category theory]] and its applications to other branches of mathematics, kernels are a generalization of the kernels of group homomorphisms, the kernels of module homomorphisms and certain other kernels from algebra.  (wiki)

- Kernel has a lot of variant meaning, based on different context (R3):
	- Dictionary:
		- 1. The core, center or essence of an object.
		- 2. Almond fruit broken open, showing the edible kernel.
		- 3. The central part of many computer operating systems which manages the system's resources and the communication between hardware and software components. 
	- Computing
		- Kernel (operating system)
		- Kernel (image processing)
		- Kernel method (machine learning)
		- Kernelization: A technique for designing efficient algorithms
		- Kernel (linear algebra): a set of vectors mapped to the zero vectors
	- Mathematics
		- Kernel (geometry): the set of points within a polygon from which the whole polygon boundary is visible.
		- Kernel (statistics): a weighting function used in kernel density estimation to estimate the probability density fuction of a random variable. 
		- Kernel ([[category theory|category theory]]): a generalization of the kernel of a homomorphism
---

- Applied: GNNs, CNNs. 
---
- The kernel trick avoids the explicitly mapping that is needed to get linear learning algorithms to learn a nonlinear function or decision boundary. (wiki)

- Definition: 
	- $K(x,z) \triangleq \langle phi(x), \phi(z) \rangle$. angle branket indicates [[dot product]].

---
- [[Least mean squares (LMS) algorithm]], with features, with the kernel trick
	- (Stuck!!!) Visit cs229 textbook, page 51, and continue the page [[Least mean squares (LMS) algorithm]]

---
## CNNs
- In [[Convolutional|CNNs]], a kernel / convolution matrix / mask is a small matrix used for blurring, sharpening, embossing, edge detection...etc. Doing it by convolution between the kernel and an image. 

- Internet: 
	- It is a sized k x k filter in CNNs. Each block of the kernel could be assigned different weights.
	- The size of a kernel determine how many pixel of input it receive in one time. size k x k kernel receives k x k sized pixels from the input image.
	- We use symmetric kernels (k x k) because for convolution, we need a 2D matrix and we have to flip the kernel. If we flip horizontally, they will not change. (????)
	- In CNNs, the kernel is nothing but a filter that is used to extract features from the images. The kernel is a matrix that moves over the input data, performs the dot product with the sub-region of input data, and gets the output as the matrix of dot products. 

- In paper: [[(Paper) Luo, W., Li, Y., Urtasun, R., & Zemel, R. (2016). Understanding the Effective Receptive Field in Deep Convolutional Neural Networks]], Sized k x k kernel function $v(t)=\sum_{m=0}^{k-1} \delta(t-m)$, where $\delta$ = 1 if $t = 0$, $\delta=0$ otherwise.

---
## GNNs

- cs224w:
	- 1. Graph level features: Kernels calculates similarity of 2 graphs, and it can be factorized such that $K(G,G')=h_G^Th_G$.


---
## Reference:
1. [[(Course) CS224W - Machine learning with graphs (stanford)]]
2. [[(Course) CS229 Machine learning]]
3. Wiki: Kernel
