---
alias: RREF, Reduced Row-Echelon Form (RREF)
---

- In reduced row echelon form, the matrix satisfies all the conditions of row echelon form, but with additional constraints:
    
    1. The leading entry in each row is 1.
    2. All other entries in the column containing a leading 1 are zeros.
    3. The leading 1 in each row is the only nonzero entry in its column.
    4. Rows consisting entirely of zeros are at the bottom of the matrix.
- Reduced row echelon form provides a more structured and simplified version of the matrix compared to row echelon form.
    
- Reduced row echelon form is unique for a given matrix, whereas row echelon form may have multiple representations for the same matrix.

---

- Echelon form of a matrix isn't unique, which means there are infinite possible when you perform row reduction. Reducing the pivots to be 1 would create a unique answer for each matrix. 
- rows add/subtracts another rows to eliminates some components of some columns. 
- $R=rref(A)$ has all pivots = 1, with zeros above and below.
- $rref(A)$
	- All pivots are 1 in $R$ = $rref(A)$

---

- Related:
	- [[systems of linear equations]]
	- matrix operations