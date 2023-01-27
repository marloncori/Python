from django.shortcuts import render
from io import BytesIO
import base64

from myapp.models.plotter import Plotter
from myapp.models.algorithms.quickSort import QuickSort
from myapp.models.algorithms.shellSort import ShellSort
from myapp.models.algorithms.bucketSort import BucketSort
from myapp.models.algorithms.insertSort import InsertSort
from myapp.models.algorithms.mergeSort import MergeSort
from myapp.models.algorithms.radixSort import RadixSort

def index(request):
    return render(request, 'myapp/templates/index.html')

def sort(request):
    options = { 
        'quick': QuickSort, 'merge': MergeSort,
        'shell': ShellSort, 'radix': RadixSort,
        'bucket': BucketSort, 'insert': InsertSort,
    }
    arr = [int(x) for x in request.GET.get('arr').split(',')]
    algorithm = request.GET.get('algorithm')
    for name, option in options.items():
        if algorithm == name:
            sort_algorithm = option(arr)
    
    plotter = Plotter(sort_algorithm)
    if plotter.sort_algorithm.name == 'QUICK SORT':
        anim = animation.FuncAnimation(plotter.fig, plotter.update, frames=range(1, len(arr)), repeat=False)
    else:
        anim = animation.FuncAnimation(plotter.fig, plotter.show, frames=range(1, len(arr)), repeat=False)
    plt.close(plotter.fig)
    buf = BytesIO()
    anim.save(buf, format='png', dpi=80)
    buf.seek(0)
    response = base64.b64encode(buf.read())
    return render(request, 'myapp/templates/sort.html', {'animation': response.decode('utf-8')})

