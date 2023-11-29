- 19-10-2022: created

- Related: [[Page rank algorithm|pagerank]]

- Source: https://www.youtube.com/watch?v=JGQe4kiPnrU

- How one might define a ranking of pages based on a model of web network. 

![[Pasted image 20221020003001.png]]
- Markov chain
	- Defined by a few specific properties
		- In web network, individual web pages correspond to states of the markov chain. 
		- Go to page to page, involves a transition probability. 
		- It is assumed the transition probability is based on the number of outgoing links. If it has 3 outgoing links, initially we assume it has P=0.33 goes to each page.  
		- Also possible to alter this prob by prior knowledge of the data. 
- PageRank -- backbone of google search

![[Pasted image 20221020003723.png]]
- How should we rank the web pages to show an end-user?
	- 1. How to measure relative importance?
		- Imagine we count record "from page" and "to page" activities. Count it and use that rate as transition probability.
		- Run that experiment for a long time, the distribution converge. Which is formally called "stationary distribution of Markov chain".
		- For the graph above, we might say, user would use 26% of time to stay at page id=2.

----
## How to model Markov chain?

- Random process involves steps in time. 
- Initially assume prob is uniformly distributed. 
- The prob is actually a weighed sum.

![[Pasted image 20221020004133.png]]
- Step 1:
	- This is a weighted sum calculation of "prob of previous state, times probs of transitioning to the point that we concern.", which can be expressed as a dot product. 

![[Pasted image 20221020004247.png]]
![[Pasted image 20221020004341.png]]
![[Pasted image 20221020004359.png]]
- That dot product can be laid out as a transitional matrix.
- With this matrix we can find the prob of the next step easily. 
- Stationary when applying one more step, the state prob don't change again.


---
## Problems

- Is there a unique stationary distribution?
	- 1. Any initial distribution is stationary distribution 
	- Reducible Markov chain
	- Irreducible Markov chain -- For any irreducible Markov chain, a unique stationary distribution always exist.
- Does every initial distribution converge to the stationary one?
	- For this particular Markov chain, I can start off with any initial distribution, and ends up landing on the same stationary distribution 
	- Periodic Markov chain: No guarantee of convergence to stationary distribution.

![[Pasted image 20221020004725.png]]
![[Pasted image 20221020004839.png]]
![[Pasted image 20221020005031.png]]
![[Pasted image 20221020005131.png]]
![[Pasted image 20221020005311.png]]


----
 - Ergodic theorem for irreducible and aperiodic Markov chains.
	 - 1. A unique stationary distribution $\pi$ exists.
	 - 2. All initial distributions $\pi_0$ converge to $\pi$.
 
 - Markov chain that are irreducible and aperiodic have an incredibly cool and surprising property that no matter what the starting prob, the Markov chain distribution will always converge. 

- In the web page example, no matter the initial users, as long as the Markov chain representing the web graph is irreducible and aperiodic, the long-term distribution of users will converge to stationary.
- This provides a good metric to rank the web pages. 

---
- How we calculate the stationary prob?

- 1. Brute force method
	- Start off by random prob, multiplying dot product N steps until the difference of the changing value of the prob is smaller than a threshold value.
- 2. System of equations methods, utilize the definition directly. 
- 3. Find the eigenvector corresponding to eigenvalue 1 in the transpose of the state transition matrix. 


![[Pasted image 20221020011156.png]]
- Fig: Brute force method

![[Pasted image 20221020011052.png]]
- Fig: method 2

---
Conncetions to eigenvalue / eigenvector

![[Pasted image 20221020011427.png]]
![[Pasted image 20221020011444.png]]
![[Pasted image 20221020011528.png]]

---
![[Pasted image 20221020011615.png]]

- Which of these methods work best for a massive network?
![[Pasted image 20221020011712.png]]
- Fig: the method 2 when dealing with large network, take cubic times of node

![[Pasted image 20221020011814.png|200x200]]
- Fig: getting a decomposition of eigenvalues with eigenvectors takes cubic time 

![[Pasted image 20221020011955.png]]
- Shockingly, brute force method is the most efficient way of calculating 


---
- Problems
	- 1. The page that has no outgoing links (stuck on one page?)
		- Solution: Adding random uniform teleportation solves issues of dead-ends and spider-traps.
		- randomly select a new node to start when that 's the case. 
		- We add a damping factor to all prob of the Markov chain.
	- 2. Allowing dual direction might creates periodic Markov chain.

![[Pasted image 20221020012441.png]]

