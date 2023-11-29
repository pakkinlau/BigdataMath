The optimal rank $r$ approximation to $X$ is given by the rank $r$ SVD truncation

$\underset{\tilde X s.t. rank(\tilde X) = r}{argmin} ||X - \tilde X||_F = \tilde U \tilde \Sigma \tilde V^*$
- Optimal rank $r$ approximation
	- Where $\tilde X$ is obtained by retaining only the first $r$ singular values and their corresponding columns in $U$ and $V^*$. 
- Objective function:
	- Find $\tilde X$ such that the rank of $\tilde X$ is $r$ and the Frobenius norm ($||\cdot ||_F$) of the difference between $X$ and $\tilde X$ is minimized. 
	- In the algorithm, the optimization algorithm adjust the elements of $\tilde X$. 