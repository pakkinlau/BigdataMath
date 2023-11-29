- 3-10-2022: created

- https://www.youtube.com/watch?v=O5xeyoRL95U

---
## Deep learning in one slide

- What is it
	- Extract useful patterns from data
- How:
	- Neural network + [[Conventional methods]]
- How (practical):
	- Python + tensorflow and friend?
- Hard Part:
	- Good Questions + Good Data
	- Applying methodology to solve real world problems that requires data. Asking right questions of that data, organizing that data, and labeling selecting aspects of that data that can reveal the answers to the questions you ask. 
- Why now:
	- Data, hardware, community, tools, investment
- Where do we stand?
	- Most big questions of intelligence have not been answered nor properly formulated

" AI began with an ancient wish to forge the gods." - Pamela
McCorduck , Machines Who Think, 1979

![[Pasted image 20221003172243.png]]
- Figure: visualization of the brain

![[Pasted image 20221003172401.png]]
- History of machine learning tecnologies. Improved neural network each year. 

- List of deep learning ideas and milestone: 
	- Perception (1957)
	- 1974: [[Backpropagation]], [[Recurrent|RNNs]]
	- 1989: [[Convolutional]], [[MNIST]], [[LSTM]], Bidirectional RNN
	- 2006: [[Deep]]
	- 2009: [[ImageNet]]
	- 2012: [[AlexNet]]
	- 2016: [[Generative adversarial network]]
	- 2018: [[BERT]]


---

![[Pasted image 20221003172621.png]]

---
![[Pasted image 20221003172735.png]]

- Some achine learning process in one slide

---
![[Pasted image 20221003172809.png]]

- [[tensorflow]]

---

- [[Deep|deep learning]] is [[representation]]

- representation matters
- A good representation is extremely important, and effective for being able to interpret data. With different representation, the task of drawing the line becomes difficult, it requires more dimension to do it accurately. (R1)
- [[machine learning]] is forming representation that map the topology, the space that you are trying to deal with of the raw inputs, map it in such a way, trival to classify, trival to perform regression, trival to generate new samples of that data. (R1)
- representation of higher and higher levels of representation is really the dream of artificial intelligence. (R1)
- Understanding is making teh complex simple. Like Einstein back in a few slides ago.  (R1)
- That's been the dream of all the science in general, of the history of science is the history of compression progress, of forming simpler and simpler representation of ideas. (R1)

---

![[Pasted image 20221003181129.png]]
- Figure: (R1). The representation that makes the prediction difficult. 

![[Pasted image 20221003174723.png]]
- Figure: (R1)

---

- [[Deep]] is scalable machine learning

![[Pasted image 20221003181456.png]]

- Deep learning is scalable, because it is the ability to more and more remove the input of human experts. Remove human costly inefficient effort of human beings in the picture. 
- Deep learning automates much of the extraction, get us closer to the raw data without human involvement. 

---
- There is always a balance between excitement and disillusionment.
- "Gartner hype cycle" appears in all technology aspect.



![[Pasted image 20221003181933.png]]

---
## Why not deep learning

- Automatic robots:
	- Autonomous cars, robots, don't use data model, instead they are model-based [[Conventional methods]] methods, that don't learn from data over time. 
	- To date almost no machine learning has been used, except for trival perception. 
	- The same for auto cars, no machine learning and deep learning has been used, except with perception.  
	- Some aspect of enhanced perception from the visual texture information. 
	- Most robotic has attributed mostly to non machine learning methods. 

- Unintended consequences
	- When a robot learn, based on objective function, the conseqences is not always obvious. 
	- eg: robot realize to get most points, it don't need to finish the race. Unrealized consequence happens, at least before they happens. That show the need of AI safety
	- 

![[Pasted image 20221003190340.png]]

---
- Challenge of deep learning
	- image classification is not necessarily scene understanding. 

----
![[Pasted image 20221003190916.png]]


---
![[Pasted image 20221003191224.png]]
- Abstract thinking is a hard thing

---
![[Pasted image 20221003192014.png]]
- Removing the "teacher" from the picture.
- The ecosystem that allow humans / neural networks to perform unsupervised learning. 
---
![[Pasted image 20221003192206.png]]
- Human can learn from very few examples. 
- Machines need thousands millions of examples. 

---

![[Pasted image 20221003192608.png]]

---
## Inspirations from biological network

![[Pasted image 20221003192801.png]]


---
![[Pasted image 20221003193228.png]]

- Find all the object in the scene and classify it

![[Pasted image 20221003193256.png]]
- Tradeoff: Performance and accuracy. 

---
![[Pasted image 20221003193544.png]]

- Semantic segmentation
	- 


- The architecture of object detection
---

- Transfer learning
	- Most extensively most successfully in computer vision is transfer learning. 
	- Most commonly applied way of transfer learning is taking a pre-trained neural network, eg: ResNet, and chopping it off at some point. 
		- eg: you have a specific application , such as pedestrian detection. and you have pedestrian dataset, it is useful to take resnet trained on imagenet or CoCo. cut it off, and train on your specific dataset. 
	- This is extremely useful in CV, speech, NLP. 


---
- [[Autoencoder]] 

![[Pasted image 20221004182218.png]]

- With the pretrained network, they are ultimately forming representations of the database on which classifications the regression is made, prediction is made.
- The autoencoder, forming representations in an unsupervised way. 
- The input / output is the same image. 
- Add a bottleneck in the network, where there the network is narrower at the middle that it is on the inputs and the outputs. --> It is forced to compress the data down into meaningful representation. (that's what autoencoder does.)
- Training it to reproduce the output, reproduce it with a latent representation, that is smaller than the original data. 
- Normally, if you want to train a useful representation of data, you want to train it in a supervised way. Want to train it on a discriminative task, where you have labeled data. 

- Embedding projector: 
	- https://ai.googleblog.com/2016/12/open-sourcing-embedding-projector-tool.html
	- https://projector.tensorflow.org/?config=https://gist.githubusercontent.com/akuchotrani/cc9296c2e566d495057ae27ea0da2d42/raw/8b79fcee60094861c11ac58006dbe03230ca8fbc/test_projector.json

---

-  open source Embedding projector: google tensorflow

---

- Word embeddings (word2vec)
	-  1. taking all vocabularies, want to be able to map it into a vector space, where words are far apart from each other in a Euclidean sense. 

---
![[Pasted image 20221004184320.png]]

- AutoML (google) and neural architecture search (NASNet)
	- A general concept of neural architecture search, NASNet.
	- The ability to automate the discovery of parameters of a neural network. 
	- The ability to discover the actual architecture that produces the best results. 
	- By this, you can construct a neural network that is much more efficient and accurate then state of the art. 
	- All you bring is the data, the model gives you the NN structure, and also ready to use. 
	- Structure
		- Similar basic module to the ResNet modules <-- what is ResNet
		- And with a recurrent neural network, you keep assembling and network together. Assembling in such a way that it minimize the loss of the overall classification performance. 

---
![[Pasted image 20221004184602.png]]
- Deep reinforcement learning
	- It is the task of an agent to act in the world based on the observations of the state and the rewards received in that state, knowing very little about the world, and learning from very sparse nature of the reward. 
		- eg: gaming context. 

---
- Towrds AGI
	- Transfer learnng
	- hyperparameter optimization
	- architecture search
	- meta learning 