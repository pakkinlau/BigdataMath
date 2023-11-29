- 26-9-2022: created

----
## Reference: [[CS224W - Cases of different level of tasks]]

- 1. Negative sampling
	- Breaking down the idea:
		- a. negative = in NLP, negative sampling means choosing the wrong context word that speed up the training. 
		- b. sampling = take random samples over all candidates. 
	- Instead of normalizing w.r.t. all nodes, just normalize against k random "random samples" $n_i$.
	- $log({exp(z_u^Tz_v) \over {\sum_{n \in V}ex(z_u^Tz_n)}})$ could be approximate to $log(\sigma(z_u^Tz_v))-\sum_{i=1}^k log(\sigma(z_u^Tz_{n_i}))$,$n_i$~$P_v$, which $\sigma$ is chosen to be sigmoid function. and $n_i$ is random distribution over nodes. 