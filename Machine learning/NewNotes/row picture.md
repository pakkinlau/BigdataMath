- Context:
	- Understanding [[systems of linear equations]]

- Related:
	- [[column picture]]
	- [[row space]]

- Definition:
	- The row picture is one of the three primary ways to visualize and comprehend these concepts, alongside the column picture and the augmented matrix. Say we have [[systems of linear equations|systems of linear equation]] $Ax = b$, which asks for a combination of columns to produce $b$. 
	- The row picture, also known as the geometric interpretation or geometric view, is a graphical representation of a system of linear equations. It focuses on the relationship between equations, variables, and solutions in terms of vectors and their geometric properties.
		- Each equation gives a line ($n = 2$), or a plane ($n = 3$) or a hyperplane ($n > 3$). They intersect at the solution or solutions, if any. 

- Key points:
	- Row vectors:
		- In the row picture, each linear equation is represented as a vector, and the coefficients of the variables determine the direction and magnitude of these vectors. 
		- For instance, in a 2D system of equations like ax + by = c, the equation can be viewed as a vector `[a, b]` pointing in a certain direction in the xy-plane.
		- To be concrete, say we have 2 equations: 
			- $2x - y = 0$, $-x + 2y = 3$. 
		- To represent these equations in the row picture, we can rewrite them in slope-intercept form $y = mx + b$, where $m$ is the slope and $b$ is the y-intercept. 
			- $y = 2x$, $y = 0.5x + 1.5$
		- Consider 2 equation seperately, 
			- The first equation corresponds to a line with a slope of 2 and passing through the origin.
			- THe second equation corresponds to a line with a slope of 0.5 and y-intercept of 1.5.
	- Vector Intersection: 
		- The solution to a system of linear equations is the point where these vector representations intersect or come together. In 2D, this intersection corresponds to the point of intersection of two lines. In 3D, it would be the intersection of three planes, and so on.
	- Consistency and Inconsistency: 
		- The row picture provides a clear visualization of whether a system has a unique solution (consistent), infinitely many solutions (dependent), or no solution (inconsistent). Inconsistent systems are depicted when the vectors representing equations do not intersect.
	- Applications: 
		- The row picture is particularly useful when dealing with small systems of equations in lower dimensions (2D or 3D) and for grasping the geometric intuition behind linear algebra concepts. It is often employed in introductory linear algebra courses to help students visualize the solutions to linear systems.
---
Let's demonstrate how to use the row picture to interpret a simple linear algebra problem. Consider the following system of two linear equations in two variables, x and y:

1. \(2x + y = 3\)
2. \(x - 2y = 2\)

---
### Strang's way

- Source:
	- https://youtu.be/J7DzL2_Na80?si=DIUdsMyGPIzLlvLi&t=507

$2x - y = 0$
$-x +2y = 3$
$Ax = y$

- Row picture:
	- 1. Establish the systems of equations to be represented in $Ax = y$
	- 2. Making each row of the equation to be a line
	- 3. Find intersections of lines.
![[Pasted image 20230912001801.png]]

---

We'll use the row picture to visualize and solve this system geometrically:


**Step 1: Represent Equations as Vectors**

We represent each equation as a vector. The coefficients of x and y determine the direction and magnitude of these vectors.

For the first equation, \(2x + y = 3\), we can represent it as the vector \(\mathbf{V}_1 = [2, 1]\), which points in the direction [2, 1] in the xy-plane.

For the second equation, \(x - 2y = 2\), we represent it as the vector \(\mathbf{V}_2 = [1, -2]\), which points in the direction [1, -2].

**Step 2: Visualize the Vectors**

Now, let's plot these vectors in the xy-plane:

- Vector $\mathbf{V}_1$ starts at the origin (0, 0) and goes 2 units to the right (in the x-direction) and 1 unit up (in the y-direction).
- Vector $\mathbf{V}_2$ starts at the origin (0, 0) and goes 1 unit to the right (in the x-direction) and 2 units down (in the y-direction).

Your xy-plane should now have two vectors that look like this:

```
       |
       |
       |
       |
-----> V1 (2, 1)
  |
  |
  |
  |
  V2 (1, -2)
  |
  |
```

**Step 3: Find the Intersection Point**

The solution to the system of equations corresponds to the point where these vectors intersect. In this case, it's the point where \(\mathbf{V}_1\) and \(\mathbf{V}_2\) cross paths.

To find this point, simply follow both vectors until they meet. In this example, you'll see that they intersect at the point (1, 1):

```
       |
       |
       |
       |
-----> V1 (2, 1)
  |   /
  |  /
  | / 
  |/  
  x (1, 1)
  |\
  | \
  |  \
  |   \
  V2 (1, -2)
```

**Step 4: Interpretation**

The point (1, 1) is the solution to the system of equations:

1. \(2x + y = 3\)
2. \(x - 2y = 2\)

You can verify this by substituting x = 1 and y = 1 into both equations:

1. \(2(1) + 1 = 3\) (True)
2. \(1 - 2(1) = 2\) (True)

So, using the row picture, we have visually determined that the solution to this system of equations is x = 1 and y = 1, which is the point (1, 1) on the xy-plane where the two vectors intersect.


---

## Strang's lecture

- $m$ equations from $m$ rows give $m$ planes meeting at $x$. 
- $m$ equations from $m$ rows give $m$ planes meeting at $x$. A dot product gives the equation of each plane. (each plane is like: ax + by + ... = z).
- The row picture shows m lines meeting at a single point (the solution)
![[Pasted image 20221227120956.png|400]]![[Pasted image 20221227140450.png|400]]
- Fig: row picture

![[Pasted image 20221225235455.png|400]]
- Fig: Row picture
	- 1 plane is all the way that solve 1 row in that dimension.
	- 1 equations with 3 variables, we can get a plane.  
	- 2 equations with 3 variables, we can get a line.  
	- 3 equations with 3 variables, we can get a dot.  
	- We usually want a dot. 