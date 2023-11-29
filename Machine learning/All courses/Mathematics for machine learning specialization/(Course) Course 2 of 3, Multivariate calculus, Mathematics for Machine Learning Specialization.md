# Week 1

### Functions
- The attempt of choosing a function to represent the underlying dataset is the essence of science.
- Calculus is simply the study of how these functions change with respect to their input variables and it allows you to investigate and manipulate them. 

### Gradients and derivatives
- Gradient = rise over run = $\underset{\delta x \rightarrow 0}{lim} \frac{f(x + \delta x) - f(x)}{\delta x}$
	- as $\delta x$ gets smaller, it is going to be more accurate to represent the slope of that point. 

## Time saving rules

### Product rule
- Say area $A(x) = f(x) g(x)$.
- If we draw the area with increased increment, $A(x+ \delta x) = f(x+ \delta x) + g(x+ \delta x)$
- So we can divide $A(x+ \delta x)$ into $A(x) + \delta A(x)$
- $\underset{\delta x \rightarrow 0}{lim} \delta A(x) = \underset{\delta x \rightarrow 0}{lim}(f(x)(g(x+ \delta x) - g(x)) + g(x)(f(x+ \delta x) - f(x)))$ 
- $\begin{align*}  \underset{\delta x \rightarrow 0}{lim} \frac{\delta A(x)}{\delta x} &= \underset{\delta x \rightarrow 0}{lim} \frac{{lim}(f(x)(g(x+ \delta x) - g(x)) + g(x)(f(x+ \delta x) - f(x)))}{\delta x} \\ &= f(x)g'(x) + f'(x) g(x)\end{align*}$
### Chain rule
- say we have $h(p(m))$
- $\frac{dh}{dp} \times \frac{dp}{dm} = \frac{dh}{dm}$

---
# Week 2 multivariate calculus

- multivariate calculus is just pretending we are doing univariate calculus.
- figure:
![[Pasted image 20230428054237.png|400]]


- Differentiate with respect to anything
![[Pasted image 20230428054321.png]]

- Figure:
	- in most scenario we don't have a nice analytical expression for our function, to look around.
	- Remember Jacobian pointing uphill / downhill, they are not necessarily pointing to the highest hill.
![[Pasted image 20230428064359.png]]

### Hessian matrix
- Extension of Jacobian matrix
- Second order
- Definition:
	- $H = \begin{bmatrix} \frac{\partial^2 f_1}{\partial x_1^2} & \frac{\partial^2 f_1}{\partial x_1 x_2} & \dots & \frac{\partial^2 f_1}{\partial x_1 x_n} \\ \frac{\partial^2 f_2}{\partial x_2 x_1} & \frac{\partial^2 f_2}{\partial x_2^2} & \dots & \frac{\partial^2 f_2}{\partial x_2 x_n} \\ \vdots & \vdots & \ddots & \vdots \\ \frac{\partial^2 f_n}{\partial x_n x_1} & \frac{\partial^2 f_n}{\partial x_n x_2} & \dots & \frac{\partial^2 f_n}{\partial x_n^2} \end{bmatrix}_{n \times n}$
- For a critical point $\mathbf{x} = (x_1, x_2, \ldots, x_n)$ of $f$, the Hessian matrix evaluated at $\mathbf{x}^_$ can be used to classify the critical point as a maximum, minimum, or saddle point:
- If the Hessian matrix $H$ is positive definite, then $\mathbf{x}^_$ is a local minimum of $f$.
- If the Hessian matrix $H$ is negative definite, then $\mathbf{x}^_$ is a local maximum of $f$.
- If the Hessian matrix $H$ has both positive and negative eigenvalues, then $\mathbf{x}^_$ is a saddle point of $f$.

![[Pasted image 20230428065431.png|400]]


---
# Week 3 multivariate chain rule

- multivariate chain rule
	- $\frac{df}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}+ \frac{\partial f}{\partial z}\frac{dz}{dt}$
	- This allow us to calculate the result in a piecewise manner, rather than substituting everything in at the start.
	- computer are good at solving piecewise problem
		- what is piecewise problem?
- Say we have $f(x_1, x_2, \dots, x_n) = f(\vec {x})$
- then $\frac{\partial f}{\partial x} = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n}  \end{bmatrix}$, $\frac{dx}{dt} = \begin{bmatrix} \frac{dx_1}{dt} \\ \frac{dx_2}{dt} \\ \vdots \\ \frac{dx_n}{dt} \end{bmatrix}$
- $\frac{dx}{dt} = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n}  \end{bmatrix} \cdot \begin{bmatrix} \frac{dx_1}{dt} \\ \frac{dx_2}{dt} \\ \vdots \\ \frac{dx_n}{dt} \end{bmatrix}$


---
# Week 4 - Taylor series
- In some ways, neural networks can be thought of as a generalization of Taylor series.
- Taylor series is a mathematical technique that is used to approximate a function as an infinite sum of simpler functions. These simpler functions are the derivatives of the original function evaluated at a particular point. The more terms included in the series, the more accurate the approximation becomes.
- Similarly, neural networks are also used to approximate functions. They consist of layers of interconnected nodes, which perform simple mathematical operations on the input data. The more layers and nodes in the network, the more complex the function that can be approximated.


