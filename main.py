import matplotlib.pyplot as plt
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


visualizer = sorting_algorithm_visualizer(0.001)
algorithm = algorithms()

if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(30)]

    algorithm.bubble_sort(arr)
    # algorithm.selection_sort(arr)
    # algorithm.insertion_sort(arr)
    print(visualizer.operations)
    plt.show()
