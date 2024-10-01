# CISC 235 - Assignment 2 - Algorithm A
# Sophie Robbins
# 20343727

# This program contains the linear search function for Algorithm A


def linear_search(S, x):
    for item in S:
        if item == x:
            return True
    return False
