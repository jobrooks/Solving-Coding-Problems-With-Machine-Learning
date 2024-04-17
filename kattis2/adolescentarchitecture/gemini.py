from collections import deque
from typing import List

def is_possible(blocks: List[tuple[str, int]]) -> bool:
    """
    Determines if it is possible to construct a stable tower out of the given blocks.

    Args:
        blocks: A list of tuples representing the blocks, where each tuple consists of a string giving the type of block ("cube" or "cylinder") and an integer giving the size of the block.

    Returns:
        True if it is possible to construct a stable tower, False otherwise.
    """
    # Sort the blocks by size in ascending order.
    blocks.sort(key=lambda block: block[1])

    # Create a stack to store the blocks.
    stack = deque()

    # Iterate over the blocks.
    for block in blocks:
        # If the stack is empty, push the block onto the stack.
        if not stack:
            stack.append(block)
        # Otherwise, check if the current block can be placed on top of the block at the top of the stack.
        elif (block[0] == "cube" and block[1] <= stack[-1][1]) or (block[0] == "cylinder" and block[1] * 2 <= stack[-1][1]):
            stack.append(block)
        # If the block cannot be placed on top of the block at the top of the stack, return False.
        else:
            return False

    # If all the blocks have been placed on the stack, return True.
    return True

def get_order(blocks: List[tuple[str, int]]) -> List[tuple[str, int]]:
    """
    Returns the order in which to stack the blocks to construct a stable tower.

    Args:
        blocks: A list of tuples representing the blocks, where each tuple consists of a string giving the type of block ("cube" or "cylinder") and an integer giving the size of the block.

    Returns:
        A list of tuples representing the order in which to stack the blocks.
    """
    # Sort the blocks by size in ascending order.
    blocks.sort(key=lambda block: block[1])

    # Create a stack to store the blocks.
    stack = deque()

    # Create a list to store the order in which to stack the blocks.
    order = []

    # Iterate over the blocks.
    for block in blocks:
        # If the stack is empty, push the block onto the stack and add it to the order.
        if not stack:
            stack.append(block)
            order.append(block)
        # Otherwise, check if the current block can be placed on top of the block at the top of the stack.
        elif (block[0] == "cube" and block[1] <= stack[-1][1]) or (block[0] == "cylinder" and block[1] * 2 <= stack[-1][1]):
            stack.append(block)
            order.append(block)
        # If the block cannot be placed on top of the block at the top of the stack, pop the block at the top of the stack and try again.
        else:
            stack.pop()

    # Return the order in which to stack the blocks.
    return order

def main():
    # Read the input.
    n = int(input())
    blocks = []
    for i in range(n):
        block_type, size = input().split()
        blocks.append((block_type, int(size)))

    # Check if it is possible to construct a stable tower.
    if not is_possible(blocks):
        print("impossible")
    # Otherwise, get the order in which to stack the blocks.
    else:
        order = get_order(blocks)
        # Print the order in which to stack the blocks.
        for block in order:
            print(block[0], block[1])

if __name__ == "__main__":
    main()