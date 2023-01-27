import matplotlib.pyplot as plt
import numpy as np
import time
import math
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

"""from skimage import io
from skimage.draw import circle_perimeter
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import  label2rgb
from skimage.filters import threshold_otsu
from skimage.draw import circle, line
from skimage.transfrom import rotate

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

from IPython.display import HTML
from IPython.display import display

"""
from collections import deque

import heapq
import random

"""
%matplotlib notebook
"""
        
class Grid:
    def __init__(self, grid, start=None, end=None, obstacles=None, columns=0, rows=0, margin=None):
        self.grid = grid
        self.start = start
        self.end = end
        self.obstacles = obstacles
        self.columns = columns
        self.rows = rows
        self.margin = margin
        
        self.path = []
        self.fig, self.ax = plt.subplots()
        self.ax.imshow(self.grid, cmap="Greys", origin="lower")
        self.patch = patches.Rectangle((0,0),1,1,linewidth=1,edgecolor='r',facecolor='none')
        self.ax.add_patch(self.patch)
        self.ax.set_title('SVG+A* Grid Search')
        plt.show()
        
    def set_start(self, i, j):
        self.start = (i,j)
        self.grid[i][j] = 1
    
    def set_end(self, i, j):
        self.end = (i, j)
        self.grid[i][j] = 1
    
    def set_obstacles(self,i,j):
        self.obstacles.append((i,j))
        self.grid[i][j] = 1
    
    def in_bounds(self, idx):
        (x, y) = idx
        return 0 <= x < self.columns and 0 <= y < self.rows

    def passable(self, idx):
        (x, y) = idx
        return self.grid[x][y] != 1
    
    def neighbours(self, idx):
        (x, y) = idx
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x+y) % 2 == 0: results.reverse() # aesthetic
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results
    
    def distance(self, a, b):
        (x1, y1) = a
        (x2, y2) = b
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    def heuristic(self, a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1-x2) + abs(y1-y2)
    
    def rebuild_path(self, came_from, current):
        total_path = [current]
        while current in came_from.keys():
            current = came_from[current]
            total_path.append(current)
        return total_path
    
    def astar(self):
        open_set = set()
        open_heap = []
        closed_set = set()
        came_from = {}
        
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start, self.end)}
        
        heapq.heappush(open_heap, (f_score[self.start], self.start))
        open_set.add(self.start)
        
        while open_set:
            current = heapq.heappop(open_heap)[1]
            
            if current == self.end:
                self.path = self.rebuild_path(came_from, current)
                return self.path
            
            open_set.remove(current)
            closed_set.add(current)
            
            for neighbor in self.neighbours(current):
                if neighbor in closed_set:
                    continue
                tentative_g_score = g_score[current] + self.distance(current, neighbor)
                
                if neighbor not in open_set:
                    open_set.add(neighbor)
                    tentative_is_better = True
                
                elif tentative_g_score < g_score[neighbor]:
                    tentative_is_better = True
                else:
                    tentative_is_better = False
                
                if bool(tentative_is_better):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, self.end)
                    heapq.heappush(open_heap, (f_score[neighbor]), neighbor)
                
        return came_from

    def animate(self, i):
        self.patch.set_xy([self.path[i]])
    
    def show_animation(self):
        anim = FuncAnimation(self.fig, self.animate, frames=len(self.path), interval=100, repeat=False)
        #return HTML(anim.to_html5_video())
        plt.show()
        
    def show_grid(self):
        self.ax.imshow(self.grid, cmap="Greys", origin="lower")
        plt.show()
    
    def show_path(self):
        self.ax.plot([i[0] for i in self.path], [i[1] for i in self.path], '-o')
        plt.show()


