# Malcolm Kahora, Benjamin Fryc, Raj Singh
# CSC 426-01: Project 3 - ID3 Algorithm
# Dr. Bloodgood
# 4/19/24

import math

def main():
    # First, retrieve training examples and attributes from sample data txt file
    file = open('PlayTennisSampleDataFormat.txt', 'r')

    # Attributes is a list of other attrs that may be tested by the learned DT
    attributes = file.readline().split(',')

    # Examples are the training examples
    examples = file.readlines()

    # Target_attr is the attr whose value is to be predicted by the tree
    target_attr = attributes[-1]

    # Call ID3 algorithm
    ID3(examples, target_attr, attributes)

# ID3 Algorithm
def ID3 (examples, target_attr, attributes):
    # Create a root node for the tree

    # boolean flags for all positive or all negative training examples
    all_pos = True
    all_neg = True

    # number of positive and negative examples
    p_examples = 0
    n_examples = 0

    for x in examples:
        single_case = x.split(',')
        if single_case[-1].strip() == 'Yes':
            all_neg = False
            p_examples += 1
        elif single_case[-1].strip() == 'No':
            all_pos = False 
            n_examples += 1

    num_examples = len(examples)

    # Calculate entropy
    entropy = ((-1) * (p_examples / num_examples) * math.log2(p_examples / num_examples)) + ((-1) * (n_examples / num_examples) * math.log2(n_examples / num_examples))
    print(entropy)

    IG_scores = [0]

    #if all examples are positive, return single-node tree Root with label = +
    #If all examples are negative, return single-node tree Root with label = -
    if all_pos:
        return TreeNode(value='+')
    elif all_neg:
        return TreeNode(value='-')
    else:
        # First we must find all possible values for each attribute

        # Dictionary to store possible values for each attribute
        possible_values = {}

        for attr in attributes:
            # Skip ExampleID attribute
            if attr == 'ExampleID':  
                continue
            
            # Use a set to store unique values
            values = set()  
            for example_line in examples:
                # Strip the newline character and split the line by comma to get values for each attribute
                example_values = example_line.strip().split(',')
                # Extract the value for the current attribute and add it to the set
                values.add(example_values[attributes.index(attr)])
            
            possible_values[attr] = values


        # Here is where I left off - I want to calculate the IG for each attribute, this can be a different method as well
        # 
        # We can now use the possible values to determine the amount of information gain each attribute can provide
        for attr in attributes:
           for attr in attributes:
            # Skip ExampleID attribute
            if attr == 'ExampleID':  
                continue

            if len(possible_values[attr]) > 2:
                IG_scores.append()
            else:
                value_entropies = []
                for x in possible_values[attr]:
                    value_entropies = []
                    
                IG_scores.append(entropy - sum(possible_values))

            # After we find all the values, we will pick the attribute with the highest IG for the root


    #If attributes is empty, return single-node Root with label = most common value of the target_attr in Examples
    #else:
    #   A = the attr from attributes that best classifies examples - IG
    #   Set the decision tree attr for Root = A
    #   For each positive value vi of A {
    #       add a new tree branch below Root, corresponding to the test A==v;
    #       let examples vi be the subset of examples that have value vi for A;
    #       if examples vi is empty:
    #           below the new branch, add a leaf node with label = most common value of target_attr in examples;
    #       else :
    #           below the new branch, add the subtree ID3 (examples vi, target_attr, attributes - {A})
    #return root;
    
# Tree node methods
class TreeNode:
  def __init__(self, value):
    self.value = value # data
    self.children = [] # references to other nodes

  def add_child(self, child_node):
    # creates parent-child relationship
    print("Adding " + child_node.value)
    self.children.append(child_node) 
    
  def remove_child(self, child_node):
    # removes parent-child relationship
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children

main()
