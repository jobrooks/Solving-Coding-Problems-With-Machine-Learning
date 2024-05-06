from typing import Tuple

Hydroxy = 'O'
Carbon = 'C'

Mapping = {
    'H': 1,
    'O': 2,
    'N': 3,
    'F': 1,
}

def count_neighbors(molecule: str, atom: str, idx: int) -> int:
    cnt = 0
    for i in range(idx, len(molecule)):
        if molecule[i] == atom:
            cnt += 1
        elif molecule[i].isdigit():
            continue
        else:
            break
    for i in range(idx - 1, -1, -1):
        if molecule[i] == atom:
            cnt += 1
        elif molecule[i].isdigit():
            continue
        else:
            break
    return cnt

def classify_alcohol(molecule: str) -> Tuple[int, ...]:
    is_alcohol = False
    alcohol_type = set()
    idx = 0
    while idx < len(molecule):
        if molecule[idx] != Hydroxy:
            idx += 1
            continue
        is_alcohol = True
        atom = molecule[idx - 1]
        neighbors = count_neighbors(molecule, Carbon, idx - 1)
        if neighbors == 0 or neighbors == 1:
            alcohol_type.add(1)
        elif neighbors == 2:
            alcohol_type.add(2)
        elif neighbors == 3:
            alcohol_type.add(3)
        idx += 1
    if not is_alcohol:
        return (0,)
    return tuple(sorted(alcohol_type))