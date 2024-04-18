# Sample Data
data = [
    {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'},
    {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'},
    {'Outlook': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'No'},
    {'Outlook': 'Overcast', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'Yes'},
    {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'},
    {'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
    {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'Yes'},
    {'Outlook': 'Overcast', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'Yes'},
    {'Outlook': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'}
]

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

attributes = ['Outlook', 'Temperature', 'Humidity', 'Wind']
target_attribute = 'PlayTennis'
decision_tree = id3(data, attributes, target_attribute)
print(decision_tree)
