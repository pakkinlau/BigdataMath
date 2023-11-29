---
category: []
alias: [PPM]
tags: []
---

- 28-10-2022 16:44: created

- What is prediction by partial matching (PPM)?
	- Prediction by partial matching (PPM) is an [[adaptive]] statistical data compression technique based on [[context model]] and [[prediction]]. 
	- Predictions are usually reduced to symbol rankings. The number of previous symbols, n, determines the order of the PPM model which is denoted as PPM(n). Unbounded variants where the context has no length limitations also exist and are denoted as PPM.
	- If no prediction can be made based on all n context symbols a prediction is attempted with just n-1 symbols. This process is repeated until a match is found or no more symbols remain in context. 


---
## Reference

1. 