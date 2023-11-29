---
alias: linear mapping
---


- In [[neural network]], if we use linear mapping, without using non-linear activation function, the neural network cannot learn anything.
- Some might argue, can we use non-linear mapping function, without using any activation function. Actually the combination of "linear mapping + non-linear activation function" can express any non-linear function. This is rooted in the [[universal approximation theorem]], which provides a theoretical foundation for the [[expressive power]] of neural networks.

For linear mapping between layers, the following holds:
- We use a matrix to represent each layer, then we have:
	- $x^{(1)} = A_1x$
	- $x^{(2)} = A_2x^{(1)}$
	- $y = A_3 x^{(2)}$
- then we have a compositional structure:
	- $y = A_3 A_2 A_1 x$
- This gives limited range of functional responses, due to linearity.

---

**Concept: Linear Mapping in Neural Networks**

**Definition:**
Linear mapping, also known as linear transformation or linear layer, is a fundamental operation in neural networks. It refers to the process of transforming input data using a linear function. In the context of neural networks, this operation is crucial for connecting input features to hidden layers and output layers.

**Key Points:**

1. **Linearity:** Linear mapping preserves the fundamental property of linearity, meaning the output is a linear combination of the inputs. Mathematically, it can be represented as:
$$ \text{Output} = \text{Weight} \times \text{Input} + \text{Bias}$$
   Here, weights represent the importance given to each input feature, and bias provides an offset to the output.

2. **Weights and Biases:** Neural networks learn optimal weights and biases during the training process. These learned parameters enable the network to capture complex patterns and relationships within the data.

3. **Role in Neural Networks:** Linear mapping is typically followed by a non-linear activation function, such as ReLU (Rectified Linear Unit) or Sigmoid. This combination allows neural networks to learn and approximate complex, non-linear relationships in the data. Without non-linear activation functions, the entire network would collapse into a series of linear mappings, limiting its expressive power.

4. **Multilayer Networks:** In deep learning models, linear mappings are used in multiple layers, forming a deep architecture. Each layer applies linear mapping followed by non-linear activation, enabling the network to learn hierarchical representations of the input data.

5. **Training and Optimization:** During the training process, neural networks use techniques like backpropagation and gradient descent to adjust the weights and biases in the linear mappings. This optimization process aims to minimize the difference between the predicted output and the actual target values, making the network capable of making accurate predictions on unseen data.

**Applications:**

1. **Image Recognition:** Linear mappings are used in convolutional neural networks (CNNs) to process image data, extracting features from different parts of the image.

2. **Natural Language Processing:** In tasks like text classification and sentiment analysis, linear mappings help transform word embeddings or textual features into numerical representations.

3. **Recommendation Systems:** Linear mappings are employed in collaborative filtering algorithms, where user-item interactions are modeled as linear transformations to predict user preferences for unseen items.

---

### Q: can we use non-linear mapping and no activation function

Yes, it is possible to use non-linear mapping without an activation function, but it significantly affects the expressive power and capabilities of the neural network. Let me explain the implications of using non-linear mappings without activation functions:

1. **Limited Expressiveness:** Without activation functions, each layer of the neural network becomes a linear transformation of its inputs. Consequently, no matter how many layers you stack, the overall operation remains linear. This limitation means the network can only model linear relationships in the data, severely restricting its capacity to learn complex patterns.

2. **Inability to Learn Non-linear Patterns:** Activation functions introduce non-linearities into the network, allowing it to learn and approximate non-linear patterns within the data. Without these non-linearities, the network would not be able to capture intricate relationships, making it unsuitable for tasks that involve non-linear data patterns, such as image recognition, language processing, and many real-world problems.

3. **Lack of Representation Learning:** One of the key strengths of deep learning models lies in their ability to automatically learn hierarchical and abstract representations of the input data. Activation functions enable this process by introducing non-linear transformations at each layer, allowing the network to learn increasingly complex features. Without them, the network loses this capability, making it difficult to learn useful representations.

4. **Vanishing or Exploding Gradients:** Without activation functions, deep networks are prone to vanishing or exploding gradient problems during training. These issues can hinder the convergence of the network and make it challenging to optimize the model effectively.

While it's theoretically possible to construct a neural network without activation functions, doing so severely limits the network's capacity to learn and generalize from the data. Activation functions are essential elements that introduce non-linearities, allowing neural networks to approximate complex, non-linear functions efficiently. Therefore, in practice, activation functions are almost always used in modern neural network architectures to enable the network to learn and solve a wide range of real-world problems.