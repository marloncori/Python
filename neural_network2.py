import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

class NeuralNetwork:
    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],4) 
        self.weights2   = np.random.rand(4,1)                 
        self.y          = y
        self.output     = np.zeros(y.shape)
        
    def sigmoid(self, x, deriv=False):
        if(deriv==True):
            return x*(1-x)
        return 1/(1+np.exp(-x))
    
    def feedforward(self):
        self.layer1 = self.sigmoid(np.dot(self.input, self.weights1))
        self.output = self.sigmoid(np.dot(self.layer1, self.weights2))
        return self.output
        
    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * self.sigmoid(self.output, deriv=True)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * self.sigmoid(self.output, deriv=True), self.weights2.T) * self.sigmoid(self.layer1, deriv=True)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def get_loss(self):
        loss = np.mean(np.square(self.y - self.output))
        return loss

# is it even or uneven?
x = 5
y = 1
nn = NeuralNetwork(x,y)

# animated plot of the training process
fig, ax = plt.subplots(figsize=(6,3))
ax.scatter(x, y)

line, = ax.plot([], [], lw=2)

ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.grid()
xdata, ydata = [], []

def init():
    line.set_data([], [])
    return line,

def animate(i):
    nn.feedforward()
    nn.backprop()
    xdata.append(nn.input)
    ydata.append(nn.output)
    line.set_data(xdata, ydata)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

plt.show()

nn.feedforward()
print("final output: ", nn.output)
print("final loss: ", nn.get_loss())