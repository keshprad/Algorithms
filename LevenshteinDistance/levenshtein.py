import numpy as np


def find_levenshtein_dist(seqX=input("Enter 1st Sequence:"), seqY=input("Enter 2nd Sequence:"), gap=1, mismatch=1):
    # Initialize matrix
    matrix = np.zeros(shape=(len(seqY) + 1, len(seqX) + 1), dtype=int)

    # Set the first row and col. They are just used to prevent index out of bound errors
    matrix[0] = [x for x in range(len(seqX) + 1)]
    for y in range(len(seqY) + 1):
        matrix[y, 0] = y

    # Dynamic algorithm: Go through filling out the matrix while minimizing the total penalty.
    for y in range(1, len(seqY) + 1):
        for x in range(1, len(seqX) + 1):
            val1 = matrix[y, x - 1] + gap
            val2 = matrix[y - 1, x - 1] if seqX[x - 1] == seqY[y - 1] else matrix[y - 1, x - 1] + mismatch
            val3 = matrix[y - 1, x] + gap

            matrix[y, x] = min(val1, val2, val3)

    # End result stored in the last index of the matrix
    levenshtein_dist = matrix[len(seqY), len(seqX)]
    return levenshtein_dist, matrix


levenshtein_dist, matrix = find_levenshtein_dist()
print(levenshtein_dist)
print(matrix)
