---
alias: [Arg min]
---


- 26-9-2022: created

- "Arg max": 
	- They are the points, or elements, of the domain of some function at which the function values are maximized. 
	- They refers to the inputs, or arguments, at which the function outputs are as large as possible. 

- Mathematical definition:
	- Given an arbitrary set X, and a function $f: X \rightarrow Y$, the argmax over some subset $S$ of $X$ defined by: $$\underset{x \in S}{argmax}f(x):={x \in S:f(s)  \leq f(x), \forall s \in S}$$
- Example:
![[Pasted image 20220926123032.png]]
- Figure: argmax of the function is $x=0$. Because both function attain their maximum value at that point. 


- Latex expression 
	- Underset 
	- $\underset{x}{argmax}$

- python implementation:
```python
from scipy.optimize import fmin

# create a straight line plus some noise here
x = np.sort(np.random.uniform(0, 10, 15))
y = 3 + 0.2 * x + 0.1 * np.random.randn(len(x))

# Define the objective function
def objective_function(x):
    return x[0]**2 + x[1]**2

# Initial guess
x0 = [1.0, 1.0]

# Minimize the function
xopt = fmin(objective_function, x0)

print("Optimal solution:", xopt)
print("Minimum value:", objective_function(xopt))

```

