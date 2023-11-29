- 26-9-2022: created
- 24-4-2023: really start filling the content to this page

### Maximum likelihood estimation
- MLE concept in machine learning 
	- What is not related?
		- Analytically determine the estimator, as how we traditionally does in statistics.
	- How machine learning applies MLE?
		- Gradient descent.
	- Why we still need to learn MLE, while the neural network automatically manifest MLE?
		- Loss functions are based on the principles of maximum likelihood estimation, which is a common approach used for estimating the parameters of probabilistic models.
		- Loss functions in machine learning have to consider both cases of positive and negative examples, and penalized the model for deviating from the ground truth in either direction. This helps in training the model to make accurate probabilistic prediction for both classes.
			- For example, consider binary cross-entropy loss function $L(\hat y, y) = -[ylog \hat y + (1-y)log(1 - \hat y)]$
				- When $y=1$, $L$ becomes $log \hat y$
				- When $y=0$, $L$ becomes $log(1 - \hat y)$

- When discussing why we use certain loss function in gradient descent, we want the Loss function can represent the underlying dataset, which involves the concept of maximum likelihood estimation.

- Basic formulation of likelihood function, $L(\theta|X)$
	- It is defined as the probability density function (pdf) or the probability mass function (pmf) of the observed data, treated as a function of the unknown parameters, with the observed data fixed. It is denoted as $L(\theta|X)$, where $\theta$ represents the parameter(s) to be estimated and $X$ represents the observed data.
	- For continuous probability distributions:
		- $X = x_1, x_2, \dots, x_n$
		- $L(\theta|X)$: 
			- Likelihood function, of observing the data, where $\theta$ is the set or parameters of the distribution with unknown values.
			- We can imagine the set of data $X$ and is fixed, and the list of variables in $\theta$ could change. Can we can plot a graph which the vertical axis represents the likelihood of obtaining the observed data $X$ from the model parameterized by $\theta$.
		- $f(X|\theta)$:
			- probability mass function of the observed data $X$, given a specific set of parameter values $\theta$. 
			- what is PMF?
				- horizontal axis of pmf is the variance of discrete or continuous label. EG apple, pear, banana, or 0-10 if it is continuous data. 
				- vertical axis is the possibility of that label would occur.
			- The pmf represents the PMF if $X$ is discrete, or the PDF if $X$ is continuous, of the observed data $X$ under the assumed statistical model with parameter values $\theta$. 
		- $L(\theta|X) = f(X|\theta)$, 
			- this equation defines likelihood is the value that are dependent on the value of parameters, where the observed data is given. 
			- In some sense if both data and parameters are unknown, then likelihood function and PMF function (i.e. the left hand and right hand side of the equation) would be the same thing.
		- $f(x,y)$
			- Joint probability distribution
				- Joint probability brings up an idea of "separating the factors into pieces"
				- In joint probability, we express the occurrence as $f(x,y)= P(X=x, Y=y)$. 
					- which means "Function of x and y" provide a representation of the joint behavior of variable x and y would change the occurrence of variable $x$ and $y$. 
				- If two events are independent to each others, then $P(A \land B) = f(x,y) = f(x)f(y)$
		- $f(x_1, x_2, \dots, x_n|\theta)$
			- Therefore, we can split the function as a product of univariates such that $f(x_1, x_2, \dots, x_n|\theta) = f(x_1|\theta)  \times f(x_2|\theta) \times \dots \times f(x_n|\theta)$
			- The reason for we can split it like that is because data are IID, the occurrence of one data point does not depend on the occurrence of any other data point.
			- Taking products allow the likelihood function reflects the joint probability of observing the entire dataset.
		-  $L(\mu, \sigma| x_1, x_2, \dots, x_n) = L(\mu, \sigma | x_1) \times \dots \times  L(\mu, \sigma | x_n)$
			- By using up the following two facts discussed above
				- $f(x_1, x_2, \dots, x_n|\theta) = f(x_1|\theta)  \times f(x_2|\theta) \times \dots \times f(x_n|\theta)$
				- $L(\theta|X) = f(X|\theta)$
			- We can make a statement of this: 
				- $L(\mu, \sigma| x_1, x_2, \dots, x_n) = L(\mu, \sigma | x_1) \times \dots \times  L(\mu, \sigma | x_n)$
			- By factorizing the likelihood function for i.i.d. data, we can treat the estimation of parameters as a separate optimization problem for each data point, and then combine the solutions to obtain the overall estimate of the parameters.
		-  $\underset{\mu, \sigma}{argmax}\ {L(\mu, \sigma| x_1, x_2, \dots, x_n)}$ is similar to $\underset{\hat y}{min}\ L(\hat y, y)$ 
			- 1. What was our model?
				- In logistic regression, our model is $y = f(\theta_1, \theta_2, \dots, \theta_n | x_1, x_2, \dots, x_n) = \theta_1 x_1 + \theta_2 x_2 + \theta_3 x_3 + \epsilon$, where $\theta_k$ are linear hypothesis parameters. 
				- we propose a loss function $L(\hat y, y)$ that could find an optima that could maximize the likelihood the underlying model could describe the observed data.
			- 2. Loss function $L(\hat y, y)$ carries the similar idea of likelihood function
				- Find the model parameters that maximize the likelihood function, is equivalent to minimize the negative log-likelihood.
				- This is because the logarithm is a monotonically increasing function, which means that the values of $log(x)$ and $-log(x)$ have the same optimal values that got them to its optima.
			- 3. Minimizing the loss function, it is equivalently to maximize the likelihood that the model could describe the underlying observed data.
				- When we minimize $L$, we won't change the $\hat y$ directly, but changing the parameters of the underlying model.
				- Express it alternatively, we say that we want $\theta_k$, i.e. maximize the likelihood function $L(\cdot)$ i.e. $\hat \theta_1^{MLE},\hat \theta_2^{MLE},\hat \theta_3^{MLE} = \underset{\theta_1,\theta_2,\theta_3}{argmax} \ L(\theta_1,\theta_2,\theta_3)$ 
					- [[argmax (arguments of the maxima)]] is a function or operator that returns input value(s) which the element is defined in the domain $X$, (i.e. $x \in X$), that maximize a given function or expression.
				- When changing the underlying set of parameters  $\hat \theta_1^{MLE},\hat \theta_2^{MLE},\hat \theta_3^{MLE}$, we can obtain a smaller loss.
				- How $\underset{\theta_1,\theta_2,\theta_3}{argmax}$ actually works, we might refer to Gradient Descent.
		- 

