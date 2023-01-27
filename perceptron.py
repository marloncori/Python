
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Creating the perceptron class
class Perceptron:
    
    # Initializing the perceptron
    def __init__(self, learning_rate = 0.1, max_epochs = 1000):
        self.learning_rate = learning_rate
        self.max_epochs = max_epochs
        
    # Defining the activation function
    def activation(self, x):
        if x > 0:
            return 1
        else:
            return 0
        
    # Defining the training function
    def train(self, inputs, labels):
        
        # Initializing the weights
        self.weights = np.random.rand(inputs.shape[1])
        
        # Initializing the errors
        errors = []
        
        # Looping through the epochs
        for epoch in range(self.max_epochs):
            
            # Initializing the error
            error = 0
            
            # Looping through the input and label for each epoch
            for input, label in zip(inputs, labels):
                
                # Calculating the output
                output = self.activation(np.dot(input, self.weights))
                
                # Calculating the error
                error += 0.5 * (label - output) ** 2
                
                # Updating the weights
                self.weights += self.learning_rate * (label - output) * input
                
            # Appending the errors
            errors.append(error)
            
        # Returning the errors
        return errors
    
    # Defining the prediction function
    def predict(self, inputs):
        
        # Setting the outputs
        outputs = []
        
        # Looping through the inputs
        for input in inputs:
            
            # Calculating the output
            output = self.activation(np.dot(input, self.weights))
            
            # Appending the output
            outputs.append(output)
            
        # Returning the outputs
        return outputs
    
    # Defining the animation function
    def animate(self, inputs, labels, errors):
        
        # Setting the figure
        fig = plt.figure()
        ax = fig.add_subplot(111)
        line, = ax.plot([], [], lw=2)
        
        # Setting the labels
        ax.set_title("Perceptron Training Animation")
        ax.set_xlabel("Epochs")
        ax.set_ylabel("Error")
        
        # Setting the limits
        ax.set_xlim(0, len(errors))
        ax.set_ylim(0, max(errors))
        
        # Setting the animation
        ani = animation.FuncAnimation(fig, self.update_anim, fargs=(errors, line), frames=len(errors), interval=1000, blit=True)
        
        # Showing the animation
        plt.show()
        
    # Defining the update animation function
    def update_anim(self, i, errors, line):
        line.set_data(np.arange(i+1), errors[0:i+1])
        return line,

# Defining the main function
def main():
    
    # Defining the inputs
    inputs = np.array([
        [1, 0],
        [1, 1],
        [0, 0],
        [0, 1]
    ])
    
    # Defining the labels
    labels = np.array([1, 0, 1, 0])
    
    # Creating the perceptron
    p = Perceptron()
    
    # Training the perceptron
    errors = p.train(inputs, labels)
    
    # Animating the perceptron
    p.animate(inputs, labels, errors)
    
    # Predicting the inputs
    outputs = p.predict(inputs)
    
    # Printing the outputs
    print("Outputs:", outputs)
    
# Calling the main function
if __name__ == "__main__":
    main()