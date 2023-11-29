- 9-10-2022: created

- Summation is the addition of a sequence of any kinds of numbers, called addends or summands, the result is their sum or total.

---
## Properties

- The summation sign could be moved outside in some situations.
	- Related: [[kernel method#^6f9b04]]
	- $(\sum_{i=1}^n x_i z_i)(\sum_{j=1}^n x_j z_j) = \sum_{i=1}^n \sum_{j=1}^n (x_i x_j) (z_i z_j)$
	- To prove for n = k , we need to use mathematical induction.
	- Easiest case: n = 2:
		- LHS: $(x_1z_1 + x_2z_2)(x_1 z_1 + x_2 z_2)$
		- = $(x_1z_1)^2 + (x_2z_2)^2 + 2(x_1z_1)(x_2z_2)$
		- RHS: $\sum_{i=1}^n \sum_{j=1}^n (x_i x_j) (z_i z_j)$
		- = $\sum_{j=1}^n (x_1 x_j) (z_1 z_j) + \sum_{j=1}^n (x_2 x_j) (z_2 z_j)$
		- = $(x_1 x_1) (z_1 z_1) + (x_1 x_2) (z_1 z_2) + (x_2 x_1) (z_2 z_1) + (x_2 x_2) (z_2 z_2)$
		- = $(x_1z_1)^2 + 2(x_1z_1)(x_2z_2) + (x_2z_2)^2$
		- = LHS