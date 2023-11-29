---
alias: [link features, relation features]
---
- 6-10-2022: created

- superset: [[feature]]

- distance-based feature: 
	- shortest path distance between two nodes.
- local neighborhood overlap: 
	- If A and B has common friend. It indicates A and B might have a missing link.
	- Jaccard's coefficient: intersection of [[neighbor]] / union of neighors
- global neighborhood overlap
	- Even if A and B has no common friend, they might still have a chance to have a missing link.
	- it attempts to solve the problem: two nodes still can be connected in the future. But local metric always zero if they don't have commons. 
	- global metrics resolve the limitation of local overlap by considering the entire graph.
	- Katz index: calculate the number of walks between two nodes. 
- local neighborhood overlap

- Cs224w w2: The key is to design features for "a pair of nodes"
	- My perspective: No. For knowledge graph it should be a multigraph. Which is, two entities could have more than one relation. 

![[Pasted image 20220915175443.png]]
- Figure: "common friend"


