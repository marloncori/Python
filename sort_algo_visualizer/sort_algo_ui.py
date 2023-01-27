import tkinter as tk

class SortAlgoUI:
    def __init__(self, app):
        self.app = app

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Sorting Algorithms")

        # Create the sorting algorithm buttons
        self.sort_label = tk.Label(self.root, text="Choose a sorting algorithm:")
        self.sp_label = tk.Label(self.root, text="                    ")
        self.quick_sort_button = tk.Button(self.root, text="QUICK SORT", command=self.on_quick_sort)
        self.merge_sort_button = tk.Button(self.root, text="MERGE SORT", command=self.on_merge_sort)
        self.radix_sort_button = tk.Button(self.root, text="RADIX SORT", command=self.on_radix_sort)
        self.shell_sort_button = tk.Button(self.root, text="SHELL SORT", command=self.on_shell_sort)
        self.bucket_sort_button = tk.Button(self.root, text="BUCKET SORT", command=self.on_bucket_sort)
        self.insert_sort_button = tk.Button(self.root, text="INSERT SORT", command=self.on_insert_sort)
        
        # Create the array size entry field
        self.size_label = tk.Label(self.root, text="Enter the size of the array:")
        self.size_entry = tk.Entry(self.root)

        self.sort_label.pack()
        # Place the widgets in the window
        self.quick_sort_button.pack()
        self.merge_sort_button.pack()
        self.radix_sort_button.pack()
        self.shell_sort_button.pack()
        self.bucket_sort_button.pack()
        self.insert_sort_button.pack()
        self.sp_label.pack()
        
        self.size_label.pack()
        self.size_entry.pack()

    def on_quick_sort(self):
        size = int(self.size_entry.get())
        self.app.run(1, size)

    def on_merge_sort(self):
        size = int(self.size_entry.get())
        self.app.run(2, size)

    def on_radix_sort(self):
        size = int(self.size_entry.get())
        self.app.run(3, size)

    def on_shell_sort(self):
        size = int(self.size_entry.get())
        self.app.run(4, size)

    def on_bucket_sort(self):
        size = int(self.size_entry.get())
        self.app.run(5, size)
        
    def on_insert_sort(self):
        size = int(self.size_entry.get())
        self.app.run(6, size)
        
    def begin(self):
        self.root.mainloop()
