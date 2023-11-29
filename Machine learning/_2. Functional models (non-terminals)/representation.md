---
alias: [feature representation]
---

- 3-10-2022: created

- Types of representation:
	- [[latent]] representation

- related:  [[Representation theory]], [[feature learning]]

---
## Types: 

- subset:
	- [[feature]]
	- [[graph]]
		- Notions sorted by time: 
			- 1. Use summary graph statistics, treat "representation" as a pre-processing task, and then using hand-engineered statistics to extract structural information (2000s?)
			- 2. [[node embedding]] (low-dimensional vector), using a data-driven approach to learn embeddings that [[encoder|encode]] graph structure, treating [[representation]] itself as machine learning task, and hopes for getting [[embedding]] can be used as [[feature]] inputs for [[machine learning]] [[downstream tasks|downstream task]] (2010s)
			- 3. Knowledge representation
	- [[natural language processing|NLP]]
		- [[Word representation]]
			- [[GloVe]]

---
- What is representation?
	- The space/category that allow all possible [[feature]] to live in.
	- If we talk about designing a feature set for [[machine learning]]. we are in the aspect of representation design.
- Practice
	- Know your data
		- Visualize -- plot histogram, rank most to least common
		- Debug -- Duplicates / missing
		- Monitor -- Feature quantiles over time?
- What makes good representations?
	- 1. Possible values
		- [[feature]] values should appear with non-zero value more than a small handful of times in the dataset.  
			- eg: `model = 8SK982ZZ1242Z` is not good. `model = galaxy_s6` is good. 
	- 2. Obvious meaning
		- `user_age=23` is good, `user_age = 123456789` is not good.
	- 3. Feature should not take "magic" value
		- eg: `watch_time: -1.0` to show house never been in the market. Use another indicator take on a boolean value, showing our days the product is on the market on how many days etc. 
	- 4. Feature should not change over time.
		- idea of stationary of data.
		- we might want to version it?
		- eg: `city_id:"br/sao_paulo"` is good
		- eg: `inferred_city_cluster_id: 3265` is not good.
	- 5. Distribution should not have extreme outliners. 
		- Binning trick

![[Pasted image 20221023214644.png|600x300]]
- Fig: Binning trick. (R3)
	- If we think the effect of latitude on the housing prices, there is no sort of linear relationship from North to South.
	- But within any particular latitude there often is pretty strong correlation.
	- We bucket ranges, and these each become boolean feature, we can use one-hot embedding here.
	- A cheap way to map some non-linear feature.


- Relationships to other concepts: 
	- Deep learning is a subset of representation learning. (R1)
	- Representation learning is feature learning. (R1)


![[Pasted image 20221003173448.png]]
- Figure: (R1)

---
- Why representation matters?
- 1. Effective for being able to interpret data
	- With different representation, the [[tasks]] of drawing the line becomes difficult, it requires more [[dimensionality|dimension]] to do it accurately. (R1)
	- [[machine learning]] is forming representation that map the topology, the space that you are trying to deal with of the raw inputs, map it in such a way, trival to classify, trival to perform regression, trival to generate new samples of that data. (R1)
	- Higher and higher levels of representation is really the dream of artificial intelligence. (R1)
- 2. "[[understanding]]" is making the complex simple. Like Einstein back in a few slides ago.  (R1)
	- That's been the dream of all the science in general, of the history of science is the history of compression progress, of forming simpler and simpler representation of ideas. (R1)

---

![[Pasted image 20221003181129.png|500x400]]
- Figure: (R1). The representation that makes the prediction difficult. 

![[Pasted image 20221003174723.png|500x400]]
- Figure: (R1)
---
## Goal

- [[natural language processing|NLP]]
	- Capturing fine-grained [[semantics|semantic]] and [[syntactic]] regularities using vector arithmetic. (R2)
	- but the origin of these regularities has remained opaque. (R2)
---
## Attributes and qualities

- 1. [[Use of statistical information]]

---
## Example of representations

![[Pasted image 20221023213508.png|400x200]]
- 1. If we have numerical data, just use it. Natural.
![[Pasted image 20221023213553.png|400x200]]
- 2. If we have street names, we might use one-hot vector.



---
## Reference

1. [[(Video) Fridman 2019, Deep Learning Basics --  Introduction and Overview]]
2. [[(Paper) Pennington, J., Socher, R., & Manning, C. (2014). GloVe Global Vectors for Word Representation]]
3. [[(Course) google developers - machine learning courses]]