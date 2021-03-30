# 	DECISION TREE :



- Graphical representation of all possible solutions to a decision based on some conditions.

- Decisions made can be easily explained.

- ### why this is called as "DECISION TREE" ?

- Because it starts with a root and branches into number of decisions or conditions, like a tree.

- To build a decision tree, we use algorithm called "CART".

- #### CART-Classification And Regression Tree

- ## DECISION TREE TERMINOLOGIES :

- ROOT NODE :it is first node of a tree.

- it is called as base/parent node.

- It represents entire population or sample & this further divided into 2 or more homogenous sets.

- LEAF NODE : It cannot be further segregated into further nodes.

- ### SPLITTING:

- dividing the root or sub node into different parts on the basis of some condition.

- BRANCH/SUB TREE:

- Formed by splitting the node.

- PRUNING :

- Removing unwanted nodes from the tree.

- opposite of splitting.

- CHILD NODE:

- All other nodes except root node.

- the node is derived from parent node.

#### 

### HOW DOES A TREE DECIDE WHERE TO SPLIT

#### GINI INDEX:

- The measure of impurity used in building decision tree.

#### INFORMATION GAIN:

- Measures reduction in entropy.
- Decides which attribute should be selected as the decision node.

### REDUCTION IN VARIANCE :

- It is an algorithm used for continuous target variables(regression problems).

### CHI SQUARE :

- It is an algorithm to find out statistical significance between the differences between subnodes & parent node.

## ENTROPY

- It is  a metric that measures impurity of something.

- The first step to solve the problem of a decision tree.

- IMPURITY means degree of randomness.

- ### Entropy (s)= - P(yes) log2 P(yes) - P(no) log2 P(no)

- S is the total sample space.

- No of yes = No of no, then Entropy(s)=1

- contains all yes or all no, then Entropy(s)=0

#### INFORMATION GAIN:

- #### INFORMATION GAIN = Entropy(S) - [(Weighted Avg) * Entropy(each feature)]

- S total collection.

  
  
  # RANDOM FOREST
  
  

- Random forest is an ensemble classifier made using many decision tree models.

- Random forest does compilation of multiple decision trees and its final decision goes with majority voting.

- Random forest is a versatile algorithm capable of performing both

- - REGRESSION

  - CLASSIFICATION

    - #### RANDOM FOREST USED IN VARIOUS FIELDS :

- ##### BANKING: 

  Identification of loan risk applicants by their probability of defaulting payments.

  - ##### MEDICINE :

- Identify whether a person actually as disease or not.

- ##### LAND USE :

Identification whether land is suitable for urbanisation, all facilities are there ...etc.

- MARKETING :

Identifying number of persons actually loosing out of markets.

- ### FEATURES :

- Most accurate learning algorithm.

- Works well for both Regression and Classification problems

- Runs efficiently on large databases

- Requires almost no input preparation.

- Performs implicit feature selection

- Can be easily grown in parallel.



## ENSEMBLE TECHNIQUE :



- BAGGING
- BOOSTING

#### BAGGING :

- Also called as BOOTSTRAP AGGREGATION

- 

  

  

  - 

