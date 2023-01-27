import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class DecisionTree:

    def __init__(self):
        self.data = None
        self.target = None
        self.features = None
        self.tree = None
        self.visual = []

    def prepare_data(self, data, target, features):
        """
        This function prepare the data for the tree
        :param data: data set
        :param target: target variable
        :param features: list of all features
        :return:
        """
        self.data = data
        self.target = target
        self.features = features

    def entropy(self, target_col):
        """
        This function calculate the entropy of the target variable
        :param target_col: target variable
        :return: entropy
        """
        elements, counts = np.unique(target_col, return_counts=True)
        entropy = np.sum(
            [-(counts[i] / np.sum(counts)) * np.log2(counts[i] / np.sum(counts)) for i in range(len(elements))])
        return entropy

    def InfoGain(self, data, split_attribute_name, target_name="class"):
        """
        This function calculate the information gain of the split attribute
        :param data: data set
        :param split_attribute_name: split attribute name
        :param target_name: target variable name
        :return: information gain
        """
        # Calculate the entropy of the total dataset
        total_entropy = self.entropy(data[target_name])

        # Calculate the values and the corresponding counts for the split attribute
        vals, counts = np.unique(data[split_attribute_name], return_counts=True)

        # Calculate the weighted entropy
        Weighted_Entropy = np.sum(
            [(counts[i] / np.sum(counts)) * self.entropy(data.where(data[split_attribute_name] == vals[i]).dropna()[target_name])
            for i in range(len(vals))])

        # Calculate the information gain
        Information_Gain = total_entropy - Weighted_Entropy
        return Information_Gain

    def ID3(self, data, originaldata, features, target_attribute_name="class", parent_node_class=None):
        """
        This function uses the ID3 algorithm to build the decision tree
        :param data: data set
        :param originaldata: original data set
        :param features: list of features
        :param target_attribute_name: target variable name
        :param parent_node_class: parent node
        :return:
        """

        # Define the stopping criteria --> If one of this is satisfied, we want to return a leaf node#

        # If all target_values have the same value, return this value
        if len(np.unique(data[target_attribute_name])) <= 1:
            return np.unique(data[target_attribute_name])[0]

        # If the dataset is empty, return the mode target feature value in the original dataset
        elif len(data) == 0:
            return np.unique(originaldata[target_attribute_name])[
                np.argmax(np.unique(originaldata[target_attribute_name], return_counts=True)[1])]

        # If the feature space is empty, return the mode target feature value of the direct parent node --> Note that
        # the direct parent node is that node which has called the current run of the ID3 algorithm and hence
        # the mode target feature value is stored in the parent_node_class variable.

        elif len(features) == 0:
            return parent_node_class

        # If none of the above holds true, grow the tree!

        else:
            # Set the default value for this node --> The mode target feature value of the current node
            parent_node_class = np.unique(data[target_attribute_name])[
                np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])]

            # Select the feature which best splits the dataset
            item_values = [self.InfoGain(data, feature, target_attribute_name) for feature in features]  # Return the information gain values for the features in the dataset
            best_feature_index = np.argmax(item_values)
            best_feature = features[best_feature_index]

            # Create the tree structure. The root gets the name of the feature (best_feature) with the maximum information
            # gain in the first run
            tree = {best_feature: {}}

            # Remove the feature with the best inforamtion gain from the feature space
            features = [i for i in features if i != best_feature]

            # Grow a branch under the root node for each possible value of the root node feature

            for value in np.unique(data[best_feature]):
                value = value
                # Split the dataset along the value of the feature with the largest information gain and therwith create sub_datasets
                sub_data = data.where(data[best_feature] == value).dropna()

                # Call the ID3 algorithm for each of those sub_datasets with the new parameters --> Here the recursion comes in!
                subtree = self.ID3(sub_data, originaldata, features, target_attribute_name, parent_node_class)

                # Add the sub tree, grown from the sub_dataset to the tree under the root node
                tree[best_feature][value] = subtree

            self.visual.append(tree)
            return tree
        

    def fit(self):
        """
        This function fit the decision tree
        :return:
        """
        self.tree = self.ID3(self.data, self.data, self.features, self.target)

    def predict(self, data):
        """
        This function predict the target variable using the decision tree
        :param data: data set
        :return: prediction
        """
        prediction = 0
        # Predicts the classification on a given node
        if isinstance(self.tree, dict):
            node_key = next(iter(self.tree))
            node_value = self.tree[node_key]
            vals = data[node_key]

            for key in node_value.keys():
                if vals == key:
                    if isinstance(node_value[key], dict):
                        prediction = self.predict(data)
                    else:
                        prediction = node_value[key]
        return prediction

    def visualize(self):
        """
        This function visualize the decision tree
        :return:
        """
        def update_tree(num):
            ax.cla()
            ax.axis('off')
            ax.set_title('Decision Tree')
            tree_plot(self.visual[num], (0, 0), 40, ax)

        def tree_plot(tree, start_point, length, ax):
            if isinstance(tree, dict):
                tree_keys = list(tree.keys())
                if tree_keys[0] == 'leaf':
                    ax.text(start_point[0], start_point[1], str(tree['leaf']),
                            horizontalalignment='center', verticalalignment='center', fontsize=20)
                else:
                    tree_key = tree_keys[0]
                    tree_value = tree[tree_key]
                    ax.text(start_point[0], start_point[1], str(tree_key),
                            horizontalalignment='center', verticalalignment='center', fontsize=20)
                    for key in tree_value.keys():
                        if isinstance(tree_value[key], dict):
                            if start_point[1] - 25 > 0:
                                tree_plot(tree_value[key], [start_point[0] - (length / 2), start_point[1] - 25],
                                          length / 2, ax)
                            else:
                                tree_plot(tree_value[key], [start_point[0] - (length / 2), start_point[1] + 25],
                                          length / 2, ax)
                            ax.plot([start_point[0], start_point[0] - (length / 2)], [start_point[1],
                                                                                  start_point[1] - 25], linestyle='dotted')
                            ax.text(start_point[

    def train(self):
        self.tree = self.ID3(self.data, self.data, self.features, self.target)
        print("Decision Tree trained successfully!")
    
    def predict(self, sample):
        # get the root node of the tree
        root = list(self.tree.keys())[0]

        # get the subtree for the root node
        subtree = self.tree[root]

        # get the value of the root node
        value = sample[root]

        # navigate through the tree until we reach a leaf node or a node with only one child node
        while isinstance(subtree, dict):
            root = list(subtree.keys())[0]
            value = sample[root]
            subtree = subtree[value]

        return subtree

    def plot_tree(self):
        def visual_tree(tree, level=0):
            if isinstance(tree, dict):
                self.visual.append({"type": "node", "feature": list(tree.keys())[0], "children": len(tree[list(tree.keys())[0]]), "level": level})
                for key in tree.keys():
                    visual_tree(tree[key], level+1)
            else:
                self.visual.append({"type": "leaf", "class": tree, "level": level})

        visual_tree(self.tree)
        max_level = max([i["level"] for i in self.visual])
        y = 0.5
        for i in self.visual:
            if i["type"] == "node":
                plt.text(i["level"]*1.5, y, i["feature"], ha="center", va="center", fontsize=14)
                if i["children"] > 1:
                    y -= 0.5
            else:
                plt.text(i["level"]*1.5, y, i["class"], ha="center", va="center", bbox=dict(facecolor='red', alpha=0.5), fontsize=14)
                if y + 0.5 < max_level:
                    y += 0.5

        plt.axis("off")
        plt.show()


def test(self, test_data):
    results = []
    for i in range(len(test_data)):
        result = self.predict(test_data.iloc[i])
        results.append(result)
return results

def main():
    # Load the data set
    data = pd.read_csv("data.csv")
        # Shuffle the data set
    data = data.sample(frac=1).reset_index(drop=True)

    # Split the data set into training and testing data
    training_data = data.iloc[:int(0.8*len(data))]
    testing_data = data.iloc[int(0.8*len(data)):]

    # Create a Decision Tree classifier
    clf = DecisionTree()

    # Prepare the data for the decision tree
    clf.prepare_data(training_data, "class", ["age", "income", "student", "credit_rating"])

    # Train the decision tree
    clf.train()

if __name__ == '__main__:
# Test the decision tree
    results = clf.test(testing_data)

    # Calculate the accuracy of the decision tree
    accuracy = np.sum(results == testing_data["class"]) / len(testing_data)
    print("Accuracy:", accuracy)

    # Plot the decision tree
    clf.plot_tree()
