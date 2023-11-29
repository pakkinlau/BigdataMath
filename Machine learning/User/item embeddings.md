- Example of embeddings:
	- [[collaborative filtering]]: 1M movies that 500k users have chosen to watch. Task: [[recommender system]] : movies to users. 
		- To solve this problem we need to determine which movies are [[similarity|similar]] to each others. 
		- eg: 1 dimensional "movie" embedding: `Shrek, Incredibles, The triplets, Harry potter, Star wars, Bleu, The dark knight rises, Memento`. We could say from left to the right is sorted by "adult-like" score. 
		- eg: 2 dimensional "movie", adding "blockbuster -- art house" movie axis. 
		- eg: In reality, we could have 50, even 100 dimensions to sort of do these embeddings. 
		- The goal of training an embedding is to locate similar items in the [[embedding space]]

![[Pasted image 20221023173442.png]]
- Fig: (R2)
	- Input representation for "movie" data. These table like data is a "class" input representation for [[collaborative filtering]] problem. Those are [[Sparse]], if there is a half-million movies, I don't really wnt to list all the movies you haven't watched. And when we do [[Backpropagation]], I will also compute [[dot product]] that depends on the movies you have watched. 
	- To achieve this, we use adjacent list (1,3,999999), instead of adjacent matrix. 
		- Pre-processing: we build a dictionary. 
![[Pasted image 20221023173042.png|700x400]]
- Fig: sales
	- [[regression]] problem
	- sets of ad words, we need to understand those words. 
![[Pasted image 20221023173300.png|700x400]]
- Fig: (R2)
	- [[Deep|deep neural network]] with [[Multimodality]] quality. (
	- Input: raw bitmap (blue)
	- Hidden layer: (3 dimension, we can visualize it?)
	- Logit layer?: 
		- have 10 digits, learn a probability distribution over the digits of how probable we think it is that this is each of the digits. 
		- We can take one hot target probability distribution from what I know the right answer is , and optimize a softmax loss. 