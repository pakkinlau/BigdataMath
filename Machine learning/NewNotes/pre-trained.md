---
category: []
alias: []
tags :[]
---

- 24-10-2022 21:51: created

- superset:
	- [[model]]

- Related: [[transfer learning]]

- What is pre-trained?
	- A pre-trained model is a saved network that was previously trained on a large dataset, typically on a large-scale image-classification task. You either use the pretrained model as is or use [[transfer learning]] to customize this model to a given task. (R1)
	- Pre-trained model reduces carbon emissions, especially for [[Convolutional|CNN]] tasks which consumes a lot of GPU computational power. 

- Famous pre-trained model
	- [[computer vision]]:  (R2)
		- VGG19
		- Inceptionv3 (GoogleNet)
		- ResNet50
		- EfficientNet

- Customize a pre-trained model: 
	- 1. Feature extraction 
		- Use the [[representation]] learned by a previous network to extract meaningful features from new samples. You simply add a new [[classifier]], which will be trained from scratch, on top of the pretrained model so that you can repurpose the feature maps learned previously for the dataset.
		- so that you can repurpose the feature maps learned previously for the dataset.
		- You do not need to (re)train the entire model. The base convolutional network already contains features that are generically useful for classifying pictures.
	- 2. Fine-tuning
		- Unfreeze a few of the top layers of a frozen model base and jointly train both the newly-added classifier layers and the last layers of the base model. This allows us to "fine-tune" the higher-order feature representations in the base model in order to make them more relevant for the specific task.

---
## Worked example

- https://www.tensorflow.org/tutorials/images/transfer_learning#:~:text=A%20pre%2Dtrained%20model%20is,model%20to%20a%20given%20task.

- This webpage contains a worked example of using a pre-trained model (`MobileNet`) to complete CNN tasks. 
	- 1. Use the model by: 
		- `base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,include_top=False,weights='imagenet')`
	- 2. Prevent the model changing by:
		- Freeze the convolutional base, before compiling and train the model. 
		- "Train" the model by `feature_batch = base_model(image_batch)`
	- 3. Add a [[classification]] head, pooling layer and dense layer. 
		- To generate predictions from the block of features, average over the spatial locations
		- `global_average_layer = tf.keras.layers.GlobalAveragePooling2D() feature_batch_average = global_average_layer(feature_batch)`
	- 4. Fine-tuning
		- Train the pre-trained model alongside the training of the classified you added. 
		- The training process will force the weights to be tuned from generic feature, maps to features associated specifically with the dataset. 
	- 5. Un-freeze the top layers and compile the model again.


---
## Reference

1. [[(Course) Tensorflow Core tutorial]]
2. Orhan's medium blog: https://towardsdatascience.com/4-pre-trained-cnn-models-to-use-for-computer-vision-with-transfer-learning-885cb1b2dfc
3. [[(Course) google developers - machine learning courses]]