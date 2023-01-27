import math

def sigmoid(inputs):
    """
    Calculate the sigmoid for the give inputs (array)
    :param inputs:
    :return:
    """
    sigmoid_scores = [1 / float(1 + math.exp(- x)) for x in inputs]
    return sigmoid_scores
 
 
sigmoid_inputs = [2, 3, 5, 6]
print("Sigmoid Function Output :: {}".format(sigmoid(sigmoid_inputs)))
