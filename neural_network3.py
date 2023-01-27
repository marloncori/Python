import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Neuron Class
class Neuron():
    # Constructor
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
    
    # Activation Function
    def activation_function(self, x):
        # Step Function
        return np.heaviside(np.dot(self.weights, x) + self.bias, 1)

# Neural Network Class
class NeuralNetwork():
    # Constructor
    def __init__(self, input_layer_size, hidden_layer_size, output_layer_size):
        # Input Layer
        self.input_layer_size = input_layer_size
        self.hidden_layer_size = hidden_layer_size
        self.output_layer_size = output_layer_size
        # Weights
        self.weights_input_to_hidden = np.random.randn(self.hidden_layer_size, self.input_layer_size)
        self.weights_hidden_to_output = np.random.randn(self.output_layer_size, self.hidden_layer_size)
        # Bias
        self.bias_input_to_hidden = np.random.randn(self.hidden_layer_size, 1)
        self.bias_hidden_to_output = np.random.randn(self.output_layer_size, 1)
    
    # Forward Propagation
    def forward_propagation(self, input_data):
        # Input Layer
        self.input_layer_data = input_data
        # Hidden Layer
        self.hidden_layer_data = np.array([Neuron(self.weights_input_to_hidden[i], self.bias_input_to_hidden[i]).activation_function(self.input_layer_data) for i in range(self.hidden_layer_size)]).reshape(self.hidden_layer_size, 1)
        # Output Layer
        self.output_layer_data = Neuron(self.weights_hidden_to_output, self.bias_hidden_to_output).activation_function(self.hidden_layer_data)
        return self.output_layer_data
    
    # Plot Graph
    def plot_graph(self):
        # Create Figure
        fig = plt.figure(figsize=(6, 4))
        # Input Layer
        ax1 = fig.add_subplot(221)
        ax1.set_title('Input Layer')
        ax1.scatter(self.input_layer_data, [0 for _ in range(self.input_layer_size)])
        # Hidden Layer
        ax2 = fig.add_subplot(222)
        ax2.set_title('Hidden Layer')
        ax2.scatter(self.hidden_layer_data, [0 for _ in range(self.hidden_layer_size)])
        # Output Layer
        ax3 = fig.add_subplot(223)
        ax3.set_title('Output Layer')
        ax3.scatter(self.output_layer_data, [0])
        # Show Figure
        plt.show()
    
    # Animate Graph
    def animate_graph(self, input_data):
        # Create Figure
        fig = plt.figure(figsize=(6, 4))
        # Input Layer
        ax1 = fig.add_subplot(221)
        ax1.set_title('Input Layer', fontsize=14)
        ax1.set_xlim([-3, 3])
        ax1.set_ylim([-1, 3])
        ax1.scatter([], [])
        # Hidden Layer
        ax2 = fig.add_subplot(222)
        ax2.set_title('Hidden Layer', fontsize=14)
        ax2.set_xlim([-3, 3])
        ax2.set_ylim([-1, 3])
        ax2.scatter([], [])
        # Output Layer
        ax3 = fig.add_subplot(223)
        ax3.set_title('Output Layer', fontsize=14)
        ax3.set_xlim([-3, 3])
        ax3.set_ylim([-1, 3])
        ax3.scatter([], [])
        # Animate Function
        def animate(i):
            # Input Layer
            ax1.scatter(input_data[i], [0 for _ in range(self.input_layer_size)])
            # Hidden Layer
            self.hidden_layer_data = np.array([Neuron(self.weights_input_to_hidden[j], self.bias_input_to_hidden[j]).activation_function(input_data[i]) for j in range(self.hidden_layer_size)]).reshape(self.hidden_layer_size, 1)
            ax2.scatter(self.hidden_layer_data, [0 for _ in range(self.hidden_layer_size)])
            # Output Layer
            self.output_layer_data = Neuron(self.weights_hidden_to_output, self.bias_hidden_to_output).activation_function(self.hidden_layer_data)
            ax3.scatter(self.output_layer_data, [0])
            # Return Scatter
            return ax1.collections + ax2.collections + ax3.collections
        # Create Animation
        anim = FuncAnimation(fig, animate, frames=len(input_data), interval=50, blit=True)
        # Show Animation
        plt.show()

# Main Function
def main():
    # Input Layer Size
    input_layer_size = 5
    # Hidden Layer Size
    hidden_layer_size = 3
    # Output Layer Size
    output_layer_size = 1
    # Create Neural Network
    nn = NeuralNetwork(input_layer_size, hidden_layer_size, output_layer_size)
    # Input Data, is it positive or negative?
    input_data = np.array([-2, -1, 0, 1, 2]).reshape(input_layer_size, 1)
    # Forward Propagation
    output_data = nn.forward_propagation(input_data)
    # Print Output Data
    print('Output Data:', output_data)
    # Plot Graph
    nn.plot_graph()
    # Animate Graph
    nn.animate_graph(input_data)

# Call Main
if __name__ == '__main__':
    main()