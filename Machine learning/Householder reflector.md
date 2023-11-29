Let $x \in \mathbb{C}^{m-k+1}$ be a vector consisting of the entries $k, \dots, m$ of the $k$th column. The Householder reflector $F$ will perform the following:


![[Pasted image 20231112181457.png]]
Note that, the vector $v$ is given by $v = ||x|| e_1 - x$

Recall that the orthogonal projector $P$ defined by $P = I - \frac{vv^*}{v^*v}$

Projects vectors to the plane orthogonal to $v$. We need to go twice in the direction in order to get our desired result. 

So, we need $F = I - 2 \frac{vv^*}{v^*v}$


Two possibilities
- Practially, we define $v = -sign(x_1)||x|| e_1 - x$
![[Pasted image 20231112181749.png]]

