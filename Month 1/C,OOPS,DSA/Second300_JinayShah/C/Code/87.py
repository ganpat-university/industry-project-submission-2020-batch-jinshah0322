class CobwebNode:
    def __init__(self, features=None, examples=None, children=None):
        self.features = features if features is not None else {}
        self.examples = examples if examples is not None else []
        self.children = children if children is not None else []

    def is_leaf(self):
        return not bool(self.children)


def cobweb_update(node, example, category_utility):
    if node.is_leaf():
        node.features = update_features(node.features, example)
        node.examples.append(example)
    else:
        best_child = find_best_matching_child(node.children, example, category_utility)
        cobweb_update(best_child, example, category_utility)


def find_best_matching_child(children, example, category_utility):
    best_child = None
    max_utility = float('-inf')

    for child in children:
        utility = calculate_category_utility(child.features, example, category_utility)
        if utility > max_utility:
            max_utility = utility
            best_child = child

    return best_child


def calculate_category_utility(features, example, category_utility):
    utility = 0.0
    for feature, value in example.items():
        if feature in features:
            utility += category_utility(features[feature], value)

    return utility


def update_features(old_features, example):
    new_features = old_features.copy()
    for feature, value in example.items():
        if feature in new_features:
            count, mean, variance = new_features[feature]
            new_count = count + 1
            new_mean = (count * mean + value) / new_count
            new_variance = ((count - 1) *variance + (value - mean) *(value - new_mean)) / new_count
            new_features[feature] = (new_count, new_mean, new_variance)
        else:
            new_features[feature] = (1, value, 0.0)

    return new_features


def cobweb_incremental_learning(root, examples, category_utility):
    for example in examples:
        cobweb_update(root, example, category_utility)

root_node = CobwebNode()

example1 = {"feature1": 3.5, "feature2": 1.2}
example2 = {"feature1": 4.0, "feature2": 1.0}
example3 = {"feature1": 2.8, "feature2": 0.8}

def category_utility(feature_stats, value):
    _, mean, variance = feature_stats
    if variance == 0.0:
        return 1.0 if mean == value else 0.0
    else:
        z_score = (value - mean) / (variance ** 0.5)
        return 1.0 - abs(z_score)

cobweb_incremental_learning(root_node, [example1, example2, example3], category_utility)

print("Cobweb Tree:")
print(root_node.features)