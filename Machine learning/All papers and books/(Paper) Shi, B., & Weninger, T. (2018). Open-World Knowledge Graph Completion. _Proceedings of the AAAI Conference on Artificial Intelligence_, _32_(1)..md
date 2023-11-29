- 28-9-2022: created

---
- Round 1: 
	- Abstract:
		- KGC proposed to improve KGs by flling in its missing connections. 
		- Unlike existing method that holds a closed-world assumption, they relax this assumption by propose a new open-world KGC task -- with "ConMask"
		- Use a relationship-dependent content masking to extract relevant snippets and then trains a fully CNN to fuse the extracted snippets with entities in the KG. 
	- Figures:
		- Sample KG where there exist s missing edge 
		- Translational model timeline
	- Tables:
		- Score functions, memory complexity of tensor dopositional models 
	- Link prediction benchmarks 
		- Dataset: WN18RR and FB15k-237
		- MR: lower = better 
		- MRR
		- Hits@10: Higher  = better 
		- Hits@1

---

 -![[Shi, B., & Weninger, T. (2018). Open-World Knowledge Graph Completion. Proceedings of the AAAI Conference on Artificial Intell.pdf]]