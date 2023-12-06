In Householder transformation, $Q_k$ is chosen to have $\begin{pmatrix} 1 & 0 \\ 0 & F \end{pmatrix}$ . A requirement for $F$ is that it will create zero below the $k^{th}$ diagonal element. 

Let $x \in \mathbb{C}^{m-k+1}$ be a vector consisting of the entries $k, \dots, m$ of the $k$th column. The 
Householder reflector $F$ will perform the following:
![[Pasted image 20231112181457.png]]

$m$ sized Householder reflector are defined to make the entries below the ${(m - k + 1)}^{th}$ row of the matrix to be zero. 

Note that, the vector $v$ is given by $v = ||x|| e_1 - x$

Recall that the orthogonal projector $P$ defined by $P = I - \frac{vv^*}{v^*v}$

Projects vectors to the plane orthogonal to $v$. We need to go twice in the direction in order to get our desired result. 

So, we need $F = I - 2 \frac{vv^*}{v^*v}$


Two possibilities of $v = ||x|| e_1 - x$ of householder reflector $F$: 
- Practically, we have  $v^{\pm} = \pm ||x|| e_1 - x$
- So there are two possibility $v = -sign(x_1)||x|| e_1 - x$ or $v = sign(x_1)||x|| e_1 + x$
- Discussion on $sign(x_1)$: 
	- where $sign(x_1)$ term is introduced to avoid loss of numerical precision that happens due to subtracting two nearly equal numbers (also known as "catastrophic cancellation"). 
	- When $x_1$ is positive, $-sign(x_1) = -1$ and so $- ||x|| e_1 - x$ which is $v^{-}$. Which means that we are reflecting $x$ in the opposite direction of $e_1$. 
- Choice of $v$: 
	- The choice between the two expressions $v = -sign(x_1)||x|| e_1 - x$ and $v = sign(x_1)||x|| e_1 + x$ is up to the user. Because they are both doing reflections. 
![[Pasted image 20231112181749.png]]

