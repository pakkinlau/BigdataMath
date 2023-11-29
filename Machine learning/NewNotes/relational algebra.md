---
category: []
alias: []
tags: []
---

- 28-11-2022 12:21: created

- What is relational algebra? (R1)
	- Imagine we call one SQL table as a "relation".
	- A collection of operations each acting on one or two relations, and producing one relation as result.
	- Relational algebra = a language for combining those operations.
	- Rules are needed to specify the attribute names in the result of algebraic operations with two operands. 


---
- Relational schema

- My writing (28/11/2022)
	- Schema is like creating an OBJECT from a CLASS, which require us to specifies the attribute of that OBJECT. 

![[Pasted image 20221128122128.png]]
- Fig: relational schema (R1)


- Selection $\sigma$ (or restriction) on $R$ (relational database / Relation)
	- Intuition: selection is a horizontal slice of relation.
	- Operation meaning: the condition is applied to every tuple. If it is satisfied, the tuple is kept in the answer. 

$\sigma_{condition}(R) = \{r \in R | condition(r)\}$

- Simple conditions:
	- `<attr> <comparison> <attr>`
	- `<attr> <comparison> <attr>`

---
- Projection
	- Retain a subset of attribute of a relation.
	- Intuition: if we have a SQL table, projection is a vertical slice of it.
	- The result of a projection is a relation, projection involves duplicate removal.
$\pi_{attribute}(relation)$

![[Pasted image 20221128124834.png]]
- Fig: subset of attribute from a relation "Employee"


---
- Duplicate removal

![[Pasted image 20221128125916.png]]
- Fig: self-projection of a relation DNo.

- Duplicate removal can be expensive, it can be done with:
	- nested loops
	- sort/merge
	- hashing

---
- Nesting or sequencing operations
	- 

![[Pasted image 20221128132737.png]]
- Fig: R1

---

- 9 operators
- 

- 4 families
	- Unary operator: $R \rightarrow R$
	- Binary operator: $R \times R \rightarrow R$
	- Homogeneous operators: Operands and result must have the same scheme.
	- Heterogeneous operators

---
- Set theoretic operations
- 

---
## Reference

1. https://cs.ulb.ac.be/public/_media/teaching/infoh303/algnotes2p.pdf