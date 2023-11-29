   - **L1 Regularization (Lasso):** 
	   - In linear algebra, L1 regularization adds the absolute values of the coefficients as a penalty term to the objective function. This encourages sparsity in the solution, effectively setting some coefficients to zero.
	   - Which adds an absolute value of magnitude of coefficient as penalty term to the loss function
	   - $\lambda_2 ||x||_1$
	   - The L1 regularization has the effect of pushing some coefficients towards exactly zero, which can lead to sparse solutions where some features are completely ignored by the model. This can be desirable if we believe that only a subset of the features are relevant, or if we are concerned about multicollinearity.
- Example of L1 norm application:
	- It is just the sum of distance walking in Manhatten. 



# Differences between L1 and L2 Regularization

- [[Sparse|sparsity]]: L1 regularization can lead to sparse solutions where some features are completely ignored, while L2 regularization only shrinks the coefficients towards zero.

- **Resistance to Outliers**: L1 regularization is more robust to outliers than L2 regularization, as it does not heavily penalize large errors as much as L2.

- **Computation**: L1 regularization has the property of producing a solution that is not differentiable at zero. This can make it more difficult to optimize than L2 regularization. L2 regularization, on the other hand, is always differentiable which makes it easier to compute.

- **Feature Selection**: L1 regularization can be seen as a method for feature selection, because it can set some coefficients exactly to zero. L2 regularization doesn’t have this property and therefore is not used for feature selection.

In practice, which type of regularization to use (if any) will depend on the specific details of your problem. Sometimes, a combination of both, known as Elastic Net regularization, is used.