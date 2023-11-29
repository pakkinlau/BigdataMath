---
category: []
alias: []
tags :[]
---

- 24-10-2022 15:05: created

- What is reliability?
	- Reliability refers to the degree to which you can trust your data. A model trained on a reliable data set is more likely to yield useful predictions than a model trained on unreliable data. 
	- In measuring reliability, you must determine:
		- How common are label errors? For example, if your data is labeled by humans, sometimes humans make mistakes.
		- Are your features noisy? For example, GPS measurements fluctuate. Some noise is okay. You’ll never purge your data set of all noise. You can collect more examples too.
		- Is the data properly filtered for your problem? For example, should your data set include search queries from bots? If you're building a spam-detection system, then likely the answer is yes, but if you're trying to improve search results for humans, then no.

- What makes data unreliable? Recall from the Machine Learning Crash Course that many examples in data sets are unreliable due to one or more of the following:
	- Omitted values. For instance, a person forgot to enter a value for a house's age.
	- Duplicate examples. For example, a server mistakenly uploaded the same logs twice.
	- Bad labels. For instance, a person mislabeled a picture of an oak tree as a maple.
	- Bad feature values. For example, someone typed an extra digit, or a thermometer was left out in the sun.


---
## Reference

1. [[(Course) google developers - machine learning courses]]