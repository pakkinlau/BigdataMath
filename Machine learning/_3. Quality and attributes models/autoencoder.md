- 5-10-2022: created

- The autoencoder, forming [[representation|representation]] in an [[Unsupervised learning|unsupervised]] way.  (R1)

- related:
	- [[Compress]]

- How autoencoders work: 
	- With the [[pre-trained]] network, they are ultimately forming [[representation|representation]] of the database on which classifications the regression is made, prediction is made. (R1)
	- The input / output is the same image.  (R1)
	-  Add a bottleneck in the network, where there the network is narrower at the middle that it is on the inputs and the outputs. --> It is forced to [[compress]] the data down into meaningful [[representation|representation]]. 
	- Training it to reproduce the output, reproduce it with a latent [[representation|representation]], that is smaller than the original data

![[Pasted image 20221004182218.png]]
- Figure: the autoencoder that generates latent representation of the input image. 

---


## Reference
1. [[(Video) Fridman 2019, Deep Learning Basics --  Introduction and Overview]]