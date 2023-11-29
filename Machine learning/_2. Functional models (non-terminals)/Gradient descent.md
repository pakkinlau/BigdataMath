
- 5/11/2023

Writing machine learning as an [[optimization]] problem
- $\theta^* = \arg\min_{\theta} J(\theta)$, where $J(\theta) = \frac{1}{N} \sum_{i=1}^{N} (f(x_i; \theta) - y_i)^2$
	- $J$: objective function matrix
	- $\theta$: parameter matrix of the network
	- $x_i$: certain feature of data $i$
	- $y_i$: true label of data $i$ 

- landscape for gradient descent
	- [[optimization]]
	- [[Least Squares]]
	- There are no general methods available for solving nonlinear systems. Indded, nonlinear systems can have no solutions, several solutions, or even an infinite number of solutions.

---

1. **Basic Idea of Gradient Descent:**
   Gradient Descent is an iterative optimization algorithm used to minimize a function, typically a cost or loss function in the context of machine learning. It works by iteratively moving in the direction of the steepest descent (negative gradient) to find the local minimum of the function.

2. **Derivative Information and Local Minimum:**
   The algorithm utilizes derivative information of the function to guide its iterative steps. At the local minimum, the gradient of the function becomes zero ($\nabla f(x) = 0$).

3. **Updating the Iteration Point:**
   The next point in the iteration is determined using the steepest descent formula:
$$x_{k+1}(\delta) = x_k - \delta \nabla f(x_k)$$
   Here, $x_{k+1}(\delta)$ represents the new point, $\delta$ is a parameter determining how far to move along the gradient descent curve, and $\nabla f(x_k)$ is the gradient at the current point $x_k$.

4. **Minimizing $F(\delta)$ to Find Optimal $\delta$:**
   To compute the optimal value of $\delta$, a function $F(\delta) = f(x_{k+1}(\delta))$ is constructed. The goal is to minimize $F(\delta)$ with respect to $\delta$, which is achieved by finding $\partial F / \partial \delta = 0$.

5. **Orthogonality of Gradient Directions:**
   The result $\partial F / \partial \delta = - \nabla f(x_{k+1}) \cdot \nabla f(x_k) = 0$ implies that the gradients of the current point ($\nabla f(x_k)$) and the future point ($\nabla f(x_{k+1})$) are orthogonal (perpendicular) in the space. In other words, $\delta$ is chosen such that the directions of the gradients at the current and future points are perpendicular, optimizing the movement towards the minimum.

In summary, Gradient Descent is a process of iteratively updating the current point in the direction opposite to the gradient, and the optimal step size ($\delta$) is chosen such that the gradients at the current and next points are orthogonal, leading the algorithm towards the local minimum of the function.

---

**How Gradient Descent Works:**

1. **Initialization:** The algorithm starts by initializing the model parameters randomly or with predefined values.

2. **Computing the Gradient:** The gradient of the cost function is computed with respect to the model parameters. The gradient points in the direction of the steepest increase in the function.

3. **Updating Parameters:** The parameters of the model are updated iteratively by subtracting a fraction of the gradient from the current parameter values. This fraction is known as the learning rate, and it determines the size of the steps taken during optimization. A smaller learning rate leads to slower convergence but can prevent overshooting the optimal solution, while a larger learning rate can speed up the process but may cause overshooting.

4. **Convergence:** Steps 2 and 3 are repeated until a stopping criterion is met, such as a predefined number of iterations or when the change in the cost function between iterations is below a certain threshold. At this point, the algorithm has converged, and the parameters have been optimized.

**Key Concepts and Variants:**

- **Batch Gradient Descent:** In each iteration, the algorithm computes the gradient of the entire dataset. This method guarantees convergence to the global minimum but can be computationally expensive for large datasets.

- **Stochastic Gradient Descent (SGD):** In this variant, the gradient is computed and the parameters are updated for each individual data point. SGD is faster as it processes one data point at a time, but the updates can be noisy, leading to oscillations around the optimal solution.

- **Mini-batch Gradient Descent:** This approach strikes a balance between Batch GD and SGD by computing the gradient and updating the parameters using a subset of the data in each iteration. It combines the advantages of both methods and is widely used in practice.

- **Learning Rate Scheduling:** Adapting the learning rate during training can improve the convergence of the algorithm. Techniques like learning rate annealing or adaptive methods such as Adam and RMSprop adjust the learning rate based on the progress of the optimization process.

Gradient Descent is a cornerstone of machine learning and is employed in various algorithms, including linear regression, logistic regression, neural networks, and deep learning models. Its efficiency in optimizing complex models has made it a fundamental tool for practitioners in the field of machine learning.

---

- 25-9-2022: created

- Figure:
	- [[C]]
![[Pasted image 20220702193645.png]]


---
# Reference