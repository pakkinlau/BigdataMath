---
alias: [objective function]
---

- 5-10-2022: created

- Superset: [[function optimization]]

- Objective function is prominently used to represent and solve the [[optimization]] problems of linear programming. (R2)
- The objective function is of the form $Z = ax + by$, where x, y are the decision variables. (R2)
	- eg: maximize the profits... etc. It is used across industry, commerce, management, etc real-life problems. (R2) (R2)

- Terms related
	- linear programming
	- optimization
	- decision variables
	- constraints
	- feasible region
	- feasible solution
	- optimal solution
	- optimal value

- Theorems: 
	- 1. Let there exist R the feasible region (convex polygon) for a linear programming problem and let Z = ax + by be the objective function. When Z has an optimal value (maximum or minimum), where the variables x and y are subject to constraints described by linear inequalities, this optimal value must occur at a corner point* (vertex) of the feasible region.
	- 2. Let R be the feasible region for a linear programming problem, and let Z = ax + by be the objective function. If R is bounded**, then the objective function Z has both a maximum and a minimum value on R and each of these occurs at a corner point (vertex) of R.

- objective functions for varies models:
	- In general, tasks as optimization problem: $\underset{\Omega}{\text{min}}L(y,f(x))$, 
		- $\Omega$: A set of parameters we optimize, could contain one or more scalars, vectors, matrices...
		- $f$ : It can be a simple linear layer, an MLP, or other neural networks
		- $x$: Sample a minibatch of input graph
		- 
	- [[Loss function]]
	- [[Graph Convolutional Networks|GCN]]:
		- the label $y$ would be 

---
## Reference
1. Brownlee's blog: https://machinelearningmastery.com/introduction-to-function-optimization/#:~:text=Objective%20Functions,-The%20objective%20function&text=In%20machine%20learning%2C%20the%20objective,the%20loss%20of%20the%20model.
2. Cuemath: https://www.cuemath.com/algebra/objective-function/