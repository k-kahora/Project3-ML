# Malcolm Kahora, Benjamin Fryc, Raj Singh
# CSC 426-01: Project 3 - ID3 Algorithm
# Dr. Bloodgood
# 4/19/24
import sys
import csv
from math import log2

# The target attribute is always the attribute with the target value
def entropy(subset, target_attribute):
    total = len(subset)
    if total == 0:
        return 0
    class_counts = {val: 0 for val in set(item[target_attribute] for item in subset)} # Creates a dictionary of possible values, begin Yes or No in this case.
    for item in subset:
        class_counts[item[target_attribute]] += 1 # Counts up the amount for each
    return sum((-count/total) * log2(count/total) for count in class_counts.values() if count > 0)

def info_gain(data, attribute, target_attribute):
    total_entropy = entropy(data, target_attribute)
    attribute_values = set(item[attribute] for item in data)
    weighted_entropy = 0
    for value in attribute_values:
        subset = [item for item in data if item[attribute] == value]
        weighted_entropy += (len(subset) / len(data)) * entropy(subset, target_attribute)
    return total_entropy - weighted_entropy

def id3(data, attributes, target_attribute):
    target_values = set(item[target_attribute] for item in data) # Value could be one or two
    if len(target_values) == 1:
        return next(iter(target_values))  # All examples are the same class so just return the class
    if not attributes:
        most_common = max(target_values, key=lambda val: sum(item[target_attribute] == val for item in data))
        return most_common
    best_attribute = max(attributes, key=lambda attr: info_gain(data, attr, target_attribute)) # This is the best attribute or the attribute to split on for the most information gain
    tree = {best_attribute: {}}
    remaining_attributes = [attr for attr in attributes if attr != best_attribute] # Remove the best attribute
    for value in set(item[best_attribute] for item in data): # Loop through only the best attribute for each data item
        subset = [item for item in data if item[best_attribute] == value] # This is all data items that have the same current value that's iterated from the best attribute
        subtree = id3(subset, remaining_attributes, target_attribute) # Get the best subtree from the remaining subset
        tree[best_attribute][value] = subtree
    return tree

def read_data(filepath):
    with open(filepath, newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        return data

# Pretty print the subtree so that it is easily readable
def print_tree(tree, indent="", file=sys.stdout):
    if isinstance(tree, dict): # Need to check if the tree is a single value yes or no
        for key, val in tree.items():
            print(indent + str(key) + ":", file=file)
            if isinstance(val, dict): # Could be a tree or a single value yes or no
                print_tree(val, indent + "\t", file=file)
            else:
                print(indent + "\t" + str(val), file=file)
    else:
        print(indent + str(tree), file=file)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <datafile.csv> <outputfile.txt>")
        sys.exit(1)
    
    input_filepath = sys.argv[1]
    output_filepath = sys.argv[2]
    data = read_data(input_filepath)
    attributes = list(data[0].keys())
    target_attribute = attributes[-1]  # Assume last column is the target attribute
    attributes.remove(target_attribute)  # Use all other attributes for decision making
    if 'ExampleID' in attributes:
        attributes.remove('ExampleID')  # Remove ExampleID from attributes as it's not used

    # Data is formatted and in expected positions, unnecessary attributes have been removed
    decision_tree = id3(data, attributes, target_attribute)
    
    with open(output_filepath, 'w') as file:
        print_tree(decision_tree, file=file)

if __name__ == "__main__":
    main()
