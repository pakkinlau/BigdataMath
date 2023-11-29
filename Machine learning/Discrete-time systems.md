
discrete-time systems is a subset of [[Dynamic systems]]
Discrete time dynamical systems are more general than continuous time systems. 
- 1. Discrete time systems can exhibit robustness properties, such as stability, that are easier to analyze and ensure compared to continuous time systems.
- 2. Continuous time signals can be sampled to convert them into discrete time signals, but we cannot do the opposite. 
- 3. Discrete time systems offer more control and flexibility in signal processing and manipulation. 

---
Recall the meaning of variables from [[Dynamic systems]], that is:
- $x$ represents the state of the system, depicted as a vector encapsulating various attributes or variables defining the system's state at a specific point in time.
- $t$ denotes time, indicating the temporal evolution of the system.
- $f$ embodies a dynamic vector field, describing how the system's states (e.g., 1, 2, 3, etc.) change over time. It serves as a vector-valued function that delineates how the current state $x$ transitions to the subsequent state at the next time step.
- $\beta$ stands for a set of parameters within the system. Studying the explicit dependency of these dynamics on $\beta$ elucidates how alterations in these parameters lead to substantial changes in the system's behavior. Such changes are termed bifurcations, signifying significant shifts or branching in the system's dynamics with varying $\beta$ values.


We have a very general differential equation under continuous framework:
$\dot{x} = f(x(t))$

Now we try to define a more general "discrete time" system, because it is snapshot based, not time based. 
$x_{k+1} = F(x_k)$
- **$x_k$**: Represents the state of the system at discrete time $k$. It's obtained through sampling the system at discrete intervals.
- **$F$**: Denotes a given vector field that dictates the transition from one state ($x_k$) to the subsequent state ($x_{k+1}$) in discrete time.
- Here $x_k = x(k \Delta t)$ is obtained the sampling in discrete times. 

What is $F$?
- The discrete-time propagator $F_{\Delta t}$ is parameterized by the time step $\Delta t$. S
- We define the flow map $F_t$ by $F_t(x(t_0)) = x(t_0) + \int_{t_0}^{t_0 + t} f(x(\tau)) d\tau$
- where the right hand side expression is our Flow map, $F_{\Delta t}$

What is flow map?
- Idea 1: transition from continuous to discrete time systems
	- This equation defines a way to transition a system's state from time $t_0$ to $t_0 + t$ in continuous time.
	- It involves integrating the continuous vector field $f(x(\tau))$ over the interval $[t_., t_0 + t ]$ with respect to $\tau$. 
	- This integration represents the cumulative effect of the continuous dynamics on the state $x(t_0)$ over the time interval. 
	- Flow map essentially helps bridge the continuous and discrete descriptions of the system's dynamics, enabling us to approximate the state transition over time steps using the continuous time information encapsulated in the integral of the vector field $f$. 
- Idea 2: Forward Euler integrator: 
	- Forward Euler integrator: $\frac{x_{k+1} - x_k}{\Delta t} \approx f(x_k)$
	- Then we have $x_{k+1} \approx x_k + (\Delta t) f(x_k)$

![[Pasted image 20231111233048.png|300]]

---

- Idea 3: Logistic map
	- Different fixed points corresponding to zero population / full population. 
	- $x_{k+1} = \beta x_k (1 - x_k)$
	- That is a simple nonlinear map that is $x_k$ minus $(x_k)^2$ times a $\beta$ parameter
	- As $\beta$ increases, it becomes more chaotic. 

- Why logistic map interesting in the context of discrete-time systems:
	- 1. Iterative dynamics
		- It is defined by a recurrence relation, where the value of the variable at each step depends on its value at the previous time step. This iterative nature makes it a natural fit for discrete-time systems. 
	- 2. Bifurcation and Chaos
		- The logistic map exhibits complex behavior as the parameter $r$ is varied. 
		- As $r$ increases, the system undergoes a series of bifurcations, leading to periodic, bifurcating, and eventually chaotic behavior. 
	- 3. Universality
		- It is an example of a universal system in the sense that, under certain conditions, it can exhibit a wide range of dynamical behaviors, including periodicity, bifurcation, and chaos. 
	- 4. Applications in modeling 



