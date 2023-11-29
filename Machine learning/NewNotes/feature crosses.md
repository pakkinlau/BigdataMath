---
category:[]
alias:[synthetic feature]
tags:[]
---

- 23-10-2022 21:51: created
- What is feature crosses
	- The process of creating synthetic features as products of other features we call feature crosses, or feature [[cross product]].
- eg: template: `[A x B]`
	- when A and B represent boolean [[feature]], such as bins, the resulting crosses can be extremely [[Sparse]]
- eg: `[A x B x C x D x E]`
- Why we use feature crosses?
	- 1. Linear learners use linear models. Using feature crosses + massive data is one efficient strategy for learning highly complex [[model]]
- [[Foreshadowing]]

![[Pasted image 20221023215131.png]]
- Fig: (R1)
	- There is no way to fit a line $y = w_1x_1 + w_2x_2 + b$ to this data
	- we can try to make a new kind of feature $x_3 = x_1x_2$ 
	- This allow us to learn non-linearity within linear model. 

----
- Examples: (R1)
	- Housing market price: `[latitude x num_bedrooms]`
	- Tie-tac-toe predictor: `[pos1 x pos2 x ... x pos9]`



---
## Reference

1. [[(Course) google developers - machine learning courses]]