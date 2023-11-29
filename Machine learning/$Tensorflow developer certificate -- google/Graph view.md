- Graph views: 
	- Available:
		- Filters: Only show or remove the specific path / file name.
		- Groups: Color the specified path / file name
	- Exclude something from the graph: 
		- adding a minus sign before the entity name, such as `path:-"All courses"` `file:-"changelog"`
	- Remarks 
		- 1: a spacebar is required to make both condition works. 
		- 2: Use spacebar!! And don't use comma, comma causes problem on the searching result. 

## Example:
- Vault : machine learning
	- Local graph: 
		- filtering: `file:-"changelog" file:-"_func index"  path:-"All papers and books" path:-"All research sprints" path:-"All courses"`

---
## Find any nodes that index node doesn't tracked. 

Hello. I put N nodes within a folder, and also one index notes in the folder that links almost all nodes that categorize the notes that guides navigation. Now I want to find any nodes that index node doesn't tracking. How can I specify "Group" condition of the graph view to be "The nodes that are linked with a specific node" (depth =1 neighbor) in color red? Thank you.

- Step 1: archive the current filter setting: `path:-"All courses", file:-"changelog"`
- Step 2: new filter: `path: "_2. Functional models"`
