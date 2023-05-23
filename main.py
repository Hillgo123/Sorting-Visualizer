import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider, CheckButtons  # type: ignore
import random


class sorting_algorithm_visualizer:
    """Visualizes the sorting algorithm
    
    Args:
        operation_delay: The delay between each operation
    """

    def __init__(self, operation_delay: float):
        self.operation_delay = operation_delay
        self.operations = 0

    def display_bar(self, arr: list, current_index: int = -1) -> None:
        """Displays the array as a bar chart.

        Args:
            arr: The array to be displayed.
            index: The index of the element that was just swapped. Defaults to -1.

        Returns:
            None
        """

        plt.clf()
        bar_colors = ["blue" if i != current_index else "red" for i in range(len(arr))]
        plt.bar(range(len(arr)), arr, color=bar_colors)
        plt.title(
            f"Algorithm: {btn_handler.selected_algorithm.__name__} Operations: {self.operations}"
        )
        self.operations += 1
        plt.pause(self.operation_delay)


class algorithms:
    """Contains the sorting algorithms"""

    def __init__(self):
        pass

    def bubble_sort(self, arr: list) -> None:
        """Sorts the array using bubble sort

        Args:
            arr: The array to be sorted.

        Returns:
            None
        """

        for i in range(len(arr)):  # Loop through the array
            for j in range(0, len(arr) - i - 1):  # Loop through the unsorted part of the array
                # If the current element is greater than the next element swap the current element with the next element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

                visualizer.display_bar(arr, j + 1)

        btn_handler.create_btns()

    def selection_sort(self, arr: list) -> None:
        """Sorts the array using selection sort

        Args:
            arr: The array to be sorted.

        Returns:
            None
        """

        # Loop through the array
        for i in range(len(arr)):
            min_idx = i  # Set the minimum index to the current index
            # Loop through the remaining elements in the array
            for j in range(i + 1, len(arr)):
                if (arr[j] < arr[min_idx]):  # If the current element is less than the minimum element
                    min_idx = j  # Set the minimum index to the current index

            arr[i], arr[min_idx] = (arr[min_idx], arr[i])  # Swap the current element with the minimum element

            visualizer.display_bar(arr, i)

        btn_handler.create_btns()

    def insertion_sort(self, arr: list) -> None:
        """Sorts the array using insertion sort

        Args:
            arr: The array to be sorted.

        Returns:
            None
        """

        # Loop through the array starting at index 1
        for i in range(1, len(arr)):
            # Set the key to the current element
            key = arr[i]
            # Set j to the previous index
            j = i - 1
            # While j is greater than or equal to 0 and the element at j is greater than the key
            while j >= 0 and key < arr[j]:
                # Shift the element at j to the right
                arr[j + 1] = arr[j]
                # Decrement j
                j -= 1
            # Insert the key at the correct position
            arr[j + 1] = key

            visualizer.display_bar(arr, j)

        btn_handler.create_btns()

    def merge_sort(self, arr: list) -> None:
        """Sorts the array using merge sort

        Args:
            arr: The array to be sorted.

        Returns:
            None
        """

        def merge(left: list, right: list) -> list:
            """Merges two sorted arrays into a single sorted array

            Args:
                left: The left sorted array
                right: The right sorted array

            Returns:
                The merged sorted array
            """

            result = []
            i = j = 0
            # Loop through both arrays until one of them is fully traversed
            while i < len(left) and j < len(right):
                # If the current element in the left array is less than the current element in the right array append the current element in the left array to the result array and move to the next element in the left array
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                # Otherwise, append the current element in the right array to the result array and move to the next element in the right array
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])  # Append any remaining elements in the left array to the result array
            result.extend(right[j:])  # Append any remaining elements in the right array to the result array

            return result

        def merge_sort_recursive(arr: list) -> list:
            """Recursively sorts the array using merge sort

            Args:
                arr: The array to be sorted

            Returns:
                The sorted array
            """

            # If the array has only one element or is empty, it is already sorted
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2 # Find the middle index of the array
            left = merge_sort_recursive(arr[:mid]) # Recursively sort the left half of the array
            right = merge_sort_recursive(arr[mid:]) # Recursively sort the right half of the array
            return merge(left, right) # Merge the sorted left and right halves of the array

        # Sort the array using merge sort
        sorted_arr = merge_sort_recursive(arr)

        # Replace the original array with the sorted array
        for i, value in enumerate(sorted_arr):
            arr[i] = value
            visualizer.display_bar(arr, i)

        btn_handler.create_btns()

    def quick_sort(self, arr: list) -> None:
        """Sorts the array using quick sort

        Args:
            arr: The array to be sorted.

        Returns:
            None
        """

        def partition(low: int, high: int) -> int:
            """Partitions the sub-array between low and high using the last element as the pivot

            Args:
                low: The lower index of the sub-array
                high: The upper index of the sub-array

            Returns:
                The index of the pivot element
            """

            pivot = arr[high] # Set the pivot to the last element in the array
            i = low - 1 # Set i to the index before the first element in the array
            
            # Loop through the array from low to high - 1, if the current element is less than the pivot increment i and swap the current element with the element at i
            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    
                    visualizer.display_bar(arr, j)
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1] # Swap the pivot with the element at i + 1
            
            visualizer.display_bar(arr, i + 1)
            # Return the index of the pivot
            return i + 1

        def quick_sort_recursive(low: int, high: int) -> None:
            """Recursively sorts the sub-array between low and high using the partition function

            Args:
                low: The lower index of the sub-array
                high: The upper index of the sub-array

            Returns:
                None
            """

            # If low is less than high, partition the array and recursively sort the left and right halves of the array
            if low < high:
                pi = partition(low, high)
                quick_sort_recursive(low, pi - 1)
                quick_sort_recursive(pi + 1, high)

        # Sort the entire array using quick sort
        quick_sort_recursive(0, len(arr) - 1)
        btn_handler.create_btns()

    def heap_sort(self, arr: list) -> None:
        """Sorts the array using heap sort

        Args:
            arr: The array to be sorted.

        Returns:
            None
        """

        def heapify(n: int, i: int) -> None:
            """Heapifies the sub-array rooted at i

            Args:
                n: The length of the sub-array
                i: The index of the root node of the sub-array

            Returns:
                None
            """

            largest = i # Set the largest index to i
            # Calculate the indices of the left and right children of i
            left = 2 * i + 1
            right = 2 * i + 2

            # If the left child is within the bounds of the array and is greater than the current largest element set the largest index to the left child
            if left < n and arr[left] > arr[largest]:
                largest = left

            # If the right child is within the bounds of the array and is greater than the current largest element set the largest index to the right child
            if right < n and arr[right] > arr[largest]:
                largest = right

            # If the largest index is not i, swap the elements at i and largest and recursively heapify the affected subtree
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                
                visualizer.display_bar(arr, i)
                heapify(n, largest)

        # Build a max heap by calling heapify on each non-leaf node in the array
        for i in range(len(arr) // 2 - 1, -1, -1):
            heapify(len(arr), i)

        # Sort the array by repeatedly swapping the first and last elements and heapifying the remaining elements
        for i in range(len(arr) - 1, 0, -1):
            # Swap the first and last elements of the unsorted portion of the array
            arr[i], arr[0] = arr[0], arr[i]
            
            visualizer.display_bar(arr, i)
            # Heapify the remaining elements to maintain the max heap property
            heapify(i, 0)

        btn_handler.create_btns()


class buttons:
    """Handles the buttons and sliders on the screen"""

    def __init__(self):
        self.selected_algorithm = algorithm.bubble_sort
        self.last_arr = 30
        self.selected_algorithms = {}

    def select_algorithm(self, label: str) -> None:
        """Selects the algorithm to be used for sorting.

        Args:
            label: The label of the selected algorithm.

        Returns:
            None
        """

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

    def new_array(self, event: Button) -> None:
        """Creates a new array and displays it on the screen.

        Args:
            event: The button click event that triggers the function.

        Returns:
            None
        """

        global arr
        # Make sure the array isn't already sorted
        if self.last_arr == len(arr):
            arr = [random.randint(1, 100) for _ in range(self.last_arr)]
        visualizer.operations = 0 # Reset the number of operations
        visualizer.display_bar(arr)
        self.create_btns()
        self.last_arr = len(arr)

    def update_array_size(self, arr_size: int) -> None:
        """Updates the size of the array.

        Args:
            arr_size: The new size of the array.

        Returns:
            None
        """

        global arr
        arr = [random.randint(1, 100) for _ in range(arr_size)]

    def compare_algorithms(self, event: Button) -> None:
        """Compares the sorting algorithms.

        This function compares the selected sorting algorithms by measuring the number of operations
        required to sort an array of random integers. The results are displayed in a bar chart.

        Args:
            event: The button click event that triggers the function.

        Returns:
            None
        """

        # Initialize an empty list to store the results
        results = []

        # Iterate over the selected algorithms and measure the number of operations required to sort the array
        for alg_name, alg in self.selected_algorithms.items():
            arr_copy = arr.copy()
            visualizer.operations = 0
            self.selected_algorithm = alg
            alg(arr_copy)
            results.append((alg_name, visualizer.operations))

        # Display the results in a bar chart
        plt.clf()
        plt.bar([result[0] for result in results], [result[1] for result in results])
        plt.xlabel("Algorithms")
        plt.ylabel("Operations")
        plt.title("Comparison of Sorting Algorithms")
        plt.show()
        self.create_btns()

    def create_btns(self) -> None:
        """Creates the buttons for selecting the sorting algorithm.

        Returns:
            None
        """

        # Plot the buttons
        ax_checkboxes = plt.axes(tuple([0.05, 0.05, 0.2, 0.2]))
        ax_start = plt.axes(tuple([0.35, 0.05, 0.25, 0.075]))
        ax_new_array = plt.axes(tuple([0.65, 0.05, 0.25, 0.075]))
        ax_array_size = plt.axes(tuple([0.375, 0.2, 0.25, 0.03]))

        self.btn_start = Button(ax_start, "Start")
        self.btn_start.on_clicked(self.compare_algorithms)

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

        alg_labels = [
            "Bubble Sort",
            "Selection Sort",
            "Insertion Sort",
            "Merge Sort",
            "Quick Sort",
            "Heap Sort",
        ]
        initial_states = [label in self.selected_algorithms for label in alg_labels] # Check the boxes for the selected algorithms

        self.checkboxes = CheckButtons(
            ax_checkboxes,
            alg_labels,
            initial_states,
        )
        self.checkboxes.on_clicked(self.toggle_algorithm)

    def toggle_algorithm(self, label: str) -> None:
        """Toggles the selected algorithms for comparison

        Args:
            label: The label of the algorithm to toggle

        Returns:
            None
        """

        # Dictionary mapping algorithm labels to their corresponding functions
        alg = {
            "Bubble Sort": algorithm.bubble_sort,
            "Selection Sort": algorithm.selection_sort,
            "Insertion Sort": algorithm.insertion_sort,
            "Merge Sort": algorithm.merge_sort,
            "Quick Sort": algorithm.quick_sort,
            "Heap Sort": algorithm.heap_sort,
        }

        # If the algorithm is already selected, remove it from the selected algorithms, otherwise, add it to the selected algorithms
        if label in self.selected_algorithms:
            del self.selected_algorithms[label]
        else:
            self.selected_algorithms[label] = alg[label]


algorithm = algorithms()
visualizer = sorting_algorithm_visualizer(0.0001)
btn_handler = buttons()

if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(30)]

    fig = plt.figure(figsize=(12, 8))
    fig.canvas.manager.set_window_title("Sorting Algorithm Visualizer")  # type: ignore
    plt.subplots_adjust(bottom=0.3)
    ax_bar = fig.add_subplot(111)

    visualizer.display_bar(arr)
    btn_handler.create_btns()
    plt.show()
