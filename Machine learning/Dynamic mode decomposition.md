---
alias: DMD
---

Intuition of DMD:
![[Pasted image 20231112012826.png|200]]

Background
- It gives you a coupled "spatial temporal modes". Developed in around 2010. 
- It can apply to a wide range of complex systems, including disease modeling, neuroscience, robotics, finance, plasmas. It is because it is a data driven model. It does not requires underlying knowledge. 
- Experimental fluid
	- DMD actually approximates the leading eigen-decomposition of the leading eigenvalues and eigenvectors of $A$ matrix, without ever actually computing the $A$ matrix. 

Significance and applications:
- DMD's ability to reveal the coupled spatial-temporal modes is invaluable across carious disciplines:
	- **Prediction and Control:** Understanding how spatial patterns evolve temporally aids in predicting and controlling system behavior.
	- **Feature Extraction:** Identifying dominant spatial modes helps extract critical features influencing system dynamics.
	- **Reduced-Order Modeling:** Capturing essential dynamics via a smaller set of modes enables more efficient modeling and analysis.

Say we have a movie of fluid flow
- we make snapshots for each time period
- we make hundred thousand measurements of vorticity in space
- organize this data into big matrices $X$ and $X'$. 
- $X$: 
	- The columns of $X$ are essentially snapshots reshaped into very tall columns vectors that are evolving in time. So column vector $x_1$ corresponding to the snapshot number 1. 
	- We reshape snapshot and then horizontally stack them together. 
	- Finally we have columns: $x_1, x_2, \dots, x_{m-1}$
- $X'$:
	- It shifted 1 $\Delta T$ in the future
	- Finally we have columns $x_2, x_3, \dots, x_m$

