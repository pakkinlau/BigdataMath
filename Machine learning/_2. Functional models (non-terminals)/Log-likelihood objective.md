- 26-9-2022: created

---
- Seen: 
	- [[Gaussian discriminant analysis]]
	- Unsupervised learning in GNNs (week 3 of cs224w)
	- [[EM (Expactation-maximization) algorithm]]

- Log-likelihood objective:
	- Condition: 
		- Given the Likelihood $L(\theta|x)=L(\theta|x_1,x_2,\dots)$ is [[identical and independently distributed]], then $(x_1, x_2, \dots) =p(x_1|\theta) p(x_2|\theta) \dots$
	- We use this because log-likelihood has 2 nice characteristics:
		- 1. Products turns to the sums; Exponents turns to the products.  (Products multiple prob. of data points would quickly underflows to 0)
		- 2. Log() is a monotonically increasing function, after we take logarithm on both sides, we can still use it to compare the probability of the actual likelihood. 

---
- Materials from cs224w

- Unsupervised feature learning
	- Idea: 
		- Find embedding of nodes in d-dimensional space preserves similarity. --> Learn node embeddings such that nearby nodes are close together in the network.
		- Goal: Learn a mapping function f that $f:u \rightarrow R^d : f(u):z_u$,
	- Prob. representation of u visit v: $P(v|z_u)$
		- Intuition: Optimize embedding $z_u$ to maximize the likelihood of random walk co-occurrences. 
		- Running "short fixed-length" random walks starting from each node on the graph. 
		- Log-likelihood objective (???):
			- $$\underset{f}{max} \sum_{u \in V}logP(N_R(u)|z_u)$$, which $N_R(u)$ is the neighborhood of node u by strategy R.
			- For each node u collect $N_R(u)$, the multiset of modes visited on random walks starting from u.
			- equivalently, the similarity for 2 graphs: $$L = \sum_{u \in V} \sum_{v \in N_{R(u)}} -log(P(v|Z_u))$$, which the first sigma sums over all nodes u, and the second sigma sums over nodes v seen on random walks starting from u, and the log(x) term predict probability of a single u and v co-occurring on a random walk.
		- Parameterize $P(v|z_u)$ using softmax: $P(v|z_u)={exp(z_u^Tz_v) \over {\sum_{n \in V}ex(z_u^Tz_n)}}$. We want node $v$ to be most similar to node $u$. Intuition: $\sum_{i}exp(x_i)$ close to $max_i exp(x_i)$.
		- Put all together, $$L = \sum_{u \in V} \sum_{v \in N_{R(u)}} -log({exp(z_u^Tz_v) \over {\sum_{n \in V}ex(z_u^Tz_n)}})$$
	- But doing this is expensive. Nested sum over nodes gives $O(|V|^2)$.


---

## Reference: 
- [[(Course) CS224W - Machine learning with graphs (stanford)]]
- [[(Course) CS229 Machine learning]]


----