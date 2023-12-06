---
alias: stable
---
Let $f: X \rightarrow Y$ be a function. $f$ is an operation obtaining the result $f(x)$ from the input $x \in X$. 

Our computer is a finite representation of some function. Like $x = \bar x + O(10^{-16})$, where $\bar x$ is our approximation to the number we want ($x$). $O(10^{-16})$ is the numerical round off in representing the number. 

An algorithm is another map $\tilde f: X \rightarrow Y$ (eg: rounding error). Where $\tilde f$ is our approximation mapping. 


- Absolute error: $|| \tilde f(x)  - f(x)|| \sim O(10^{-16})$
- Relative error:  $\frac{||\tilde f(x) - f(x)||}{||f(x)||} \sim O(\epsilon_{machine})$

- where $O(\epsilon)$ means "on the order of machine epsilon."


---
###  Well-conditioned function stability

- We say the algorithm $\tilde f$ is accurate if for every $x \in X$, $\frac{||\tilde f(x) - f(x)||}{||f(x)||} = O(\epsilon)$, for some $\tilde x$ with $\frac{||\tilde x - x||}{||x)||} = O(\epsilon)$
	- where $\epsilon$ is the machine precision.


---
Demonstrating stability in computation: 

- Euler discretization: 
	- $y(t + \delta t) = y(t) + \delta t \frac{dy}{dt} + \frac{{\delta t}^2}{2} \frac{d^2 y(c)}{dt^2} + ...$, where $c \in [t, t+ t+ +delta t]$
- local error: $\epsilon_k = \frac{\Delta t^2}{2} y''(c)$
- global error: $E_k = \sum_{j=1}^k \frac{\Delta t^2}{2} y''(c_j) \approx  \frac{\Delta t^2}{2} y''(c) K$

Considering we are computing differential equation $\frac{dy}{dt} = \lambda y$. 

- $\frac{dy}{dt} \approx \frac{y_{n+1} - y_n}{\Delta t} + \epsilon(y_n, \Delta t)$
- $y_{n+1} = Y_{n+1} + e_{n+1}$.
- In computer, we round off the true value to 16 decimal places. 

- In another way, we can write $\frac{Y_{n+1} - Y_n}{\Delta t} + E_n$, where $E_n = \frac{e_{n+1} - e_n}{\Delta t}- \frac{\Delta t}{2} y''(c)$
- From this equation, we can see if $\Delta t$ goes big, the error also go big because $E_n$ goes big. But if  $\Delta t$ approach $0$, then the error would be big as well because $\Delta t$ is acting as the denominator of the first term. 


- The overall error would be like this: 
![[Pasted image 20231126114146.png|300]]

---
- What is this?

Stability

Consider solving $Ax = b$ with perturbation in $A$. assume that $\frac{||\delta A||}{||A||} = O(\epsilon)$


Then we have  $\frac{\|\delta x\|}{\|x\|}\leq\,\kappa\bigl(A\bigr)\,O\bigl(\epsilon\bigr)$

![[Pasted image 20231025174957.png]]

---
The relationship $\frac{\|\delta x\|}{\|x\|}\leq\,\kappa\bigl(A\bigr)\,O\bigl(\epsilon\bigr)$ is derived from a perturbation analysis of the linear system of equations $Ax = b$. Below, I will describe the steps to understand this relationship.

Suppose we perturb $A$ by a small amount to get a new matrix $A + \delta A$. Then the perturbed system of equations is $(A + \delta A)x' = b$. If $x'$ is the solution to the perturbed system, then the change in the solution $\delta x = x' - x$ is given by:

$$(A + \delta A)x' = Ax + \delta Ax' = b$$

Subtracting $Ax = b$ from both sides gives

$$\delta Ax' = \delta A (x + \delta x) = 0$$

Assuming $\delta A$ is small and hence $\delta x$ is small, we can neglect the term $\delta A \delta x$. So we have:

$$\delta Ax \approx 0$$

Now, considering norms, you obtain:

$$\|\delta Ax\| \approx 0$$

Divide both sides by $\|Ax\|$ and use the definition of the matrix norm subordinate to the vector norm to get:

$$\frac{\|\delta A\| \|x\|}{\|Ax\|} \approx 0$$

Rearranging, you get the relative change in the solution:

$$\frac{\|\delta x\|}{\|x\|} \leq \frac{\|\delta A\|}{\|A\|} \kappa(A) = O(\epsilon) \kappa(A)$$

where $\kappa(A) = \|A\|\|A^{-1}\|$ is the condition number of the matrix $A$, and $O(\epsilon)$ is the relative change in $A$. 

This is a simplified explanation. In reality, the derivation involves a more rigorous mathematical treatment. But this gives the basic idea. 

The key takeaway is that the relative change in the solution is bounded by the condition number times the relative change in the matrix. This highlights the critical role the condition number plays in the stability of the solution to a system of linear equations.