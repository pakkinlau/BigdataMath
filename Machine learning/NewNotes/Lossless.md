---
category: []
alias: []
tags: []
---

- 28-10-2022 16:39: created

- What is Lossless?
	- Lossless data compression algorithms usually exploit statistical redundancy to represent data without losing any information, so that the process is reversible. (wiki)
	- It is possible because most real-world data exhibits statistical redundancy. (wiki)
		- eg: image -- run-length encoding
			- an image may have areas of color that do not change over several pixels; instead of coding "red pixel, red pixel, ..." the data may be encoded as "279 red pixels". 
		- eg: Lempel-Ziv compression -- hardware memory
	- The strongest modern lossless compressors use probabilistic models, such as [[prediction by partial matching.]] 
	- 


---
## Reference

1. 