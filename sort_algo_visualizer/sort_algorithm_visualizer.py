from sort_algo_app import SortAlgoApp
from sort_algo_ui import SortAlgoUI

#------------------------------------------------------------------------------------------------
def main():
    app = SortAlgoApp()
    ui = SortAlgoUI(app)
    ui.begin()
    
#------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    try:
         main()       
    except KeyboardInterrupt:
        print(" END OF PROGAM.")
#------------------------------------------------------------------------------------------------    