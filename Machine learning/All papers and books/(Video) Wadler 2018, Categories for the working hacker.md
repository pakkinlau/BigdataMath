- 29-9-2022: created

- Views
	- Math is your friend. Stuck on math, and then things will slowly becomes easier. It illuminates (2:00)
- What is Categories
	- 1. logic (ancient greek, 1935) 
	- 2. programming (first defined as lambda calculus by Alonzo Church in 1932) --> Turns out logical inconsistency, so come up with "Types". --> Consistent programming with types, in 1940. 
	- Robert Howard: 1 & 2 are the same thing! It took 40 years to see that. 
	- And categories are actually the third thing that is the same as 1 and 2. You can use categories to model logic, use categories to model lambda calculus. 
- 6:00
![[Pasted image 20220929110041.png]]
Red: arrows
A: set  / algebra / groups / object

- With this structure: you can specify enormous amount. Really?
	- How can you get something meaningful out of something trival?


![[Pasted image 20220929110330.png]]
- associative law: V
---

- Most important structure in programming + connectives in logic
	- Logic:
		- conjunction (and) and disjunction (or) ?
	- Products
		- It is another name for logical conjunction and also "record type", "pair type". 

![[Pasted image 20220929110707.png]]
- 1. You have two ways to get to A from C, either: by f, or by (f,g) then (gst). That composition is just equal to doing a single f. No matter how you get there, it's the same function. 
	- This diagram is fixed for all above mentioned 3 kinds of domain (logic, math, programming)
- 2. In computing, A is a type of some data structure, like string, B is another, like strings, then this would be a record with two fields, one field called first, another called second. Then I get integer and also string from C. I just apply those to plunk them together, so I can build a pair, consisting of integer and string. 
- 3. In logic, that is "implication". That would be f is a proof that from C you can derive A, from C you can prove B, then there is a prof C --> A x B (that's equivalent to A $\land$ B in logic, which means both A and B is true. )


![[Pasted image 20220929112923.png]]
- Why we call them "product"?
	- say A has 3 elements, B has 2 elements, and then if we combine the data type, then there is 6 possible forms, so A X B has 6 elements in total. 
		- In computing, that make sense. 
		- In logic, ???

![[Pasted image 20220929113206.png]]
- $\mathscr{C}(C, A \times B) \cong\mathscr{C}(C,A) \times \mathscr{C}(C,B)$: 
	- Curly C means "the set of all possible arrows from "C" to "$A \times B$". 
	- $\cong$ means isomorphism, that means LHS and RHS are the same thing. 
	- THis formula tells us "the only way to get to $A \times B$ is to have two function, one is C to A, another is C to B. "
	- That is the part of the way to get there, that is "all of them". That is the nice property that it bring us. 
	- This is a nice way to summarize the categorical diagram. 

![[Pasted image 20220929114850.png]]
![[Pasted image 20220929114930.png]]
![[Pasted image 20220929114940.png]]
- Products in Java
	- In Haskell you can build any kind of "product" you want 

---
The second datatype: sum

- A bit less familiar
- Disjoint union = sum

- Option type = sum

![[Pasted image 20220929115222.png]]
- Diagram
	- If I have f: A -> C,  and g: B-> C, then, there is an unique arrow from A+B to C. 
	- Commute: So if we have  (f: A -> C),  and (g: B-> C), then it commutes we have ((f,g): A+B -> C )
	- That commute is what category care about. Avoiding traffic jams. 
	- What is A+B. 
	- left ; (f,g) $\cong$ f
	- right ; (f,g) $\cong$ g
- Logic:
	- Sum = logical or  = disjunction connector
	- (a) We have left: A-> A+B, and right: B-> A+B
	- (b) If we have f: A->C and g: B->C, then we have (f,g) A+B -> C (In layman's word, if we have either A or B stands true, then A or B is true, it is standard logic.) (That's the definition of OR)
	- (c) left ; (f,g) $\cong$ f ;  right ; (f,g) ≅ g
- Data structure
	- Either type A or type B (int or string, for example)
	- eg: left = is a string, right = is a integer
- Why it is called "sum"
	- Totally A+B possible outcomes. 
- "Disjoint union"
	- That means either one or the other, it won't be both of them. 
	- It won't be int + str. 

---
![[Pasted image 20220929124013.png]]
![[Pasted image 20220929124200.png]]
-


![[Pasted image 20220929124503.png]]
- Dual: Put two image as a pair, and reverse the direction of all arrows. 

---
Isomorphisms

![[Pasted image 20220929125516.png]]
![[Pasted image 20220929125600.png]]
- You learned that in high school. 