In the context of matrix approximation, cumulative energy refers to the amount of information retained or captured by a reduced-rank approximation of a matrix. 

When you perform matrix approximation techniques such as Singular Value Decomposition (SVD) or Principal Component Analysis (PCA), you decompose a matrix into lower-dimensional representations. In the case of SVD, for example, a matrix $A$ is approximated as the product of three matrices $U$, $\Sigma$, and $V^T$ (transpose of $V$). Here, $U$ and $V$ are orthogonal matrices, and $\Sigma$ is a diagonal matrix containing singular values.

When you reduce the rank of the matrix by keeping only the top $k$ singular values (and their corresponding columns in $U$ and $V$), you create a low-rank approximation of the original matrix. The cumulative energy in this context refers to the sum of squares of the retained singular values divided by the total sum of squares of all singular values. Mathematically, it can be expressed as:$$
\text{Cumulative Energy} = \frac{\sum_{i=1}^{k} \sigma_i^2}{\sum_{i=1}^{n} \sigma_i^2}$$

Where $\sigma_i$ represents the $i$th singular value, $k$ is the number of singular values retained, and $n$ is the total number of singular values in the original matrix. 

This cumulative energy value indicates the proportion of total energy (or information) retained by the reduced-rank approximation. A higher cumulative energy signifies that a larger portion of the original matrix's information is preserved in the approximation. The choice of $k$ (the number of singular values retained) depends on how much energy (or information) you want to retain in the approximation. Higher values of $k$ result in a more accurate approximation but require more memory and computational resources.