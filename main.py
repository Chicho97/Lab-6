# Laboratory 6 - Sorting Algorithms
# A simple Python program that sorts numbers using the
# algorithm written in a text file.

import os


def insertion_sort(numbers):
    """Sort a list of numbers using Insertion Sort."""
    result = numbers[:]  # work on a copy, keep the original list
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        # move bigger numbers one place to the right
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j = j - 1
        result[j + 1] = key
    return result


def merge(left, right):
    """Merge two sorted lists into one sorted list."""
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    # add what is left in either list
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(numbers):
    """Sort a list of numbers using Merge Sort."""
    if len(numbers) <= 1:
        return numbers[:]
    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])
    return merge(left, right)


def main():
    filename = "date.txt"

    # 1. Check that the file exists
    if not os.path.exists(filename):
        print("Error: file 'date.txt' does not exist.")
        return

    with open(filename, "r") as file:
        lines = file.readlines()

    # 2. The file must have exactly two input lines
    if len(lines) < 2:
        print("Error: 'date.txt' must have two lines: "
              "numbers on line 1 and the algorithm name on line 2.")
        return

    numbers_line = lines[0].strip()
    algorithm = lines[1].strip()

    # 3. Check that the numbers are valid integers
    if numbers_line == "":
        print("Error: line 1 is empty. Write numbers separated by spaces.")
        return
    try:
        numbers = [int(x) for x in numbers_line.split()]
    except ValueError:
        print("Error: line 1 must contain only integers separated by spaces.")
        return

    # 4. Run only the algorithm written in the file
    if algorithm.lower() == "insertion":
        sorted_numbers = insertion_sort(numbers)
        algorithm_name = "Insertion"
    elif algorithm.lower() == "merge":
        sorted_numbers = merge_sort(numbers)
        algorithm_name = "Merge"
    else:
        print("Error: unknown algorithm '" + algorithm + "'. "
              "Use 'Insertion' or 'Merge'.")
        return

    # 5. Write the result below the two input lines.
    #    The original two lines are kept, so running the program
    #    again does not add the result a second time.
    result_line = algorithm_name + ": " + " ".join(str(x) for x in sorted_numbers)
    with open(filename, "w") as file:
        file.write(numbers_line + "\n")
        file.write(algorithm + "\n")
        file.write(result_line + "\n")

    print(result_line)


if __name__ == "__main__":
    main()
