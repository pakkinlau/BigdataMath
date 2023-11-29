- 4-10-2022: created

- Nearly the first GPU-implementaton of CNNs.
- AlexNet is considered one of the most influential papers published in computer vision, having spurred many more papers published employing CNNs and GPUs to accelerate [[Deep]]. >80,000 citations 

- AlexNet competed in the ImageNet large scale visual recognition challenge on 2012. It arhieved a top-5 error of 15.3%.
- The original paper's primary result was that the depth of the model was essential for its high performnace, which was computationally expensive , but made feasible due to the utilization of GPUs during training. 

- ALexNet was outperformed by Microsoft research's very deep (~100 layer) mdeol, which won the imageNet 2015 contest.


---
## Design

- Contained 8 layers, the first five were convolutional layers, some of them followed by [[pooling]] layer, and the last three were fully connected layer. 
- It used the non-saturating ReLU activation function, which showed improved training [[performance]] over tanh and sigmoid.