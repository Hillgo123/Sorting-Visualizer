import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons, Slider
import random


class algorithms:
    """Contains the sorting algorithms"""

    def __init__(self):
        pass

    def bubble_sort(self, arr: list):
        """Sorts the array using bubble sort"""

        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                visualizer.display_bar(arr, j + 1)

        btn_handler.create_btns()

    def selection_sort(self, arr: list):
        """Sorts the array using selection sort"""

        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            visualizer.display_bar(arr, i)

        btn_handler.create_btns()

    def insertion_sort(self, arr: list):
        """Sorts the array using insertion sort"""

        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            visualizer.display_bar(arr, j)

        btn_handler.create_btns()

    def merge_sort(self, arr: list):
        """Sorts the array using merge sort"""

        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        def merge_sort_recursive(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort_recursive(arr[:mid])
            right = merge_sort_recursive(arr[mid:])
            return merge(left, right)

        sorted_arr = merge_sort_recursive(arr)
        for i, value in enumerate(sorted_arr):
            arr[i] = value
            visualizer.display_bar(arr, i)

        btn_handler.create_btns()

    def quick_sort(self, arr: list):
        """Sorts the array using quick sort"""

        def partition(low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    visualizer.display_bar(arr, j)
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            visualizer.display_bar(arr, i + 1)
            return i + 1

        def quick_sort_recursive(low, high):
            if low < high:
                pi = partition(low, high)
                quick_sort_recursive(low, pi - 1)
                quick_sort_recursive(pi + 1, high)

        quick_sort_recursive(0, len(arr) - 1)
        btn_handler.create_btns()

    def heap_sort(self, arr: list):
        """Sorts the array using heap sort"""

        def heapify(n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left] > arr[largest]:
                largest = left

            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                visualizer.display_bar(arr, i)
                heapify(n, largest)

        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            visualizer.display_bar(arr, i)
            heapify(i, 0)

        btn_handler.create_btns()


class sorting_algorithm_visualizer:
    """Visualizes the sorting algorithm"""

    def __init__(self, operation_delay: float):
        self.operation_delay = operation_delay
        self.operations = 0

    def display_bar(self, arr: list, current_index: int = None):
        """Displays the bars on the screen"""

        plt.clf()
        bar_colors = ["blue" if i != current_index else "red" for i in range(len(arr))]
        plt.bar(range(len(arr)), arr, color=bar_colors)
        plt.title(f"Operations: {self.operations}")
        self.operations += 1
        plt.pause(self.operation_delay)


class buttons:
    """Handles the buttons and sliders on the screen"""

    def __init__(self):
        self.selected_algorithm = algorithm.bubble_sort
        self.last_arr = 30

    def start_visualization(self, event: Button):
        """Starts the visualization of the selected algorithm"""

        visualizer.operations = 0
        self.selected_algorithm(arr)
        plt.show()

    def select_algorithm(self, label: str):
        """Selects the algorithm to be used for sorting"""

        if label == "Bubble Sort":
            self.selected_algorithm = algorithm.bubble_sort
        elif label == "Selection Sort":
            self.selected_algorithm = algorithm.selection_sort
        elif label == "Insertion Sort":
            self.selected_algorithm = algorithm.insertion_sort
        elif label == "Merge Sort":
            self.selected_algorithm = algorithm.merge_sort
        elif label == "Quick Sort":
            self.selected_algorithm = algorithm.quick_sort
        elif label == "Heap Sort":
            self.selected_algorithm = algorithm.heap_sort

    def new_array(self, event: Button):
        """Creates a new array and displays it on the screen"""

        global arr
        if self.last_arr == len(arr):
            arr = [random.randint(1, 100) for _ in range(self.last_arr)]
        visualizer.display_bar(arr)
        self.create_btns()
        self.last_arr = len(arr)

    def update_array_size(self, arr_size: int):
        """Updates the size of the array"""

        global arr
        arr = [random.randint(1, 100) for _ in range(arr_size)]

    def create_btns(self):
        """Creates the buttons on the screen"""

        ax_algorithm = plt.axes([0.05, 0.05, 0.2, 0.2])
        ax_start = plt.axes([0.35, 0.05, 0.25, 0.075])
        ax_new_array = plt.axes([0.65, 0.05, 0.25, 0.075])
        ax_array_size = plt.axes([0.375, 0.2, 0.25, 0.03])

        self.radio_algorithm = RadioButtons(
            ax_algorithm,
            [
                "Bubble Sort",
                "Selection Sort",
                "Insertion Sort",
                "Merge Sort",
                "Quick Sort",
                "Heap Sort",
            ],
        )
        self.radio_algorithm.on_clicked(self.select_algorithm)

        self.btn_start = Button(ax_start, "Start")
        self.btn_start.on_clicked(self.start_visualization)

        self.btn_new_array = Button(ax_new_array, "New Array")
        self.btn_new_array.on_clicked(self.new_array)

        self.slider_array_size = Slider(
            ax_array_size,
            "Array Size",
            10,
            100,
            valinit=len(arr),
            valstep=1,
            valfmt="%0.0f",
        )
        self.slider_array_size.on_changed(self.update_array_size)


visualizer = sorting_algorithm_visualizer(0.0001)
algorithm = algorithms()
btn_handler = buttons()

if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(30)]

    fig = plt.figure(figsize=(12, 8))
    fig.canvas.manager.set_window_title("Sorting Algorithm Visualizer")
    plt.subplots_adjust(bottom=0.3)
    ax_bar = fig.add_subplot(111)

    visualizer.display_bar(arr)
    btn_handler.create_btns()
    plt.show()
