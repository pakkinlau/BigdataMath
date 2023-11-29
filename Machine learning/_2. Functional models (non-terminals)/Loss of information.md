---
category: []
alias: [lossy]
tags: []
---

- 25-9-2022: created

- What is Loss of information?
	- During a [[Compress|compression]] process, some loss of information occurs.
	- Why some lossy compression schemes are allowed?
		- Corresponding trade-off between preserving information and reducing size. 
		- eg: human eyes is more sensitive to subtle variations in luminance than it is to the variations in color. JPEG image compression works in part by rounding off nonessential bits of information.
		- Lossy image compression is used in digital cameras, to increase storage capacities. Similarly, DVDs, Blu-ray and streaming video use lossy video coding formats. Lossy compression is extensively used in video.
- Source of lossy
	- Most forms of lossy compression are based on transform coding, especially the discrete cosine transform (DCT).

- One problem of machine learning is that, it is [[inductive]] thinking, it is not [[transductive]] thinking. 
- The avg(), max(), sum() that adopted during training in many cases lead to loss of information. 
- eg: [[Transformer]] tries to mitigate the problem by replacing RNNs. 


---
## Reference

1. 

