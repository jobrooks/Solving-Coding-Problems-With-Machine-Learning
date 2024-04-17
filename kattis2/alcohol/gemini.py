import re

def is_alcohol(smiles):
  # Remove hydrogen atoms from the SMILES string.
  smiles = re.sub(r"[H]", "", smiles)

  # Split the SMILES string into a list of atoms and bonds.
  atoms = []
  bonds = []
  for i in range(len(smiles)):
    if smiles[i].isalpha():
      atoms.append(smiles[i])
    else:
      bonds.append(smiles[i])

  # Create a dictionary of atoms and their neighbors.
  neighbors = {}
  for i in range(len(atoms)):
    neighbors[atoms[i]] = []
    for j in range(i + 1, len(atoms)):
      if bonds[j] == "=":
        neighbors[atoms[i]].append(atoms[j])
        neighbors[atoms[j]].append(atoms[i])
      elif bonds[j] == "-":
        neighbors[atoms[i]].append(atoms[j])
        neighbors[atoms[j]].append(atoms[i])

  # Check if the compound contains a hydroxy group.
  is_alcohol = False
  for atom in atoms:
    if atom == "O" and len(neighbors[atom]) == 1:
      is_alcohol = True
      break

  # Check the number of carbon atoms bonded to the carbon atom that is bonded to the hydroxy group.
  alcohol_type = 0
  if is_alcohol:
    for neighbor in neighbors[atom]:
      if neighbor == "C":
        alcohol_type += 1

  return alcohol_type

if __name__ == "__main__":
  smiles = input()
  alcohol_type = is_alcohol(smiles)
  print(alcohol_type)