import sys

def transpose(piece, low, high):
  """
  Transpose the piece so that it is within the given vocal range.

  Args:
    piece: The piece of music as a list of tones.
    low: The lowest tone that the singer can sing.
    high: The highest tone that the singer can sing.

  Returns:
    The minimum number of accidentals in any transposition of the piece that keeps it in the singer's vocal range.
  """

  # Find the minimum number of tones to transpose the piece up or down.
  min_up = sys.maxsize
  min_down = sys.maxsize
  for tone in piece:
    if tone < low:
      min_up = min(min_up, low - tone)
    elif tone > high:
      min_down = min(min_down, tone - high)

  # Transpose the piece up or down by the minimum number of tones.
  if min_up < min_down:
    transposed_piece = [tone + min_up for tone in piece]
  else:
    transposed_piece = [tone - min_down for tone in piece]

  # Count the number of accidentals in the transposed piece.
  num_accidentals = 0
  for tone in transposed_piece:
    if "#" in tone:
      num_accidentals += 1

  return num_accidentals

def main():
  """
  Read the input and output the minimum number of accidentals in any transposition of the piece that keeps it in the singer's vocal range.
  """

  # Read the input.
  n = int(input())
  low, high = input().split()
  piece = input().split()

  # Transpose the piece and count the number of accidentals.
  num_accidentals = transpose(piece, low, high)

  # Output the minimum number of accidentals.
  print(num_accidentals)

if __name__ == "__main__":
  main()