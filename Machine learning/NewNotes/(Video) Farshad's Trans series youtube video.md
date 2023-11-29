---
category: []
alias: []
tags: []
---

- 01-11-2022 01:38: created

https://www.youtube.com/watch?v=RIYjV_Yp6Y0


![[Pasted image 20221101013911.png]]
- Speaker: My favorite conference

![[Pasted image 20221101013938.png]]
![[Pasted image 20221101015210.png]]
![[Pasted image 20221101015219.png]]
![[Pasted image 20221101015232.png]]
- Output:
	- Entity representation (arbitrary dimension such as $R^{100}$) and Relation dimension.
	- d: dissimilarity measure
	- margin $\gamma$: [[mutual information]] for [[semantic hashing]]??? Watch his another video
	- We want head + relation = tail.
	- In the equation, margin is the only source of compensation in order to reach the other level.
![[Pasted image 20221101014648.png]]
- Problem:
	- You have to update embeddings for billions of nodes.
![[Pasted image 20221101014745.png]]
![[Pasted image 20221101014756.png]]
- Number of parameter is linear 
	- $n_ek+n_rk$, $e$ is entity and $r$ is relation, so if you fix dimension of embedding space $R^K$, then it is linear.
