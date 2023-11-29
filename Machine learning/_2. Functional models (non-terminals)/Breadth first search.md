- 25-9-2022: created

- Breadth-first search is so named because it expans the frontier between discovered and undiscovered vertices uniformly across the breadth of the frontier. 

![[Pasted image 20220925103108.png]]
- Figure from Jure's paper / lecture notes. The simutaneously illustrate the BFS and DFS strategy.

- Description: 
	- Breadth-first sampling (BFS): The neighborhood $N_s$ is restricted to nodes which are immediate neighbors of the source. 
		- In that figure for a neighborhood of size k = 4, BFS samples nodes $s_1, s_2, s_3$.
	- Depth-first sampling: The neighborhood consists of nodes sequentially sampled at increasing distances from the source node. In that figure, DFS sample $s_4, s_5,s_6$.

---
- detailed step: 
	- 1. Init: 
		- Queue = empty, (Queue: first in first out)
		- Each vertex except the starting point s is infinite far away from s
		- Each vertex are in white color. 
		- $u.\pi$ represent the predecessor of u.
	- 2. Dequeue itself and enqueue the neighbors of starting point s, adj(s): 
		- Dequque = First-in first-out.
		- Each step checks all immediate neighbors and mark the connection in gray color, which denoted "discovered".
		- `u.d` : the distance from the starting point accumulate itself. (Why we need to track shortest distance?)
	- 3. Jump to each element in adj(s), and then dequeue them, and then enqueue (adj(adj(s))) which are in white color.  The agent standing node is from adj(s) jump to each neighbor u to discover the adj(u)
		- Step into each node $v \in adj(u)$, discover $adj(v)$.

![[Pasted image 20220925105049.png]]
![[Pasted image 20220925103905.png]]
- Figure: from introduction to algorithm (4 guys), book.

- Predecessor / parent: u is a predecessor / parent of v in the breadth-first tree, if u was first discovered earlier than v in the course of scanning. 
- Shortest path: 

---
- Real life example: 
	- A person read 


---
- Reference:
	- Chapter 22, Introduction  to algorithm, TCRC.