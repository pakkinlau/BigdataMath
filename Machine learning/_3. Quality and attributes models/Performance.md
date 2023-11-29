- 5-10-2022: created

- Subset:
	- [[State-of-the-art]]

- Performance metrics are a part of every machine learning pipeline. They tell you if you’re making progress, and put a number on it. 
- i.e. the performance is task-specific. 

- Regression metrics:
	- MAE
	- MSE
	- RMSE
	- R-Squared

- Classifcation metrics:
	- Accuracy
	- Confusion matrix
	- Precision and recall, precision-recall tradeoff 
	- F1-score
	- AU-ROC

---
- For [[NLP tasks]], it has a number of tasks, which could be marked its performance individually.


- Example: [[Stanza]]'s performance' (R2)
	- [[Data]]: Universal dependencies (v2.5) test [[treebank]]. 
	- Test for:
		- MWT expander
		- POS/UFeats tagger
		- Lemmatizer
		- Dependency parser
![[Pasted image 20221012152906.png]]


![[Pasted image 20221012153433.png]]
- Example: (R2)
	- [[named entity recognition|NER]] performance across different languages and corpora.  
	- Entity micro-averaged test $F_1$.
	- For each corpus we also list the number of entity types. 

---
- Translation related performance
	- [[bi-text retrieval]]


---
- Volume related performance
	- data required to achieve good performance (R3)
	- 



---
## Reference

1.  2022, Bajaj neptune.ai https://neptune.ai/blog/performance-metrics-in-machine-learning-complete-guide
2. [[(Paper) Qi, P., Zhang, Y., Zhang, Y., Bolton, J., & Manning, C. (2020). Sta n z a -- A Python Natural Language Processing Toolkit for Many Human Languages.]]
3. [[(Paper) Feng, F., Yang, Y., Cer, D., Arivazhagan, N., Wang, W., & Ai, G. (2020). Language-agnostic BERT Sentence Embedding.]]