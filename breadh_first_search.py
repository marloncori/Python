
#importing all required libraries
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

#defining the graph class
class Graph:
    def __init__(self, graph_dict={}):
        self.__graph_dict = graph_dict

    #function to get the nodes in the graph
    def get_nodes(self):
        return list(self.__graph_dict.keys())

    #function to get the edges of the graph
    def get_edges(self):
        return self.__generate_edges()

    #function to generate edges
    def __generate_edges(self):
        edges = []
        for node in self.__graph_dict:
            for neighbour in self.__graph_dict[node]:
                if {neighbour, node} not in edges:
                    edges.append({node, neighbour})
        return edges

    #function to add edges in the graph
    def add_edge(self, edge):
        edge = set(edge)
        (node1, node2) = tuple(edge)
        if node1 in self.__graph_dict:
            self.__graph_dict[node1].append(node2)
        else:
            self.__graph_dict[node1] = [node2]

#function to animate the graph
def bfs_animation(start_node, end_node, graph):
    visited = []
    queue = [start_node]

    #checking if start_node and end_node are in the graph
    if start_node not in graph.get_nodes() or end_node not in graph.get_nodes():
        print("Start node or end node is not in the graph")
        return
    
    #checking if the graph has at least one edge
    if not graph.get_edges():
        print("The graph does not contain any edges")
        return
    
    #defining the figure
    fig = plt.figure()
    ax = plt.axes()
    plt.title('Breadth First Search Algorithm')
    
    #defining the global variables for the figure
    global count
    count = 0
    global nodes
    nodes = graph.get_nodes()
    
    #defining the function for the animation
    def animate(i):
        #declaring the global variables
        global count
        global nodes

        #clearing the figure
        ax.clear()
        #setting the x and y coordinates
        x_coords = np.array([i[0] for i in nodes])
        y_coords = np.array([i[1] for i in nodes])

        #plotting the nodes
        ax.scatter(x_coords, y_coords, color='blue')

        #extracting the edges of the graph
        edges = graph.get_edges()

        #plotting the edges
        for edge in edges:
            node1, node2 = edge
            x1, y1 = node1
            x2, y2 = node2
            ax.plot([x1, x2], [y1, y2], color='blue')
        #plotting the nodes which are visited
        for node in visited:
            x, y = node
            ax.plot(x, y, color='red', marker='o', markersize=10)
        #checking if queue is empty
        if len(queue):

            #extracting the first element of the queue
            node = queue.pop(0)
            x, y = node

            #plotting the current node
            ax.plot(x, y, color='green', marker='o', markersize=10)

            #plotting the neighbors of the current node
            for neighbour in graph.__graph_dict[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
            #adding the current node to the visited list
            visited.append(node)

        #stopping the animation
        if node == end_node:
            return
        
        #increasing the count
        count += 1
    
    #animating the figure
    anim = animation.FuncAnimation(fig, animate, frames=count, interval=1000)
    
    #displaying the figure
    plt.show()

def run():
    #defining the graph
    graph = Graph()

   #adding edges to the graph
    graph.add_edge([(1,2), (2,3)])
    graph.add_edge([(3,4), (4,5)])
    graph.add_edge([(5,6), (6,7)])
    graph.add_edge([(7,8), (8,5)])
    graph.add_edge([(8,7), (7,5)])

    #defining the start node and the end node
    start_node = [(1,2), (2,3)]
    end_node = [(8,7), (7,5)]


    #calling the function to animate the graph
    bfs_animation(start_node, end_node, graph)


if __name__ == '__main__':
    run()
#graph.add_edge([(2, 3), (3, 4)])
#graph.add_edge([(3, 4), (1, 2)])
#graph.add_edge([(3, 4), (4, 5)])
#graph.add_edge([(1, 2), (6, 7)])
#graph.add_edge([(2, 3), (8, 9)])
#graph.add_edge([(8, 9), (10, 11)])

##calling the bfs_animation function
#bfs_animation((2, 3), (10, 11))