---
category: []
alias: []
tags :[]
---

- 24-10-2022 14:53: created

- What is Data preparation and feature engineering?
	- To get those [[prediction]] right, we must construct the [[data]] set and transform the data correctly. 

- eg:
	- Google translate team has more training data than they can use. Rather than tuning their model, the team has earned bigger wins by using the best features in their data.
	- "...one of our most impactful quality advances since neural machine translation has been in identifying the best subset of our training data to use" --- Software Engineer, Google Translate
	- "...most of the times when I tried to manually debug interesting-looking errors they could be traced back to issues with the training data."  --- Software Engineer, Google 
	- "Interesting-looking" errors are typically caused by the data. Faulty data may cause your model to learn the wrong patterns, regardless of what modeling techniques you try.

- Steps to Constructing Your Dataset
	1.  Collect the raw data.
	2.  Identify feature and label sources.
	3.  Select a sampling strategy.
	4.  Split the data.

![[Pasted image 20221024145708.png]]
- Fig: Typical process of a machine learning pipeline. 

- Size and quality of a data set
	- It depends on the project. Consider the relative size of these data sets.
![[Pasted image 20221024150311.png]]

- Quality of a data set
	- Consider taking an empirical approach and picking the option that produces the best outcome. With that mindset, a quality data set is one that lets you succeed with the business problem you care about. 
	- While collecting data, it is helpful to have a more concrete definition of quality. Certain aspects of quality tend to correspond to better-performing models.
		- [[reliability]]
		- feature [[representation]]
		- minimizing skew

---
## Reference

1. [[(Course) google developers - machine learning courses]]