


![[Pasted image 20231125234530.png]]
	- Q: Why $P = I - \frac{vv^*}{v^*v}$? 
		- recall [[Projection formula]]. $\text{proj}_{v}(x) = \frac{v \cdot v^*}{v^* \cdot v} x$, which [[outer product]] projecting $x$ onto $v$ and [[dot product|inner product]] in the denominator normalizing such transformation. 
		- $I - \frac{vv^*}{v^*v}$ is a reflection operator, specifically a reflection about the plane orthogonal to the vector $v$. 
		- Consider we have $b$ projecting onto $a$, to obtain $p$. $e$ is the error vector. and $e = b - p$. $p = Pb$. 
		- To obtain a transformation matrix $b$ onto $e$, we have $(I - P)b = b - Pb = b - p = e$. 
		- So that we have 
