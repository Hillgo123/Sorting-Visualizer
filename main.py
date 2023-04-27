import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import random


class algorithms:
    def __init__(self):
        pass

    def bubble_sort(self, arr: list):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                visualizer.display_bar(arr, j)

    def selection_sort(self, arr: list):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            visualizer.display_bar(arr)

    def insertion_sort(self, arr: list):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            visualizer.display_bar(arr)


class sorting_algorithm_visualizer:
    def __init__(self, operation_delay: float):
        self.operation_delay = operation_delay
        self.operations = 0

    def display_bar(self, arr: list, current_index: int = None):
        plt.clf()
        bar_colors = ["blue" if i != current_index else "red" for i in range(len(arr))]
        plt.bar(range(len(arr)), arr, color=bar_colors)
        plt.pause(self.operation_delay)
        self.operations += 1


class buttons:
    def __init__(self):
        self.selected_algorithm = None

    def start_visualization(self, event):
        if self.selected_algorithm is not None:
            self.selected_algorithm(arr)
            plt.show()

    def select_algorithm(self, event, algorithm: algorithms):
        self.selected_algorithm = algorithm

    def create_buttons(self):
        ax_bubble = plt.axes([0.1, 0.05, 0.2, 0.075])
        ax_selection = plt.axes([0.4, 0.05, 0.2, 0.075])
        ax_insertion = plt.axes([0.7, 0.05, 0.2, 0.075])
        ax_start = plt.axes([0.4, 0.15, 0.2, 0.075])

        self.btn_bubble = Button(ax_bubble, "Bubble Sort")
        self.btn_bubble.on_clicked(
            lambda event: self.select_algorithm(event, algorithm.bubble_sort)
        )

        self.btn_selection = Button(ax_selection, "Selection Sort")
        self.btn_selection.on_clicked(
            lambda event: self.select_algorithm(event, algorithm.selection_sort)
        )

        self.btn_insertion = Button(ax_insertion, "Insertion Sort")
        self.btn_insertion.on_clicked(
            lambda event: self.select_algorithm(event, algorithm.insertion_sort)
        )

        self.btn_start = Button(ax_start, "Start")
        self.btn_start.on_clicked(self.start_visualization)


visualizer = sorting_algorithm_visualizer(0.001)
algorithm = algorithms()
btn_handler = buttons()

if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(30)]

    fig = plt.figure()
    plt.subplots_adjust(bottom=0.2)
    ax_bar = fig.add_subplot(111)

    visualizer.display_bar(arr)
    btn_handler.create_buttons()
    plt.show()
