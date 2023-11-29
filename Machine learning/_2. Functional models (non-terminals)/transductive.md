- 6-10-2022: created

- Transductive setting (Reasoning from observed, specific training cases to specific test cases.): train/valid/test set data are on the same graph
	- Transduction = Reasoning from observed, specific (training) cases to specific (test) cases. 
	- Vladimir Vapnik (PhD in statistics): When solving a problem of interest, do not solve a more general problem as an intermediate step, try to get the answer that you really need but not a more general one. 
	- Transduction was introduced by Vladimir Vapnik in 1990s, induction requires solving a more general problem  (inferring a function) before solving a more specific problem.
	- The predictions of the transductive model are not achievable by any inductive model.
		- eg: binary classification. A large set of test inputs may help in finding the clusters, thus providing useful information about the classification labels. The same predictions would not be obtainable from a model which induces a function based only on the training cases.
		- eg: Transductive suppert vector machine (TSVM).
	- Why transduction could be more accurate than inductive learning:
		- Route 1: Examples -->Induction to get approximating functions --> Deduction using that function to perform prediction.
		- Route 2: Examples --> Use transduction to preform prediction. 

- Feature:
	- Transductive learning does not build a predictive model. If new unlabelled points are encountered, we will have to re-run the algorithm. Inductive model is a predictive model, it could initially built model to predict new unlabelled points. 
	- Inductive learning has less computational cost than transductive learning. 