---
(The following part is not related to machine learning, but as an extra material, it is still very useful to convey the meaning of MLE, so we still worth learning it)

- Analytical methods for finding estimators/parameters for normal distribution with MLE
	- Finding the local maxima for each estimator
		- Before we differentiate, we take logarithm for both sides because that makes the calculation way way more easier.
		- The likelihood function and the log of the likelihood function both peak at the same values for $\mu$ and $\sigma$.
		- $ln L(\mu, \sigma| x_1, x_2, \dots, x_n) = ln L(\mu, \sigma | x_1) + \dots + ln L(\mu, \sigma | x_n)$
		- With logarithm, now we can simplify the terms inside easier.
			- if there is power terms, they will become normal terms.
			- if there is multiplications, there will be additions between terms.
		- The final simplified expression for normal distribution would be:
			- $\begin{align*}ln L(\mu, \sigma| x_1, x_2, \dots, x_n) &=\sum_{i = 1}^k [ -\frac{1}{2}ln(2 \pi) - ln(\sigma) - \frac{(x_n - \mu)^2}{2 \sigma^2}] \\ &= -\frac{k}{2}ln(2\pi) - n ln(\sigma) - \sum_{i = 1}^k \frac{(x_n - \mu)^2}{2 \sigma^2} \end{align*}$
			- $\begin{align*} \frac{\partial}{\partial \mu} ln L(\mu, \sigma| x_1, x_2, \dots, x_n) &= 0 - 0 + \sum_{i = 1}^k \frac{(x_n - \mu)}{ \sigma^2} \\ &= \frac{1}{\sigma^2}[(x_1 + \dots + x_n) - n \mu] \end{align*}$
			- $\begin{align*} \frac{\partial}{\partial \sigma} ln L(\mu, \sigma| x_1, x_2, \dots, x_n) &= 0 - \frac{n}{\sigma} + \sum_{i = 1}^k \frac{(x_n - \mu)^2 (2) \sigma^{-3}}{2} \\ &= - \frac{n}{\sigma} + \sum_{i = 1}^k \frac{(x_n - \mu)^2 }{\sigma^{3}} \\ &= - \frac{n}{\sigma} + \frac{1}{\sigma^{3}}\sum_{i = 1}^k (x_n - \mu)^2\end{align*}$
			- Set $\frac{\partial}{\partial \mu} ln L(\mu, \sigma| x_1, x_2, \dots, x_n)$ and $\frac{\partial}{\partial \sigma} ln L(\mu, \sigma| x_1, x_2, \dots, x_n)$ = 0, we have 
				- $\mu = \frac{x_1 + \dots + x_n}{n}$
					- Thus, the maximum likelihood for $\mu$ is the mean of the measurements.
					- So that is where the center of our normal curve will go.
				- $\sigma = \sqrt{ \frac{ \sum_{i=1}^n (x_k - \mu)^2}{n}}$
					- We see that, the MLE for $\sigma$ is the standard deviation of the measurement.
					- Thus, using the formula for the standard deviation to determine the width of the normal curve, given the data, has the maximum likelihood.

- Figure: 
	- The graphs show how numerical values of likelihood function change in respect to different parameter values.
	- source: https://www.youtube.com/watch?v=Dn6b9fCIUpM
![[Pasted image 20230425021600.png|400]]
![[Pasted image 20230425021719.png|400]]


- MLE = finding the distribution that is best describing the set of data
- We have many kinds of distribution models
	- normal, exponential, gamma etc
	- is there any distribution better than the other?
		- MLE for mean
		- 1. most of the values you measure should lies on the mean
			- a. the effect of shifting the distribution
			- b. after shifting, determine the likelihood of observing the sample data
		- MLE for the standard deviation
			- 
- in logistic regression, the use of two terms accounts for the fact that the model needs to be penalized when it predicts a wrong probability value that deviates from the ground truth.
- Formally represent the idea, we have:
	- $\hat \theta = arg max_\theta \ L(\theta|X)$