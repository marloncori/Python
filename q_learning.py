
"""
 This code is implementing a reinforcement learning algorithm called Q-learning. In reinforcement learning, an agent learns to interact with an environment in order to maximize a reward signal.
In this particular code, the agent is learning to navigate a grid and find the optimal path to a goal. It receives rewards for reaching the goal, and can choose from a set of actions (e.g. up, down, left, right) at each step to move through the grid.
The Q-learning algorithm uses a Q-table to store the values of taking each action in each state. At each step, the agent chooses the action with the highest expected future reward, based on the values in the Q-table. The values in the Q-table are updated after each step using the Q-learning update rule, which takes into account the reward received, the value of the next state, and the current value of the state-action pair.
Through this process, the agent learns the optimal actions to take in each state in order to maximize the cumulative reward.

 The optimal path will depend on the values of the rewards in the grid and the parameters of the Q-learning algorithm (i.e. the learning rate alpha and the discount factor gamma).
 The blue cells in the plot represent the cells in the grid that the agent can visit and make actions from. The shades of blue represent the values of the actions in each cell, as determined by the create_matrix method I provided earlier. For example, a cell with a value of 9 (1 + 8) represents a cell where the agent can take the actions 'U' (up) and 'R' (right).
 To find the optimal path, you can run the Q-learning algorithm for a sufficient number of iterations, then use the Q-table to determine the optimal action to take at each step. You can do this by iterating over the states in the grid and choosing the action with the highest Q-value for each state.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.animation as animation

# Define the environment
class Grid:
    def __init__(self, rows, cols, start):
        self.rows = rows
        self.cols = cols
        self.i = start[0]
        self.j = start[1]
        self.state = start

    def set_state(self, state):
        self.state = state
        
    def set_reward(self, reward, new_state):
        self.rewards = reward
        self.new_state = new_state

    def set_actions(self, action):
        self.actions = action

    def current_state(self):
        return (self.i, self.j)

    def is_terminal(self, s):
        return s not in self.actions

    def get_next_state(self, s, a):
        i, j = s[0], s[1]

        if (i, j) in self.actions and a in self.actions[(i, j)]:
            if a == 'U':
                i -= 1
            elif a == 'D':
                i += 1
            elif a == 'R':
                j += 1
            elif a == 'L':
                j -= 1
        else:
            print(" Action not found in actions dict.")
        return (i, j)

    def move(self, action):
        if (self.i, self.j) in self.actions:
            if action in self.actions[(self.i, self.j)]:
                if action == 'U':
                    self.i -= 1
                elif action == 'D':
                    self.i += 1
                elif action == 'R':
                    self.j += 1
                elif action == 'L':
                    self.j -= 1
            else:
                pass
        else:
            pass  
        return self.rewards.get((self.i, self.j), 0)

    def undo_move(self, action):
        if action == 'U':
            self.i += 1
        elif action == 'D':
            self.i -= 1
        elif action == 'R':
            self.j -= 1
        elif action == 'L':
            self.j += 1
        assert (self.current_state() in self.all_states())

    def game_over(self):
        return (self.i, self.j) not in self.actions

    def all_states(self):
        return list(self.actions.keys()) + list(self.rewards.keys())

    def create_matrix(self):
        # Initialize the matrix with zeros
        matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        # Set rewards in matrix
        for (i, j), reward in self.rewards.items():
            matrix[i][j] = reward

        # Set actions in matrix
        for (i, j), actions in self.actions.items():
            if 'U' in actions:
                matrix[i][j] += 1
            if 'D' in actions:
                matrix[i][j] += 2
            if 'L' in actions:
                matrix[i][j] += 4
            if 'R' in actions:
                matrix[i][j] += 8
        return matrix
    
# Define the q-learning algorithm
class Qlearning:
    def __init__(self, grid, alpha, gamma):
        self.alpha = alpha
        self.gamma = gamma
        self.grid = grid
        self.q_table = {}
        self.state = self.grid.state
        self.create_q_table()

    def create_q_table(self):
        for state in self.grid.all_states():
            if state in self.grid.actions:
                self.q_table[state] = {}
                for action in self.grid.actions[state]:
                    self.q_table[state][action] = 0
            else:
                pass
            
    def get_max_q_value(self, state):
        max_q = -np.inf
        if state in self.grid.actions:
            for action in self.grid.actions[state]:
                q_value = self.q_table[state][action]
                if q_value > max_q:
                    max_q = q_value
        else:
            pass
        return max_q

    def get_max_q_action(self, state):
        max_action = None
        max_q = -np.inf
        for action in self.grid.actions[state]:
            q_value = self.q_table[state][action]
            if q_value > max_q:
                max_q = q_value
                max_action = action
        return max_action

    def get_action(self, state):
        best_action = None
        if np.random.uniform(0, 1) < self.epsilon:
            best_action = np.random.choice(self.grid.actions[state])
        else:
            best_action = self.get_max_q_action(state)
        return best_action

    def update_q_table(self, state, action, reward, new_state):
        if (state, action) in self.q_table:
            q_value = self.q_table[state][action]
            max_q = self.get_max_q_value(new_state)
            new_q_value = q_value + self.alpha * (
                    reward + self.gamma * max_q - q_value)
            self.q_table[state][action] = new_q_value
        else:
            pass
        
    def train(self):
        self.epsilon = 0.5
        self.decay_rate = 0.005
        self.episodes = 100000

        for episode in range(self.episodes):
            self.state = self.grid.state
            done = False
            while not done:
                action = self.get_action(self.state)
                reward = self.grid.move(action)
                new_state = self.grid.current_state()
                self.update_q_table(self.state, action, reward, new_state)
                self.state = new_state
                done = self.grid.game_over()
            self.epsilon = self.epsilon - self.decay_rate
            if episode % 700 == 0:
                print(f"[TRAINING] eposide: {episode}")

    def get_best_action(self, state):
        return self.get_max_q_action(state)

    
    def test(self, state):
        """
        Test the q-learning implementation by starting from the given state and
        following the action with the highest q-value until a terminal state is reached.
        """
        while True:
            # Get the action with the highest q-value for the current state
            action = self.get_max_q_action(state)

            # Get the reward for taking the action and the new state after taking the action
            reward = self.grid.move(action)
            new_state = self.grid.current_state()

            # Print the current state, action taken, reward received, and new state
            print(f"State: {state}, Action: {action}, Reward: {reward}, New state: {new_state}")

            # Check if the new state is a terminal state
            if self.grid.is_terminal(new_state):
                break

            # Update the current state to the new state
            state = new_state
            
# Visualize the process
def visualize_process(grid, q):
    # Define the starting state
    grid.set_state(grid.state)
    # Define the layout
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # Define the matrices
    matrices = []
    # Define the frames
    frames = []
    # Define the states
    states = []
    # Define the rewards
    rewards = []
    # Define the ended states
    ended_states = []
    # Iterate over each action
    for action in q.grid.actions:
        # Get the new state
        new_state = q.grid.get_next_state(grid.current_state(), action)
        # Append the states
        states.append(new_state)
        # Append the rewards
        rewards.append(q.grid.rewards.get(new_state))
        # Append the ended states
        ended_states.append(q.grid.is_terminal(new_state))
        # Append the frames
        state_action_matrix = grid.create_matrix()
        frames.append([ax.imshow(state_action_matrix, interpolation='none',
                                 cmap=plt.get_cmap('Blues'))])
        # Append the matrices
        matrices.append(state_action_matrix)
    # Animate the process
    ani = animation.ArtistAnimation(fig, frames, interval=400,
                                    blit=True, repeat_delay=1000)
    # Show the animation
    plt.show()


# Define the main function
def main():
    # Define the grid
    rows2, cols2 = 5, 5
    start1 = (3,0)
    rows, cols = 3, 4
    
    grid = Grid(rows2, cols2, start=start1)
    # Define the rewards
    rewards = {
        (0, 3): 1,
        (1, 3): -1
    }
    # Define the actions
    actions = {
        (0, 0): ('D', 'R'),
        (0, 1): ('L', 'R'),
        (0, 2): ('L', 'D', 'R'),
        (0, 3): ('D', 'L'),
        (1, 0): ('U', 'D'),
        (1, 2): ('U', 'D', 'R'),
        (1, 3): ('D', 'U', 'L'),
        (2, 0): ('U', 'R'),
        (2, 1): ('L', 'R'),
        (2, 2): ('L', 'R', 'U'),
        (2, 3): ('D',),
        (2, 4): ('L', 'R'),
        (3, 0): ('U',),
        (3, 2): ('U', 'D', 'R'),
        (3, 3): ('R',),
        (3, 4): ('U', 'L', 'R'),
        (4, 0): ('U', 'R'),
        (4, 1): ('L', 'R'),
        (4, 2): ('L', 'R', 'U'),
        (4, 3): ('L', 'U'),
    }
    actions2 = {
    (0, 0): ['R', 'D'],
    (0, 1): ['L', 'R'],
    (0, 2): ['L', 'D', 'R'],
    (1, 0): ['U', 'D'],
    (1, 2): ['U', 'D'],
    (2, 0): ['U', 'R'],
    (2, 1): ['L', 'R'],
    (2, 2): ['L', 'U'],
    (2, 3): ['L']  # Add key (2, 3)
}
    # Set the rewards
    grid.set_reward(rewards, (4, 3))
    # Set the actions
    grid.set_actions(actions)
    # Define the q-learning algorithm
    # Create the Q-learning algorithm
    qlearning = Qlearning(grid, alpha=0.5, gamma=0.9)
    # Train the Q-learning algorithm
    qlearning.train()

    # Test the Q-learning algorithm
    qlearning.test((2, 0))
    
    visualize_process(grid, qlearning)

if __name__ == '__main__':
    main()