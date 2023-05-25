# code based on java implementation

"""main.py
   code containing functions to rotate an array by "k" steps
"""

# ---------------------------------------------------------------------------------------------------------


def rotate_array_by_k(k: int, array: [str]) -> [str]:
    length = len(array)
    rotated_array = [""] * length

    for i in range(length):
        next_pos = (i + k) % length
        rotated_array[next_pos] = array[i]

    return rotated_array

# ---------------------------------------------------------------------------------------------------------


def print_array(array: [str]) -> None:
    for item in array:
        print(f"{item}", end=" ")

    print()

# ---------------------------------------------------------------------------------------------------------


def main():
    test_string_array: [str] = ["A", "W", "A", "R", "D"]
    print_array(test_string_array)

    shift: int = int(input("Rotate array by (num): "))
    rotated_test_array: [str] = rotate_array_by_k(shift, test_string_array)

    print_array(rotated_test_array)


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
