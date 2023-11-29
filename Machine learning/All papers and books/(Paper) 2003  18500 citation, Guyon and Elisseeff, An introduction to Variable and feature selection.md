- 5-10-2022: created

- Found this when: writing [[Feature selection]]

- Abstract:
	- The objective of variable selection is three-fold: improving the [[prediction]] [[performance]] of the predictors, providing faster and more cost-effective [[neural network|predictor]] (??), and providing a better understanding of the underlying process that generated the data.

- Objective function
- Feature construction
- Feature ranking
- Multivariate feature selection
- Efficient search method
- Feature validity assessment methods

- 1997:
	- Gene selection
		- For microarray data.
		- The variables are gene expression coefficients corresponding to the abundance of mRNA in a smple.
		- A typical classification task is to separate healthy patients from cancer patients, based on their gene expression “profile”. 
		- Usually fewer than 100 examples (patients) are available altogether for training and testing. But, the number of variables in the raw data ranges from 6000 to 60,000. 
	- Text categorization
		- THe documents are represented by a "bag-of-words", this is a vector of dimension the size of the vocabulary containing word frequency counts. (proper normalization of the variables also apply).
		- Vocabularies of hundreds of thousands of words are common, but an initial pruning of the most and least frequent words may reduce the effective number of words to 15,000
		- Large document collections of 5000 to 800,000 documents are available for research.
		- Typical tasks include the automatic sorting of URLs into a web directory and the detection of unsolicited email (spam).
		- For a list of publicly available datasets used in this issue, see Table 1 at the end of the paper.

- Potential benefits of variable and feature selection
	- facilitating data visualization
	- facilitating data understanding
	- reducing the measurement and storage requirements
	- reducing training
	- utilization times
	- defying the curse of dimensionality to improve prediction performance

- This paper: 
	- focus mainly on constructing and selecting subsets of features that are useful to build a good predictor. 
	- This contrasts with the problem of finding or ranking all potentially relevant variables. 
	- Selecting the most relevant variables is usually suboptimal for building a predictor, particularly if the variables are redundant. Conversely, a subset of useful variables may exclude many redundant, but relevant, variables. 

---
## Section 2 Variable ranking

- Variable ranking as a principal or auxiliary selection mechanism because its simplicity, scalability and good empirical success. 
	- Several papers in this issue use variable ranking as a baseline method (see, e.g., Bekkerman et al., 2003, Caruana and de Sa, 2003, Forman, 2003, Weston et al., 2003). 
- Variable ranking is not necessarily used to build predictors. 
- A ranking criterion is used to find genes that discriminate between healthy and disease patients; such genes may code for “drugable” proteins, or proteins that may hemselves be used as drugs.


- Principle of the method and notation

- Correlation criteria

- Single variable classifier

- Information theoretic ranking criteria

---
## Small but revealing example

- Outline the usefulness and the limitations of variable ranking techniques and present several situations in hwich the variable dependencies cannot be ignored. 
 

- Q1: Can presumably redundant variables help each other?
	- "Information gain" from presumably redundant variable
		- Noise reduction and consequently batter class separation may be obtained by adding variables that are presumably redundant.
		- Redundant variable, such as rotating the histogram, would probably provides a better separation of two classes. The SD of two variables is the same, but the center of two classes is bigger. 

![[Pasted image 20221005180810.png]]



- Q2: How does correlation impact variable redundancy?
	- Perfectly correlated variables are redundant in the sense that no additional information is gained by adding them.

![[Pasted image 20221005180917.png]]




- Q3: Can a variable that is "useless by itself" be useful with other?
	- One concern about multivariate methods is that they are prone to overfitting. 
	- Still one may wonder whether one could potentially lose some valuable variables through that filtering process.
	- What is "useless" data by itself?
		- 




---
## Variable subset selection

- the usefulness of selecting subsets of variables that together have good predictive power, as opposed to ranking variables according to their individual predictive power. 


- Wrappers and embedded methods 

- They seem to be a 'brute force' method requiring massive amounts of computation, but it is not necessarily so. 
- Efficient [[Search algorithm|search strategy]] may be devised. Using such strategies does not necessarily mean sacrificing prediction performance.  coarse search strategies may alleviate the problem of overfitting, as illustrated for instance in this issue by the work of Reunanen
	- Greedy search starategies:
		- forward selection: variables are progressively incorporated into larger and larger subsets. 
		- backward elimination: one starts with the set of all variables and progressively eliminates the least promising ones.9 Both methods yield nested subsets of variables

- But, how to select subsets of variables?
	- [[Wrapper]]: 
	- [[Filter]]
	- [[Embedded]]

- Wrapper and embedded methods
- Nested subset methods
- Direct Objective Optimization
- Filters for Subset Selection


---
## Feature construction and space dimensionality reduction

- Clustering
- Matrix factorization
- Supervised feature selection


---
## Validation methods


---
## Advanced topics and open problems

- Topics 
	- Variance of variable subset selection 
	- Variable ranking in the context of othres
	- Unsupervised variable selection 
	- Forward vs backward selection
	- The multi-class problem
	- Selection of examples
	- Inverse problems


![[Guyon,Elisseeff, 2003,  An Introduction to Variable and Feature Selection.pdf]]

