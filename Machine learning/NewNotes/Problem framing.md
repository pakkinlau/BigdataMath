---
category:[]
alias:[]
tags:[]
---

- 23-10-2022 23:56: created

- Problem framing is the process of analyzing a problem to isolate the individual elements that need to be addressed to solve it. Problem framing helps determine your project's technical feasibility and provides a clear set of goals and success criteria. When considering an ML solution, effective problem framing can determine whether or not your product ultimately succeeds.
- At a high level, ML problem framing consists of two distinct steps:
	- Determining whether ML is the right approach for solving a problem.
	- Framing the problem in ML terms.
---
## understand the problem

- To understand the problem, perform the following tasks:
	- State the goal for the product you are developing or refactoring.
	- Determine whether the goal is best solved using ML.
	- Verify you have the data required to train a model.

- State the goal:
	- Weather app / video app / mail app / map app / banking app / dining app
- Clear use case for [[machine learning]]
	- To confirm that [[machine learning]] is the right approach, first verify that your current non-ML solution is optimized. If you don't have a non-ML solution implemented, try solving the problem manually using a [[heuristic]].
- Against non-ML solution: 
	- Quality: How much better do you think an ML solution can be?
	- Cost and maintenance: How expensive is the ML solution in both the short- and long-term? 
		- Can the ML solution justify the increase in cost? Note that small improvements in large systems can easily justify the cost and maintenance of implementing an ML solution.
		- How much maintenance will the solution require? In many cases, ML implementations need dedicated long-term maintenance.
		- Does your product have the resources to support training or hiring people with ML expertise?
- Against non-ML, data aspect:
	- Abundant: 
		- the model relevant and useful examples in your dataset, the better your model will be. 
	- Consistent and reliable:
		- Having data that's consistently and reliably collected will produce a better model. For example, an ML-based weather model will benefit from data gathered over many years from the same reliable instruments. 
	- Trusted
	- Available: 
		- Make sure all inputs are available at prediction time in the correct format. If it will be difficult to obtain certain feature values at prediction time
	- Correct:
		- In large datasets, it's inevitable that some [[label]] will have incorrect values, but if more than a small percentage of labels are incorrect, the model will produce poor predictions.
	- Representative: 
		- The [[Data|dataset]] should be as representative of the real world as possible. 

- [[feature]]:
	- [[predictive]]

---
- Data
	- To make good prediction, you need [[Data]] that contains [[feature]] with predictive power.

---
## Framing an [[machine learning]] problem

- Define the ideal outcome and the model's goal
- Identify the model's output
- Define success metrics

![[Pasted image 20221024124617.png]]
- Fig: examples of the ideal outcome and the model's goal

- Choose the right kind of [[model]]


---
## Reference

1. [[(Course) google developers - machine learning courses]]