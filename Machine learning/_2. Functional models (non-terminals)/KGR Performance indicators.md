- 28-9-2022: created

- MRR and HITS@10 are two important indicators. MR is not a good indicator.

- Mean reciprocal rank, MRR
	- MRR measures the number of triples predicted correctly. If the first predicted triple is correct, then 1 is added, if the second is correct is summed, and so on
	- $$MRR={1 \over |S|} {\sum_{i=1}^{|S|}}  {1 \over rank_i} = {1 \over |S|}({1 \over rank_1} + {1 \over rank_2}+ \dots + {1 \over rank_{|S|}})$$
- MR:
	- $$MR = {1 \over |S|}{\sum_{i=1}^{|S|}}  {rank_i}$$
- Hits@n, Hits@10, Hits@1, H@K
	- (R2) It is a [[performance]] index that measures the **probability** to find the correct prediction in the first top K model predictions. Usually k=10 reflects the accuracy of an embedding model to predict the relation between two given triples correctly. 
	- Set expression: 
		- $$HITS@n = {1 \over |S|}{\sum_{i=1}^{|S|}}  {I(rank_i \leq n)}$$
		- $$HITS@K = {|\{q \in Q : q<k\}| \over |Q|} \in [0,1]$$


---

## Reference
1. China website: https://blog.csdn.net/yang13563758128/article/details/122088487
2. [[(Wikipedia) Knowledge graph embedding]]