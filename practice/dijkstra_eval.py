# code based on dijkstra's evaluation algorithm utilizing two stacks

"""dijkstra_eval.pu
    Python code to evaluate a valid mathematical expression formatted as a string
"""

# ---------------------------------------------------------------------------------------------------------

from data_structures.stack_ds import Stack


# ---------------------------------------------------------------------------------------------------------


def dijkstra_eval(expression: str) -> str:
    """Evaluate a valid expression using dijkstra's evaluation algorithm"""
    operations: Stack = Stack()
    operands: Stack = Stack()

    expression_array = expression.split(" ")

    for item in expression_array:
        if item == "+":
            operations.push(item)

        elif item == "-":
            operations.push(item)

        elif item == "*":
            operations.push(item)

        elif item == "/":
            operations.push(item)

        elif item == ")":
            operation = operations.pop()

            first_operand = int(operands.pop())
            second_operand = int(operands.pop())

            new_operand = 0

            if operation == "+":
                new_operand = second_operand + first_operand

            elif operation == "-":
                new_operand = second_operand - first_operand

            elif operation == "*":
                new_operand = second_operand * first_operand

            elif operation == "/":
                new_operand = second_operand / first_operand

            operands.push(str(new_operand))

        else:
            if item.isnumeric():
                operands.push(item)

    return operands.pop()


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    test_expression = "( ( 2 * 10 ) + ( 11 - 1 ) )"  # needs to be fully parenthesized
    print(dijkstra_eval(test_expression))


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