class Visualization:
    def __init__(self):
        params = [
            ['Add Obstacles', 'danger', '50%', '50px'],
            ['Set Start', 'success', '50%', '50px'],
            ['Set End', 'success', '50%', '50px'],
            ['Run SVG+A*', 'info', '50%', '50px'],
            ['Show Grid', 'warning', '50%', '50px'],
            ['Show Path', 'warning', '50%', '50px'],
            ['Show Animation', 'warning', '50%', '50px'],
        ]
        button = {
            'w0': None,'w1': None,'w2': None,'w3': None,'w4': None,'w5': None,'w6': None,
        }
        
    def display_buttons(self):
        style = {'description_width': 'initial'}
        i = 0
        for val in self.button.values():
            val = widgets.Button(description=self.params[i][0], button_style=self.params[i][1],
                                 layout=widgets.Layout(width=self.params[i][2], height=self.params[i][3]),
                                 style=style)
            i += 1
        display(widgets.HBox((self.button['w0'],self.button['w1'],self.button['w2'],
                              self.button['w3'],self.button['w4'],self.button['w5'],
                              self.button['w6'])))
        
    def on_click(self, event, grid):
        global start_set, end_set
        if event.xdata and event.ydata:
            i, j = int(event.xdata), int(event.ydata)
            if self.button['w0'].style.button_color == 'danger':
                grid.set_obstacles(i, j)

                grid.show_grid()
            elif self.button['w1'].style.button_color == 'success':
                grid.set_start(i, j)

grid = Grid(np.zeros((20, 20)), start=(0, 0), end=(19, 19), obstacles=[(1,1), (2,2), (3,3)])
 
def update(i):
    global grid
    # Run the A* algorithm for a single step
    came_from, _, a_star_open, a_star_closed = grid.step()
    path = grid.astar()
    #grid.show_animation()
   
    # Clear the plot
    grid.patch.set_visible(False)
    for collection in grid.path_collection.collections:
        collection.set_visible(False)
        
    # Draw the updated path and open/closed sets
    path = grid.rebuild_path(came_from, grid.end)
    grid.path_collection = grid.ax.scatter([point[1] for point in path], [point[0] for point in path], c='r', s=10)
    grid.open_collection = grid.ax.scatter([point[1] for point in a_star_open], [point[0] for point in a_star_open], c='g', s=10)
    grid.closed_collection = grid.ax.scatter([point[1] for point in a_star_closed], [point[0] for point in a_star_closed], c='b', s=10)
    
    return grid.patch, grid.path_collection, grid.open_collection, grid.closed_collection

def main():
    global grid
    # Initialize the FuncAnimation object
    animation = FuncAnimation(grid.fig, update, frames=np.arange(0, 100), interval=100)
    # Start the animation
    plt.show()


if __name__ == "__main__":
    main()
    
    """
class Grid:
    def __init__(self, grid, start=None, end=None, obstacles=None, columns=0, rows=0, margin=None):
        # Initialize the grid, start, end, and obstacles
        self.grid = grid
        self.start = start
        self.end = end
        self.obstacles = obstacles
        self.columns = columns
        self.rows = rows
        self.margin = margin
        
        # Initialize the path and figure
        self.path = []
        self.fig, self.ax = plt.subplots()
        
        # Initialize the patch and collections for the path, open set, and closed set
        self.patch = patches.Rectangle((0,0),1,1,linewidth=1,edgecolor='r',facecolor='none')
        self.path_collection = None
        self.open_collection = None
        self.closed_collection = None
        
        # Initialize the open and closed sets for A*
        self.open_set = set()
        self.closed_set = set()
        
        # Initialize the came_from dictionary for A*
        self.came_from = {}
        
        # Display the grid and set the title
        self.ax.imshow(self.grid, cmap="Greys", origin="lower")
        self.ax.add_patch(self.patch)
        self.ax.set_title('SVG+A* Grid Search')
        plt.show()
        
    def step(self):
        # Check if the open set is empty, in which case the algorithm has finished
        if not self.open_set:
            return self.came_from, None, self.open_set, self.closed_set
        
        # Find the node in the open set with the lowest f-score
        current = min(self.open_set, key=lambda x: self.f_score[x])
        
        # If the current node is the end, reconstruct the path and return the came_from dictionary
        if current == self.end:
            self.path = self.rebuild_path(self.came_from, self.end)
            return self.came_from, self.path, self.open_set, self.closed_set
        
        # Remove the current node from the open set and add it to the closed set
        self.open_set.remove(current)
        self.closed_set.add(current)
        
        # Check the neighbours of the current node
        for neighbour in self.neighbours(current):
            # Skip the neighbour if it's already in the closed set
            if neighbour in self.closed_set:
                continue
            
            # Calculate the tentative g-score for the neighbour
            tentative_g_score = self.g_score[current] + self.distance(current, neighbour)
            
            # If the neighbour is not in the open set, or if the tentative g-score is lower than the current g-score, update the came_from, g-score, and f-score values
            if neighbour not in

"""