---
alias: solving systems of linear equations, systems of linear equation
---

### systems of linear equations


---
### solving systems of linear equations

**Overview:**
Solving systems of linear equations is a fundamental concept in linear algebra, which is a branch of mathematics that deals with vector spaces, linear transformations, and their properties. Linear equations represent relationships between variables in a linear fashion, and solving systems of such equations involves finding values for the variables that satisfy all the equations simultaneously.

**Key Elements:**

1. **Linear Equations:** Linear equations are mathematical expressions where each term is either a constant or a constant multiplied by a variable raised to the power of 1. They can be written in the form:

   $$a_1x_1 + a_2x_2 + \ldots + a_nx_n = b$$

   Here, $x_1, x_2, \ldots, x_n$ are variables, $a_1, a_2, \ldots, a_n$ are coefficients, and $b$ is a constant.

2. **System of Linear Equations:** A system of linear equations consists of multiple linear equations with the same set of variables. The goal is to find values for these variables that satisfy all the equations simultaneously.

   Example:
   $$\[
   \begin{align*}
   2x + 3y &= 8 \\
   4x - 2y &= 6
   \end{align*}
   \]$$

3. **Matrix Representation:** Systems of linear equations can be represented using matrices and vectors. The coefficient matrix ($A$), variable vector ($X$), and constant vector ($B$) are used to rewrite the system in matrix form: $AX = B$.

   Example:
   $$\[
   \begin{bmatrix}
   2 & 3 \\
   4 & -2
   \end{bmatrix}
   \begin{bmatrix}
   x \\
   y
   \end{bmatrix}
   =
   \begin{bmatrix}
   8 \\
   6
   \end{bmatrix}
   \]$$

4. **Methods of Solving:**
   - **Gaussian Elimination:** This method involves transforming the coefficient matrix into row-echelon form through a series of row operations, ultimately leading to a solution.
   - **Matrix Inversion:** When the coefficient matrix is invertible, you can find the solution by multiplying both sides of the matrix equation $AX = B$ by the inverse of $A$, i.e., $X = A^{-1}B$.
   - **Cramer's Rule:** This method provides explicit formulas for each variable in terms of determinants, applicable when the coefficient matrix is square and its determinant is non-zero.

5. **Existence and Uniqueness of Solutions:**
- A system can have:
	 - A unique solution if and only if the coefficient matrix is square and has full [[rank]] (i.e., all rows and columns are [[Linear independence|linearly independent]]).
	 - No solution if it's inconsistent (i.e., equations contradict each other).
	 - Infinitely many solutions if it's underdetermined (i.e., there are more variables than equations).

1. **Applications:** Solving systems of linear equations has numerous applications in various fields, including physics, engineering, economics, computer graphics, and more. It is used to model and analyze real-world problems involving linear relationships.

**Conclusion:**
Solving systems of linear equations is a fundamental skill in linear algebra that provides a powerful tool for understanding and solving real-world problems. It involves transforming a system of linear equations into a more manageable form, whether through matrix operations, elimination techniques, or specialized methods, ultimately leading to solutions that have wide-ranging applications in diverse fields.


---
# Determining the number of solutions when solving systems of linear equations

**Title: Understanding Solutions to Systems of Linear Equations**

**Concept**: When solving systems of linear equations, determine whether a system of linear equations has a unique solution, infinitely many solutions, or no solution at all.

**Context**: Linear Algebra

**Notes**:

1. **Introduction to Systems of Linear Equations**:
   - In linear algebra, systems of linear equations are fundamental mathematical tools used to describe real-world scenarios.
   - A system of linear equations consists of multiple linear equations involving the same set of variables.

2. **Solution Types**:
   - When solving a system of linear equations, we encounter three possible outcomes:
     1. **Unique Solution**:
        - A system of linear equations has a unique solution when there is only one set of values for the variables that satisfies all the equations simultaneously.
        - Geometrically, this corresponds to the intersection point of lines (in 2D) or the intersection of planes (in 3D) formed by the equations.
     2. **Infinitely Many Solutions**:
        - Infinitely many solutions occur when there are multiple sets of values for the variables that satisfy all the equations.
        - Geometrically, this corresponds to overlapping lines (in 2D) or overlapping planes (in 3D) formed by the equations.
     3. **No Solution**:
        - A system of linear equations has no solution when there are contradictory equations that cannot be satisfied simultaneously.
        - Geometrically, this corresponds to parallel lines (in 2D) or parallel planes (in 3D) formed by the equations, which never intersect.

3. **Methods for Determining Solutions**:
   - There are various methods for determining the nature of solutions to systems of linear equations, including:
     - **Gaussian Elimination**: This method involves row operations to transform the system into row-echelon form or reduced row-echelon form. The result can indicate the type of solution.
     - **Matrix Notation**: Expressing the system as a matrix equation (Ax = b) and then performing matrix operations to determine the solution or lack thereof.
     - **Graphical Representation**: In 2D or 3D, you can graphically represent the equations and observe the intersection behavior.

4. **Examples**:
   - Consider the following examples:
     1. Unique Solution:  
        - 2x + 3y = 7
        - 4x - y = 5
        - This system has a unique solution.
     2. Infinitely Many Solutions:  
        - x + 2y = 4
        - 2x + 4y = 8
        - This system has infinitely many solutions.
     3. No Solution:  
        - 3x + 2y = 5
        - 6x + 4y = 9
        - This system has no solution.

5. **Importance**:
   - Understanding the nature of solutions to linear equations is crucial in various fields, including physics, engineering, economics, and computer science.
   - It forms the basis for solving problems involving optimization, consistency, and feasibility.

6. **Conclusion**:
   - Determining whether a system of linear equations has a unique solution, infinitely many solutions, or no solution is a fundamental skill in linear algebra. It enables us to model and analyze real-world problems effectively and make informed decisions based on the mathematical outcomes.