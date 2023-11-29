---
alias: []
---

- 5-10-2022: created

- Feature selection is also called variable selection or attribute selection. (R1)
- It is the automatic selection of attributes in your data (such as columns in tabular data) that are most relevant to the predictive modeling problem you are working on. (R1)
- feature selection… is the process of selecting a subset of relevant features for use in model construction (wiki)

---
- The problem that feature selection solves

- Feature selection methods aid you in your mission to create an accurate predictive model. They help you by choosing features that will give you as good or better accuracy whilst requiring less data.
- Feature selection methods can be used to identify and remove unneeded, irrelevant and redundant attributes from data that do not contribute to the accuracy of a predictive model or may in fact decrease the accuracy of the model.
- Fewer attributes is desirable because it reduces the complexity of the model, and a simpler model is simpler to understand and explain.
- The objective of variable selection is three-fold: improving the prediction [[performance]] of the predictors, providing faster and more cost-effective predictors, and providing a better understanding of the underlying process that generated the data. 



---
- Algorithms
	- [[Filter]]: 
		- Apply a statistical measure to assign a scoring to each feature. the features are ranked by the score and either selected to be kept or removed from the dataset.  (R1)
		- Some examples of some filter methods include the Chi squared test, information gain and correlation coefficient scores. (R1)
	- [[Wrapper]]: 
		- Consider the selection of a set of features as a search problem, where different combinations are prepared, evaluated and compared to other combinations. A predictive model is used to evaluate a combination of features and assign a score based on model accuracy. (R1)
		- The search process may be methodical such as a best-first search, it may stochastic such as a random hill-climbing algorithm, or it may use heuristics, like forward and backward passes to add and remove features. (R1)
	- [[Embedded]]
		- Embedded methods learn which features best contribute to the accuracy of the model while the model is being created. The most common type of embedded feature selection methods are regularization methods. (R1)
		- Regularization methods are also called penalization methods that introduce additional constraints into the optimization of a predictive algorithm (such as a regression algorithm) that bias the model toward lower complexity (fewer coefficients). (R1)



---
## Reference
1. Brownlee's blog: https://machinelearningmastery.com/dimensionality-reduction-for-machine-learning/
2. [[(Paper) 2003  18500 citation, Guyon and Elisseeff, An introduction to Variable and feature selection]]