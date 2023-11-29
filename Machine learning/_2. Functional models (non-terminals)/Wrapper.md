- 5-10-2022: created

- What is wrapper
	- Wrappers utilize the learning machine of interest as a black box to score subsets of variable according to their predictive power, regardless of the chosen learning machine. (R1)
	- In its most general formulation, the wrapper methodology consists in using the prediction [[performance]] of a given learning machine to assess the relative usefulness of subsets of variables (R1)
	- Wrappers are often criticized because they seem to be a 'brute force' method requiring massive amounts of computation, but it is not necessarily so.  (R1)
	- In fact, the learning machine is considered a perfect black box and the method lends itself to the use of off-the-shelf machine learning software packages. (R1)


- In practice, when using wrapper, one needs to define: 
	- 1. how to search the [[General space]] of all possible variable subsets: 
		- [[Search algorithm]] --- An exhaustive search can conceivably be performed, if the number of variables is not too large. But, the problemis known to be NP-hard, and the search becomes quickly computationally intractable. 
		- exhaustive search is not practical, so [[Search algorithm|search strategy]] can be used. 
		- [[Search algorithm|search strategy]] is not necessary sacificing [[Prediction]] [[Performance]], in fact, it appears to be converse in some cases,  coarse [[Search algorithm|search strategy]] alleviate the problem of [[Overfitting]]. 
			-  Greedy search starategies:
				- [[forward selection]]
				- [[backward elimination]]
				- both methods yield nested subsets of variables. 

	- 2. how to assess the prediction performance of a learning machine to guide the search and halt it
	- 3. which [[predictor]] to use

---
## Reference
1. [[(Paper) 2003  18500 citation, Guyon and Elisseeff, An introduction to Variable and feature selection]]