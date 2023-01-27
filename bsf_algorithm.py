
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class BreadthSearchFirst:
    def __init__(self):
        self.iterations = 0
        
    # Finding the starting node
    def find_start(self, graph):
        start_node = None
        for node in graph.keys():
            if graph[node][1] == 0:
                start_node = node
        return start_node
    
    # Finding the goal node
    def find_goal(self, graph):
        goal_node = None
        for node in graph.keys():
            if graph[node][1] == 1:
                goal_node = node
        return goal_node
    
    # Finding all the neighbors of the current node
    def find_neighbors(self, graph, start_node):
        neighbors = []
        for node in graph[start_node][0]:
            neighbors.append(node)
        return neighbors
    
    # Finding the path from the start node to the goal node
    def find_path(self, graph, start_node, goal_node):
        queue = [start_node]
        visited = []
        path = []
        if start_node == goal_node:
            return 0
        while len(queue) > 0:
            self.iterations += 1
            path.append(start_node)
            node = queue.pop(0)
            if node == goal_node:
                path.append(node)
                return path
            else:
                if node not in visited:
                    neighbors = self.find_neighbors(graph, node)
                    visited.append(node)
                    for neighbor in neighbors:
                        queue.append(neighbor)
                        start_node = neighbor
        return 0
    
    # Drawing the graph
    def draw_graph(self, graph):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_title('Graph')
        ax.set_xlim(0, 3)
        ax.set_ylim(0, 3)
        ax.grid()
        start_node = self.find_start(graph)
        goal_node = self.find_goal(graph)
        for node in graph.keys():
            ax.scatter(graph[node][0][0], graph[node][0][1], s=100, color='blue')
            ax.text(graph[node][0][0], graph[node][0][1], node)
        ax.scatter(graph[start_node][0][0], graph[start_node][0][1], s=100, color='green')
        ax.text(graph[start_node][0][0], graph[start_node][0][1], start_node)
        ax.scatter(graph[goal_node][0][0], graph[goal_node][0][1], s=100, color='red')
        ax.text(graph[goal_node][0][0], graph[goal_node][0][1], goal_node)
        for node in graph.keys():
            for neighbor in graph[node][0]:
                ax.plot([graph[node][0][0], graph[neighbor][0][0]], [graph[node][0][1], graph[neighbor][0][1]], color='gray')
        return ax
    
    # Animating the graph
    def animate_graph(self, graph, path):
        ax = self.draw_graph(graph)
        i = 0
        def animate(i):
            if i < len(path) - 1:
                ax.plot([graph[path[i]][0][0], graph[path[i + 1]][0][0]], [graph[path[i]][0][1], graph[path[i + 1]][0][1]], color='orange', linewidth=3)
            return ax
        return animation.FuncAnimation(fig=plt.gcf(), func=animate, frames=len(path), interval=1000)
    
    # Main function
    def run(self, graph):
        start_node = self.find_start(graph)
        goal_node = self.find_goal(graph)
        path = self.find_path(graph, start_node, goal_node)
        if path:
            print('Path found:', path)
            print('Number of iterations:', self.iterations)
            anim = self.animate_graph(graph, path)
            plt.show()
        else:
            print('Path not found')
        

graph = {
    'A': [['B', 'C'], 0],
    'B': [['A', 'D'], 0],
    'C': [['A', 'D'], 0],
    'D': [['B', 'C', 'E'], 0],
    'E': [['D', 'F'], 0],
    'F': [['E', 'G'], 0],
    'G': [['F', 'H'], 0],
    'H': [['G', 'I'], 0],
    'I': [['H', 'G'], 1]
}

if __name__ == '__main__':
    try:
        breadth_search_first = BreadthSearchFirst()
        breadth_search_first.run(graph)
        
    except (KeyboardInterrupt, SystemExit):
        print(" Program has been stopped.")