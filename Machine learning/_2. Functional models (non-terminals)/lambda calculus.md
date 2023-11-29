- 1-10-2022: created


- Church's thesis -- Any function that we intuitvely think is computable is actually definable in the lambda calculus. 


- Introduced by Church in 1930s, in his study of the foundations of mathematics and computation.  (R1)

- It provides a formalization of the notion of a "computable by computer" function. Inspired by functional programming languages. Or other programming language's anonymouns lambda functinon  (R1)
	- Other ways of defining computable functions (R1)
		- Partial recursive functions (Godel, Kleene), 
		- Turing machines (Turing)
		- Symbol manipulation (Post, Markov)
		- Register machines ( Shepherdson, Sturgis)
	- All of these different approaches yield the same class of computable functions  (R1)

- The grammer of lambda calculus:
	- Each lambda expression functions consist of two parts 
		- 1. The part that specify which are the inputs: eg: $\lambda x$ 
		- 2. The dot separator 
		- 3. The part that specifeis the operations of the function eg$x**2+2*x+1$.
	- eg: 
		- Function: $f(x) = x^2 + 2x +1$ 
		- Lamhda expression:  $(\lambda x.x  **2 + 2*x+1)$ 



- In lamdba-calculus, all values have types. 
	- eg: 3 has type int, written as 3: Int
	- eg: a function returning the length of a string has type $Str \rightarrow Int$. Where Str is `[Char]`, which `[]` is a type constructor, which a list of char type element, it returns a str element.

- Subtype relations
  - If A is a subtype of B, we write  $A \leq B$ or ( $B \geq A$).
  - There is an arrow in between A and B if and only if there is a subtype relation between them. 
  - eg: Int is a subtype of num, so $Int \leq Num$.

- Lambda calculus composition of function
  - $f: A \rightarrow B$ and $g: B \rightarrow C$, then 
	  - $g \circ f = (\lambda x. g(fx)), x:A$. (latter phrase means it only takes type A as x)
	  - $1_A = (\lambda x.x),  x: A$


--
## Reference

1. [[(Video) Blargoner 2020, Category theory, 3 parts series]]