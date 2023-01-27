import math

def softmax(inputs):
    """
    Calculate the softmax for the give inputs (array)
    :param inputs:
    :return:
    """
    return math.exp(inputs) / float(sum(math.exp(inputs)))
 
 
inputs = [2, 3, 5, 6]
for x in range(inputs):
    print("Softmax Function Output :: {}".format(softmax(inputs[x])))
