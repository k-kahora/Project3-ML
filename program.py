import sys
import csv
from math import log2

def entropy(subset):
    total = len(subset)
    if total == 0:
        return 0
    yes = sum(1 for item in subset if item['PlayTennis'] == 'Yes')
    no = total - yes
    p_yes = yes / total
    p_no = no / total
    entropy_yes = -p_yes*log2(p_yes) if p_yes > 0 else 0
    entropy_no = -p_no*log2(p_no) if p_no > 0 else 0
    return entropy_yes + entropy_no

def info_gain(data, attribute):
    total_entropy = entropy(data)
    attribute_values = set(item[attribute] for item in data)
    weighted_entropy = 0
    for value in attribute_values:
        subset = [item for item in data if item[attribute] == value]
        weighted_entropy += (len(subset) / len(data)) * entropy(subset)
    return total_entropy - weighted_entropy

def id3(data, attributes, target_attribute):
    target_values = set(item[target_attribute] for item in data)
    if len(target_values) == 1:
        return next(iter(target_values))  # All examples are the same class
    if not attributes:
        return max(target_values, key=lambda val: sum(item[target_attribute] == val for item in data))
    best_attribute = max(attributes, key=lambda attr: info_gain(data, attr))
    tree = {best_attribute: {}}
    attributes = [attr for attr in attributes if attr != best_attribute]
    for value in set(item[best_attribute] for item in data):
        subset = [item for item in data if item[best_attribute] == value]
        subtree = id3(subset, attributes, target_attribute)
        tree[best_attribute][value] = subtree
    return tree

def read_data(filepath):
    with open(filepath, newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        return data

def print_tree(tree, indent="", file=sys.stdout):
    if isinstance(tree, dict):
        for key, val in tree.items():
            print(indent + str(key) + ":", file=file)
            if isinstance(val, dict):
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
    attributes.remove('PlayTennis')
    attributes.remove('ExampleID')  # Assuming we don't want to use ExampleID as an attribute

    decision_tree = id3(data, attributes, 'PlayTennis')
    
    with open(output_filepath, 'w') as file:
        print_tree(decision_tree, file=file)

if __name__ == "__main__":
    main()
