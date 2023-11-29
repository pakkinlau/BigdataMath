- weighted p-norm
	- $||x||_w = ||Wx||$, where $W$ can be any non-singular matrix.
---

p-norm revisited

In mathematics, a **p-norm** is a way of measuring the size or length of a mathematical object, such as a vector. In the context of vectors, the p-norm of a vector $x$ in $\mathbb{R}^n$ is defined as:$$ \|x\|_p = \left( |x_1|^p + |x_2|^p + \ldots + |x_n|^p \right)^{\frac{1}{p}}$$
where $x = (x_1, x_2, \ldots, x_n)$ is a vector in $\mathbb{R}^n$, $p$ is a real number greater than or equal to 1, and $|\cdot|$ represents the absolute value.

---
weighted p-norm

When each entry in the vector is multiplied by a corresponding positive weight, you get a **weighted p-norm**, denoted as $\|x\|_{p,w}$, where $w = (w_1, w_2, \ldots, w_n)$ is a vector of positive weights. The weighted p-norm of the vector $x$ is defined as:$$ \|x\|_{p,w} = \left( |w_1 \cdot x_1|^p + |w_2 \cdot x_2|^p + \ldots + |w_n \cdot x_n|^p \right)^{\frac{1}{p}} = \left( \sum_{i=1}^{n} w_i |x_i|^p \right)^{\frac{1}{p}}$$$$ \|x\|_{p,w} = ( |w_1 \cdot x_1|^p + |w_2 \cdot x_2|^p + \ldots + |w_n \cdot x_n|^p )^{\frac{1}{p}} = \left( \sum_{i=1}^{n} w_i |x_i|^p \right)^{\frac{1}{p}}$$
Weighted p-norms are useful in various areas, including statistics, signal processing, and machine learning, where different components of a data vector might have different importance or relevance. By assigning appropriate weights to the components, you can emphasize or de-emphasize certain parts of the data when calculating the norm. Different choices of $p$ and $w$ can lead to different properties of the norm and can be useful in different applications.

---
Is weighted p-norms a vector norm?

To prove that the function $|| \cdot ||_W$ defined as the weighted $p$-norm on a nonsingular matrix $W$ is a vector norm, we need to show that it satisfies the following properties for any vectors $x$ and $y$, and any scalar $\alpha$:

1. **Non-negativity:** $||x||_W \geq 0$, and $||x||_W = 0$ if and only if $x = 0$.
2. **Homogeneity:** $||\alpha x||_W = |\alpha| \cdot ||x||_W$.
3. **Triangle Inequality:** $||x + y||_W \leq ||x||_W + ||y||_W$.

Let's prove each property one by one:

**1. Non-negativity:**
- $||x||_W = \sqrt[p]{(x^T W^T W x)}$ (definition of weighted $p$-norm)
- $x^T W^T W x$ is a quadratic form. Since $W$ is nonsingular, $W^T W$ is positive definite, meaning $x^T W^T W x$ is always non-negative.
- $||x||_W = 0$ if and only if $x^T W^T W x = 0$. But for a nonsingular matrix $W$, $x = 0$ is the only solution to this equation, proving non-negativity.

**2. Homogeneity:**
- $||\alpha x||_W = \sqrt[p]{(\alpha x)^T W^T W (\alpha x)}$
- $||\alpha x||_W = \sqrt[p]{\alpha^p (x^T W^T W x)}$
- $||\alpha x||_W = |\alpha| \sqrt[p]{(x^T W^T W x)} = |\alpha| \cdot ||x||_W$.

**3. Triangle Inequality:**
- $||x + y||_W = \sqrt[p]{(x^T + y^T) W^T W (x + y)}$
- $||x + y||_W = \sqrt[p]{(x^T W^T W x) + 2 (x^T W^T W y) + (y^T W^T W y)}$
- By the Cauchy-Schwarz inequality, $2 |x^T W^T W y| \leq \sqrt{(x^T W^T W x)(y^T W^T W y)}$
- $||x + y||_W \leq \sqrt[p]{(x^T W^T W x) + 2 \sqrt{(x^T W^T W x)(y^T W^T W y)} + (y^T W^T W y)}$
- $||x + y||_W \leq \sqrt[p]{(x^T W^T W x) + 2 \sqrt{(x^T W^T W x)(y^T W^T W y)} + (y^T W^T W y)}$
- $||x + y||_W \leq \sqrt[p]{((x^T W^T W x) + (y^T W^T W y))^p} = ||x||_W + ||y||_W$.

Therefore, $|| \cdot ||_W$ satisfies all the properties of a vector norm, making it a valid weighted $p$-norm on the nonsingular matrix $W$.