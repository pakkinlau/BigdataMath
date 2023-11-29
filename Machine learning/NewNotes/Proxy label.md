---
category: []
alias: []
tags :[]
---

- 24-10-2022 13:06: created

- Superset:
	- [[label]]

- What is Proxy label?
	- Proxy labels substitute for labels that aren't in the dataset. Proxy labels are necessary when you can't directly measure what you want to predict. 
	- But cautious with proxy labels because they don't directly measure what you want to predict.
	- eg:
		- In the video app, we can't directly measure whether or not a user will find a video `useful`. It is great if the [[Data|dataset]] had a `useful` feature, and users marked all the videos that they found useful, but because the dataset doesn't, we will need a proxy label that substitute for usefulness.

![[Pasted image 20221024131525.png]]
- Fig: issue of proxy labels
	- mostly about the representativeness. and the algorithm will be very prone to manipulations.

---
## Suggestion

- 1. Start a simple model
	- When implementing a model, start simple. Most of the work in ML is on the data side, so getting a full pipeline running for a complex model is harder than iterating on the model itself. 
	- After setting up your data pipeline and implementing a simple model that uses a few features, you can iterate on creating a better model.
	- Simple models provide a good baseline, even if you don't end up launching them. In fact, using a model is probably better than you think. 
	- Starting simple helps you determine whether or not a complex model is even justified.
- 2. Train your own model versus using a pre-trained model
	- Many pre-trained models exist for a variety of use cases and offer many advantages. However, pre-trained models only really work when the label and features match your dataset exactly. 
	- Commonly, ML practitioners use matching subsections of inputs from a pre-trained model for fine-tuning or [[transfer learning]].  



---
## Reference

1. [[(Course) google developers - machine learning courses]]