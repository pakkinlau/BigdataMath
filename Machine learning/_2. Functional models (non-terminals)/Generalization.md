- 26-9-2022: created

- Related: 
	- [[discrimination]]

- What is generalization?
	- Generalization refers to your [[model]]'s ability to adapt property to new, previously unseen [[Data|data]], drawn from the same distribution as the one used to create the model. (R2)

- How do we know if our model is good?
	- Theoretically: 
		- interesting field - [[generalization theory]]
		- Based on ideas of measuring model simplicity / complexity
	- Intuition: 
		- Formulization of (Ockham's razor) (R2)
		- 14th century -- William of Ockham Ockham's razor - "a model should be as simple as possible". (R2)
		- Based on ideas of measuring model simplicity / complexity (R2)

---

- Empirically: (R2)
	- Will our model do well on a new sample of data?
	- [[evaluate]]: get a new sample of data-call it the test set
	- Good [[performance]] on the test set is a useful indicator of good [[performance]] on the new data in general:
		- If the test set is large enough
		- If we don't cheat by using the test set over and over


![[Pasted image 20221007074433.png|200x200]]![[Pasted image 20221007074445.png|200x200]]
- Figure: (R2) we do a "perfect" fitting on training data, but might be perform badly on "test" data.

![[Pasted image 20221023211350.png|400x300]]

- [[machine learning]] fine print, the critical assumption : (R2)
	- 1. We draw examples independently and identically distributed ([[identical and independently distributed|i.i.d.]]) at random from the distribution. We are not biasing oursevles in any way.
	- 2. The distribution is stationary: It doesn't change over time. 
	- 3. We always pull from the same distribution: Including training, validation, and test sets

- But sometimes we violate them.  (R2) 
	- eg: assumption 2 --> The consumer behavior changes over the holiday season.  (R2)
	- eg: assumption 3 --> If people suddenly decide a different breed of puppies is as cute as they saw before.  (R2)

- Generalization bounds (R2)
	- Model's ability to generalize to new data based on:
		1. complexity of the model  (R2)
		2. the model's [[performance]] on training data. (R2)


- Generalization = their performances on unseen test examples. (R1)
	- Recall: dataset $\{(x^{(i)}, y^{(i)} )\}_{i=1}^n$, we learn a mode; $h_\theta$ by minimizing lost/cost function $J(\theta)$, which encourages the model to fit the data. THis loss fucntion for training purpose is referred to as the training loss/error/cost. 
	- Even training set and test dataset are both drawn from the same distribution $D$, the test error is not necessarily always close to the training error.

- The loss function encourages the model to fit the data, thus reduce the "training loss/error/cost". (R1)
	- Training loss/error/cost: $J(\theta)= {1\over n} {\sum_{i=1}^n(y^{(i)}-h_\theta(x^{(i)}))^2}$
- After obtaining a trained model, we tsample $(x,y)$ from test distribution $D$, and measure the model's error on it, eg, by mean sqaured error.  (R1)
	- Testing loss/error/cost: $L(\theta)=E_{(x,y)\sim D}[(y-h_\theta(x))^2]$.


---


- 8.1 Bias variance tradeoff  (R1)
	- 8.1.1 A mathematical decomposition (for regression)

![[Pasted image 20221007080526.png]]
- Figure: (R1) The model suffers from high [[bias]] even if we fit it to a very large traning dataset. 

![[Pasted image 20221007080714.png]]
- Figure: (R1): The model on three different datasets generated from the same distribution behave quite differently, suggesting the existence of a large [[variance]]. 


![[Pasted image 20221007081220.png]]
- Figure: (R1) If our model is too simple, there may have large bias, and it typically may suffer from [[underfitting]]. And if the model is too complex, and has very many parameters, then it may suffer from large vaiance. 


- 8.2 The double descent phenomenon


---
## Reference:
1. [[(Course) CS229 Machine learning]]
2. [[(Course) google developers - machine learning courses]] https://developers.google.com/machine-learning/crash-course/generalization/video-lecture