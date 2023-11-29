- 6-10-2022: created
- Defuzzification is the process of producing a quantifiable result in crisp logic, given [[fuzzy set]]s and corresponding membership degrees. 
- It is typically need for [[fuzzy control system]].

- case:
	- In a control system, 3 potentil sets are "decrease pressure (15%)", Maintain Pressure (34%), Increase Pressure (72%)". Defuzzification is interpreting the membership degrees of the [[fuzzy set]] into a specific decision or real value. 

- The simplest but least useful [[defuzzification]] is to choose the ste with the highest membership, igore the others.
	- The problem with this approach is that it loses information. 

- A useful technique is center of gravity. 
	- 1. The results of the rules must be added together in some way. 

- case study:
	- eg: the most typical fuzzy set membership function has a graph of a triangle. 
	- Step 1" The first step of defuzzification typically "chops off" parts of the graphs to form trapezoids 
		- if this triangle were to be cut in a straight horizontal line somewhere between the top and the bottom, and the top portion were to be removed, the remaining portion forms a trapezoid.
		- if potential option set X has Y%, than this triangle will be cut Y% the way up from the buttom.
	- Step 2: Thee triangels will then be superimposed one upon another, forming a single geometric shape.
	- Step 3: The centroid of this shape, called the fuzzy centroid, is calculated. The x coordinate of the centroid is the defuzzified value. 

![[Pasted image 20221006113715.png]]
- figure: wiki