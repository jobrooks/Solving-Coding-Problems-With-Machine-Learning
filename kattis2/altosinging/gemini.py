import sys

def transpose(piece, min, max, octave_min, octave_max):
    """
    Transpose the piece to the given range.

    Args:
        piece: The piece to transpose.
        min: The lowest tone Anton can sing.
        max: The highest tone Anton can sing.
        octave_min: The lowest octave Anton can sing.
        octave_max: The highest octave Anton can sing.

    Returns:
        The transposed piece.
    """
    transposed_piece = []
    for tone in piece:
        note, octave = tone[:-1], int(tone[-1])
        if octave < octave_min or octave > octave_max:
            return None
        interval = ord(note) - ord(min[:-1])
        if interval < 0 or interval > ord(max[:-1]) - ord(min[:-1]):
            return None
        transposed_note = chr(ord(note) + interval)
        transposed_octave = octave
        if transposed_note > 'G':
            transposed_octave += 1
        elif transposed_note < 'C':
            transposed_octave -= 1
        transposed_piece.append(transposed_note + str(transposed_octave))
    return transposed_piece

def count_accidentals(piece):
    """
    Count the number of accidentals in the piece.

    Args:
        piece: The piece to count the accidentals in.

    Returns:
        The number of accidentals in the piece.
    """
    accidentals = 0
    for tone in piece:
        if '#' in tone:
            accidentals += 1
    return accidentals

def main():
    """
    Read the input and output the answer.
    """
    n = int(sys.stdin.readline())
    min, max = sys.stdin.readline().split()
    piece = sys.stdin.readline().split()
    octave_min = int(min[-1])
    octave_max = int(max[-1])
    min_accidentals = 1000000
    num_transpositions = 0
    for i in range(-12, 13):
        transposed_piece = transpose(piece, min, max, octave_min + i, octave_max + i)
        if transposed_piece is not None:
            accidentals = count_accidentals(transposed_piece)
            if accidentals < min_accidentals:
                min_accidentals = accidentals
                num_transpositions = 1
            elif accidentals == min_accidentals:
                num_transpositions += 1
    print(min_accidentals, num_transpositions)

if __name__ == "__main__":
    main()