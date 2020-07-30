import time as t
from LevenshteinDistance import levenshtein

def run_levenshtein(seqX=None, seqY=None, gap=1, mismatch=1):
    if seqX is None:
        seqX = input("Enter 1st Sequence:")
    if seqY is None:
        seqY = input("Enter 2nd Sequence:")

    start = t.time()
    levenshtein_dist, matrix = levenshtein.find_levenshtein_dist(seqX, seqY, gap, mismatch)
    end = t.time()

    print("Sequence 1: " + seqX + "\tSequence 2: " + seqY)
    print("Time to find the Levenshtein Distance: " + str(end-start))
    print("Levenshtein Distance: " + str(levenshtein_dist))
    print("Matrix after alg:\n"+ str(matrix) + "\n")

######################
run_levenshtein("World", "world")
run_levenshtein("humble", "crumple")
run_levenshtein("rapper", "speaker")
run_levenshtein("cereal", "mouse")
run_levenshtein("buy", "purchase")