Next step: find a best fit linear operator $A$ that advances $X$ into $X'$, So $X' \approx AX$. (We can also write $A =X' X^\dagger$)

Mathematically, the best fit operator $A$ is defined by $A = \underset{A}{argmin} ||X' - AX||_F = X'X^\dagger$, where $|| \cdot ||_F$ is the Frobenius norm and $^\dagger$ represent the pseudo-inverse. 
- While this setup depicts the theoretical setup of the problem. It is difficult to solve it because $X$ could have huge dimensions. 


Generate eigen flow fields that are dominant spatial coherent mode

The idea is that if you collect sufficient snapshot, what you usually find is that there are dominant coherent patterns that emerge. Even if there is million degrees of freedom of your systems, such as vortex shedding, there is a repeatable  low dimensional set of patterns that emerge from those dynamics. 


---
- Example: video decomposition
![[Pasted image 20231112021141.png|500]]

What is "mode" in general?
- the notion of "mode" in the context of Dynamic Mode Decomposition (DMD) refers to the basic components or fundamental building blocks that represent the spatial patterns or structures within a dynamic system.
- these modes are essential elements derived from the data analysis
- In DMD, modes can take on different forms and interpretations:
	- 1. Column Vectors:
	   - In the context of DMD, the modes can be represented as column vectors extracted from the matrix $A$. These vectors encode spatial patterns or structures within the system.
	-  2. Eigenvectors:
	   - The modes correspond to the eigenvectors of the matrix $A$. Each eigenvector represents a specific spatial pattern or mode, and collectively, they capture the system's spatial dynamics.
	-  3. Spatial Patterns:
	   - These modes can be interpreted as the dominant spatial patterns that describe how the system evolves over time. Each mode encapsulates a distinct spatial structure contributing to the overall system behavior.
### Reconstruction via Modes:
   - By combining these modes with the temporal dynamics (given by eigenvalues), one can reconstruct the system's behavior. The modes, in conjunction with their associated temporal behavior, allow reconstruction of the evolving dynamics of the system.
### Matrix Reconstruction:
   - All modes together can be used to reconstruct the matrix $A$, or more specifically, an approximation of the matrix $A$ that captures the essential dynamics of the system.

---
Discuss why DMD is a "coupled spatial-temporal mode"
- Recall how we construct DMD 
	- first we have data snapshots in time
	- we reshape data into columns and horizontally stack them, also create a shifted snapshot.
	- Approximate the evolution of the system by $X' = AX$. And $A$ has approximate degree of freedom even it is not linear. 
- Coupled spatial-temporal mode nature:
	- Spatial mode: 
		- **Spatial modes** represent the spatial distribution or patterns within a system at a given instant in time. They highlight the spatial structures or arrangements that contribute to the behavior of the system. In essence, these modes are spatial patterns that have specific shapes and magnitudes across different regions or components of the system.
		- **Spatial modes** help identify key features or structures within a system that influence its behavior.
		- The spatial modes of the system correspond to the eigenvectors of the matrix $A$. These modes reveal the spatial patterns or structures within the system that contribute to its behavior.
		- Each mode represents a distinct spatial pattern contributing to the system's evolution.
		- Note that DMD requires us to specify the SVD rank for a reduced representation of data. We use $\tilde \cdot$ (tilde) to denote such dimensional reduction. 
		- We have $X' = AX$, and considering matrix-matrix multiplication, the eigenvectors of $A$ represent the spatial modes of the system, which reveal the spatial patterns or structures within the system that contribute to its behavior. 
		- Brining spatial modes back to our solution: 
			- Recall from [[Linear dynamics]], we have the change of states:  $x(t_0 + t) = e^{At}x(t_0)$ or in its diagonalized form: $A = T \Lambda T^{-1}$ and $x(t_0 + t) = Te^{\Lambda t}T^{-1}x(t_0)$. So, the eigenvalues of $A$ lie in $\Lambda$, which dictates the temporal growth or decay rates of the corresponding modes, and the eigenvectors of $A$, which lie in $T$, correspond to the spatial modes of the system.
	- Temporal dynamics: 
		- **Temporal dynamics**, on the other hand, refer to how these spatial modes evolve over time. They describe how each spatial pattern or mode changes or behaves as time progresses. Understanding the temporal dynamics involves examining how these spatial patterns grow, decay, oscillate, or interact with each other over different time intervals.
		- **Temporal dynamics** reveal how these features evolve, providing insights into the system's stability, growth, or decay.
		- The eigenvalues of the matrix $A$ encapsulate the temporal dynamics. 
		- Eigenvalues dictate the temporal growth or decay rates of the corresponding modes. The corresponding eigenvectors represent the spatial modes of the system.
		- Bringing back temporal dynamics back to our solution: 
			- Recall from [[Linear dynamics]], we have the change of states:  $x(t_0 + t) = e^{At}x(t_0)$ or in its diagonalized form: $A = T \Lambda T^{-1}$ and $x(t_0 + t) = Te^{\Lambda t}T^{-1}x(t_0)$. So, the eigenvalues of $A$ lie in $\Lambda$, which dictates the temporal growth or decay rates of the corresponding modes, and the eigenvectors of $A$, which lie in $T$, correspond to the spatial modes of the system.
- Coupled nature:
	- DMD uniquely couples spatial information (modes) with temporal dynamics, showcasing how specific spatial patterns evolve over time and how these patterns contribute to the overall system dynamics. 

---
- Q: Expand and explain why "Each temporal mode is associated with a complex exponential, $e^{\omega t}$, where $\omega$ is a complex number associated with the eigenvalue of the operator $A$."
- 

In Dynamic Mode Decomposition (DMD), we analyze dynamical systems where the future state of the system can be approximated by a linear function of the current state. This is captured by the relation $AX = Y$, where $A$ is the linear operator, and $X$ and $Y$ are matrices constructed from snapshots of the system at consecutive time points.

When we perform a spectral analysis (eigendecomposition) of the operator $A$, we find its eigenvalues and eigenvectors. Each eigenvalue $\lambda$ is associated with a corresponding eigenvector (which in this context we call the spatial mode). The eigenvalues are generally complex numbers, which we can write as $\lambda = e^{\omega \Delta t}$, where $\omega$ is also a complex number and $\Delta t$ is the time step between the snapshots.

Now, why does each temporal mode follow a complex exponential $e^{\omega t}$?

Because the future state of the system is assumed to be a linear function of the current state, we can write the state of the system at any time $t$ as $x(t) = e^{At}x(0)$, where $x(0)$ is the initial state of the system. If we consider a single mode of the system, the state can be written as $x(t) = e^{\omega t}x_0$, where $x_0$ is the initial state of that mode. The state of the system at time $t$ is essentially a superposition of all modes, each evolving according to its own complex exponential.

Therefore, each temporal mode of the system is associated with a complex exponential $e^{\omega t}$, where $\omega$ is a complex number associated with the eigenvalue of the linear operator $A$. The real part of $\omega$ gives the growth or decay rate of the mode (expanding or contracting in time), and the imaginary part gives its frequency (oscillating in time). 

This is a fundamental idea in the analysis of linear dynamical systems and is key to understanding how DMD provides a spatial and temporal decomposition of the dynamics.


---
Computation of obtaining DMD modes: 

- Step 1: Compute the SVD of $X$: $X \approx U \Sigma V^*$
	- Might be truncate the first five 
- Step 2: Eigenvalue spectrum 
	- $X' = AU\Sigma V^*$
	- By inversing $V^*$, $\Sigma$ and $U$, we can have $\tilde A$ by performing pseudo-inverse on each variables.
	- But we don't want to compute the million by million $A$ so we project $A$ onto dominant singular vectors $U^*$ and $U$, and we obtain a smaller $\tilde A$: 
	- $U^* A U = \tilde A$
		- Question: How can we get singular matrix $U$, without computing $A$? 
	- $\tilde A = U^* X'V \Sigma^{-1}$
	- where $\tilde A$ is a linear best-fit dynamical system that tells me how my POD modes evolve in time, how these dominant coherent pattens evolve in time. 
	- So $\tilde A$ is a much smaller matrix. It is maybe thousand by thousand, one hundred by hundred sized matrix. An it has the same eigenvalue matrix as the big $A$ matrix. 
	- 
- Step 3: Compute the spectrum: $\tilde A W = W \Lambda$
	- Q: what is the matrix $W$? it is eigenvector matrix of $\tilde A$ 
- Step 4: Compute the DMD modes: $\Phi = X'V \Sigma^{-1} W$
	- We call these eigenvectors modes, because they are spatial temporal coherent mode shapes. 
	- $\Phi$ is a high dimensional eigenvectors of $\tilde A$. 
- Step 5: Future state prediction:
	- $\hat X(k \Delta t) = \Phi \Lambda^t b_0$

---
Physical meaning
$\Phi$ holds spatial information (spatial correlations between measurements)
$\Lambda$ holds temporal information (growth / decay / oscillations)

Linear dynamic system 
$x_k = \Phi \Lambda^k x_0$

---

How to use DMD in practice

1. Collect data
2. Organize into matrices
3. DMD (Diagnostics, future state predictions)

---


![[Pasted image 20231122120344.png]]
