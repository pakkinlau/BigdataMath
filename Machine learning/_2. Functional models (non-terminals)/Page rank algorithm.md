---
alias: [pagerank]
---

- 26-9-2022: created
- superset:
	- [[algorithm]]

- Characteristics: (R1)
	- Importance "Rank" $r_j$ for node $j$ defined by: $$r_j = \sum_{i \rightarrow j} {r_i \over d_i}$$, where $d_i$ is the outgoing degree of node $i$.
	- 1. Links from important pages count more. 
	- 2. The influence shared equally to all of the outgoing links.
	- 3. Importance of each node is the sum of all incoming links.

![[Pasted image 20221020194201.png]]

- Inspirations
	- For guys who wants to be more influential
		- 1. As a short term strategy, try to get more people mention you, would be more useful. The way of doing that is by locating yourself nearby the influential people.  But Influential people mentioning you isn't a thing if those mentioning are widely spread, so you have to be a close friend to those influential people.
		- 2. As a long term strategy, in a game theoretic perspective, if we assume all nodes are trying to be more influential, then all nodes are doing the same behavior (i.e. reducing mentioning the node that has less utility that pushing up its own influence.) Thus the goal of each node is to search for the node that has a higher quality underlying characteristics and mimic it. 
	- My perception:
		- 1. Page rank is more likely to be influential not by how it located in a network structure, but its underlying quality characteristics. 

---

- Computation: (R2)
	- Concept: (R2)
		- Markov chain: each time an agent has a probability to remain on the location, on jump to another linked location. Each node represent a "state" that all agents go to there would have the same probability to exit or remain the state.
		- Transitional probability of node $a$ to node $b$: That represents the prob of an agent on node $a$ leaves $a$ and points to $b$. 
	- Firstly, we assume the webpage network is a fully connected network (to reduce some connections, we can let some connections prob = 0).  (R2)
		- Each node receives all transitional probability from all other nodes. 
		- $\pi_1$ is suggested to be arbitrary initial value.  
		- $\pi_n = [\pi_n(0)\  \pi_n(1)\  \pi_n(2)\  \pi_n(3)\  \pi_n(4)]$
		- $P = \begin{cases} P(0,0) \\ P(1,0) \\ P(2,0) \\ P(3,0)\end{cases}$. This set of prob works by counting the number and quality of links to a page.
		- $\pi_{n+1}=\pi_n P$
	- After many iterations, the probability distribution will converge when $\pi = \pi P$ (R2)
		- solves $r=Mr$ where r can be viewed as both the principle eigenvector of M and as the stationary distribution of a random walk over the graph. (R1)

![[Pasted image 20221020004133.png]]
![[Pasted image 20221020004247.png]]
- Fig: the representation of Page Rank 



---
- Related problem: [[Matrix factorization]]

---
## Implementations

- [[Page rank implementation -- sprank.py]]



---

## Reference: 

1. [[(Course) CS224W - Machine learning with graphs (stanford)]]
2. [[(Video) PageRank -- A Trillion Dollar Algorithm]]