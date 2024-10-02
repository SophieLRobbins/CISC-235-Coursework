import random
import time
from A2_AlgA import linear_search
from A2_AlgB import quicksort, binary_search


# CISC 235 - Assignment 2 - Initial Setup
# Sophie Robbins
# 20343727

# This program contains the bubble sort, binary search and trinary 
# search functions that are used for experiment 1. 

"""
Randomly generates a list of n values between 0 and n.

param n: sive of list and max value
return sorted_arr: the sorted array
"""
def generate(n):
    S = [random.randint(0, n) for _ in range(n)]
    return S



def other_values(S, n):
    all_vals = list(range(n+1))
    # Add the values present in all_vals that are not present in sorted_arr.
    not_in_S = list(set(all_vals) - set(S))
    return not_in_S


def find_k(n):
    max_k = 1000000  # You can adjust this limit as needed
    linear_times, binary_times = run_experiment(n, max_k)

    for k in range(max_k):
        if binary_times[k] < linear_times[k]:
            return k + 1  # Return the value of k*
    return None  # If never found


def run_experiment(n, max_k, S, not_in_S):
    generate(n)
    other_values(S, n)
    linear_times = []
    binary_times = []

    for k in range(1, max_k + 1):
        targets = random.sample(S, k // 2) + random.sample(not_in_S, k // 2)
        random.shuffle(targets)

    start = time.time()
    for x in targets:
        linear_search(S, x)
    end = time.time()
    linear_times.append(end - start)

    # Measure Algorithm B
    start = time.time()
    for x in targets:
        binary_search(S, x)
    end = time.time()
    binary_times.append(end - start)

    return linear_times, binary_times

def main():
    n_values = [1000, 2000, 5000, 10000]
    results = {}

    for n in n_values:
        k_star = find_k(n)
        results[n] = k_star

    print(results)

main()