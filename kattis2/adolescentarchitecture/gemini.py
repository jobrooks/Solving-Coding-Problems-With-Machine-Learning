import sys

class Block:
    def __init__(self, type, size):
        self.type = type
        self.size = size

    def __lt__(self, other):
        if self.type == 'cube' and other.type == 'cube':
            return self.size < other.size
        elif self.type == 'cylinder' and other.type == 'cylinder':
            return self.size < other.size
        elif self.type == 'cube' and other.type == 'cylinder':
            return self.size * self.size < other.size * other.size
        else:
            return False

def is_possible(blocks):
    stack = []
    for block in blocks:
        if not stack or stack[-1] >= block:
            stack.append(block)
        else:
            return False
    return True


def main():
    n = int(input())
    blocks = []
    for i in range(n):
        type, size = input().split()
        blocks.append(Block(type, int(size)))

    blocks.sort(reverse=True)

    if is_possible(blocks):
        for block in blocks:
            print(block.type, block.size)
    else:
        print('impossible')

if __name__ == '__main__':
    main()