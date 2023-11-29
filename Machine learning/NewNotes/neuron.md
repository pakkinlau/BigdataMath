---
created: 09-04-2023 01:36
category: []
alias: []
tags: []
---

- What is neuron?
	- 1. NN has no idea of the relationship between X and Y. 
		- So it makes a guess. 
		- And then it uses the sets of Xs and Ys to measure how good or how bad its guess was.
		- Each guess should be better than before. 
	- 2. It is manifesting the idea of [[machine learning paradigm]], 

---
- McCulloch-Pitts Neuron (Reference 2)
	- The first computational model of a neuron was proposed by Warren MuCulloch (neuroscientist) and Walter Pitts (logician) in 1943.
	- The first part, $g$ takes an input, performs an aggregation and based on the aggregated value and based on $g(x_1, x_2, \dots, x_n)$ $f$ makes a decision.

![[Pasted image 20230418151325.png|400]]


---
- Example:
	- Getting the linearity equation, by feeding data and the end results to a neuron 

![[Pasted image 20230402192201.png|500]]
- Example:
	- Neural network:
		- The simplest neuron network, which only has one neuron.
		- `Dense`: define a layer of connected neurons.
		- `Sequential`: Successive layers are defined in sequence.
	- Running the model
		- Loss function:
			- `sgd`: stochastic gradient descent
				- Check out TensorFlow documentations for more. 
		- Optimizers: 
	- Represent the known data
		- `np.array()` makes data representation particularly enlists much easier. 
	- Training
		- `model.fit()`
	- Return result
		- `print(model.predict([10.0]))`
		- The reason is because 
```python
model = keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
model.compile(optimizer='sgd',loss='mean_squared_error')

# Our data representation
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype =float)
ys = np.array([-3.0,-1.0,1.0, 3.0, 5.0, 7.0], dtype =float)

# Training
model.fit(xs, ys, epochs=500)

print(model.predict([10.0]))
```


---
## Reference

1. [[Course 1 of 4, Introduction to TensorFlow for Artificial Intelligence, Machine Learning, and Deep Learning]]
2. https://towardsdatascience.com/mcculloch-pitts-model-5fdf65ac5dd1