- Or called BPE
- Compression technique used in NLP to handle out-of-vocabulary words and reduce the vocabulary size. 
- It is a data compression algorithm that splits the input text into subword unit.
- How it works:
	- Initialization:
		- BPE starts with initializing the vocabulary with individual characters or subword.
	- Merge operation:
		- In each iteration, the algorithm looks for the most frequently occuring pair of characters or subwords in the vocabulary and merges them into a single subword.
	- Iteration:
		- The algorithm repeats the merge a specified number of times or until a certain condition is met.
	- Completion:
		- Once the desired condition is met, the merge operation is reached and the algorithm stops.