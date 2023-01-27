import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Plotter:
    def __init__(self, sort_algorithm):
        self.sort_algorithm = sort_algorithm
        self.fig = plt.figure(figsize=(10,6))
        self.ax = self.fig.add_subplot(1,1,1)
        self.set_axes(self.sort_algorithm.arr)
        self.total_time = 0
        
    def set_axes(self, arr):
        self.ax.set_xlim([0,len(arr)])
        self.ax.set_ylim([0,max(arr)])
    
    def show(self):
        self.sort_algorithm.start()
        
    def update(self, iteration):
        sorted_arr, seconds = self.sort_algorithm.start(iteration)
        if sorted_arr is not None:
            if all(sorted(self.sort_algorithm.unsorted)==sorted_arr):
                self.ax.text(0.1, 0.85, 'Sorted!',
                             horizontalalignment='left', verticalalignment='top',transform=self.ax.transAxes,fontsize=20, color='green')
                return
            
            self.ax.cla()
            self.set_axes(sorted_arr)
            self.ax.set_title(self.sort_algorithm.name, fontsize=15, color='blue', pad=10)
            self.ax.set_xlabel('Elements')
            self.ax.set_ylabel('Values')
            self.ax.bar(range(len(sorted_arr)),sorted_arr)
            self.total_time += seconds
            self.ax.text(0.55,0.95, 'Iteration: {}\nSeconds: {:.2f}\n Total Time: {:.2f}'.format(iteration, seconds, self.total_time),
                         horizontalalignment='right',verticalalignment='top',transform=self.ax.transAxes)
            
    def animate(self, speed=1):
        if self.sort_algorithm.name == 'QUICK_SORT':
            anim = animation.FuncAnimation(self.fig, self.update, frames=range(speed*len(self.sort_algorithm.arr)),
                                       interval=speed*100, repeat=False)
            plt.show()
        else:
            self.show()
