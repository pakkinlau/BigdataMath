---
alias: stable
---
Let $f: X \rightarrow Y$ be a function. $f$ is an operation obtaining the result $f(x)$ from the input $x \in X$. 

Our computer is a finite representation of some function. Like $x = \bar x + O(10^{-16})$, where $\bar x$ is our approximation to the number we want ($x$). $O(10^{-16})$ is the numerical round off in representing the number. 

An algorithm is another map $\tilde f: X \rightarrow Y$ (eg: rounding error). Where $\tilde f$ is our approximation mapping. 


- Absolute error: $|| \tilde f(x)  - f(x)|| \sim O(10^{-16})$
- Relative error:  $\frac{||\tilde f(x) - f(x)||}{||f(x)||} \sim O(\epsilon_{machine})$

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
$\frac{||\delta A||}{||A||} = O(\epsilon)$

![[Pasted image 20231025174957.png]]