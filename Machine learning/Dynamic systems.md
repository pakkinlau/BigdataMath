11/11/2023
In simplest form, we have:
$y = g(x,t) + n$
- where $y$ is measurements, $n$ is noise. 

In dynamical systems, we have: 
- $\frac{d}{dx}x(t) = f(x(t), t, u; \beta) + d$, 
	- It is a system of coupled differential equations. 
	- where $x$ is the state, a vector that represents the state of our system. It is a vector that has the minimal number set of values that you need to describe your system. 
		- example
			- A pendulum is uniquely defined, not just by its angle-theta, but by its angular rate, $\dot{\theta}$. So the state of a system is $\theta$ and $\dot{\theta}$
			- For stock market, the state of the system might be the value in all of the stocks, and there might be more information that needs to go into that state vector. 
			- Weather - weather condition on 1 kilometer grid. 
	- $t$ is time
	- $u$ is actuation (control)  --- not a focus of MATH4280
		- This is a variable representing all of the variables that we have active control over. 
		- Those variables can change the dynamics
	- $f$ is a given vector field 
		- That is dynamic. That describes the dynamic of state 1, state 2, state 3...
		- $f$ is a vector valued function that tells me given a current state $X$, how does that state change in the next time instant.
		- example
			- Newton second law
	- $\beta$ is a set of parameters
		- Other parameters that we have no direct control over. 
		- We want to understand explicit dependence of these dynamics on those beta parameters, as I change those parameters, I might get really big changes in the dynamics called bifurcations. So $\beta$ can be very important. 
	- $d$ is disturbance 
- measurement of $x$
	- we might just measure some "proxy" measurement
		- eg: neuroscience - EKG / EEG neurons 
		- 

- Example of systems
	- $\dot{x}$: A system that an aircraft is flying
	- $\beta$: wind speed, humidity... 
	- $u$: control variables, how far my flaps of airplane moves
	- $f(\cdot)$: The dynamics / vector field. It tells how fast $x$ is changing. 
- More example of system
	- [[Lorenz system]]
- Simpler case: autonomous system
	- $\frac{d}{dx} x(t) = f(x(t))$, where the right hand side has no time dependence or parameter.
	- You can also say Newton second law is an example of dynamic systems. 
	- Traditionally we write down Newton's law from first principles using physics
	- Increasingly the complex systems, we cannot write down the first principle to start the analysis, but we can take a large volume of neuro-science, financial data, to establish a more robust model of reality. 
- Challenges
	- [[Nonlinearity]]
	- [[Unknown dynamics]]
	- [[Dynamic systems]]
	- chaos, transients
	- noise, stochasticity
	- [[multi-scale]] dynamics
	- uncertainty
	- [[High dimensional dynamics]]
	- latent / hidden variables 
- Application
	- Future state prediction (predicting $\dot{x}$, an ensemble of predictions)
	- Design and optimization (F1 race cars / yachts) - fluid dynamics
	- Control - Measure my system, with a model of the system, to design an actuation signal to modify its behavior actively using sensor based feedback
	- Interpretability and physical intuition - A lot of machine learning methods are hard to interpret and don't give you intuition. 
- Techniques:
	- Physicist use coordinate transformation to make dynamical systems looks linear. But now  people use deep learning, or sparse regression, to find coordinate transformation of data
- Key points:
	- Most machine learning are developed for static task. Using RNN to model dynamic systems. 
	- If you know something about the system, such as energy is conserved, or mass is conserved, you can dramatically improve the learning of these systems by enforcing those constraints, directly in the learning procedure. 