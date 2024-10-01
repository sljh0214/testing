from typing import List

def calculate_sum_and_sum_square(samples: List[int]):
    sum = 0
    sum_square = 0
    for item in samples:
        sum = sum + item
        sum_square = sum_square + (item ** 2)
    return sum, sum_square

def mean(sum, size):
    return sum / size

def std(e_x2, e_x_2):
    """E(X^2) - E(X)^2"""
    return (e_x2 - e_x_2) ** 0.5

def ci_min(avg, conf_index, std, n):
    return avg - (conf_index * (std / (n ** 0.5)))

def ci_max(avg, conf_index, std, n):
    return avg + (conf_index * (std / (n ** 0.5)))

def ci95(samples: List[int]):
    n = len(samples)

    sum, sum_square = calculate_sum_and_sum_square(samples)

    avg = mean(sum, n)
    avg_square = (avg ** 2)
    avg_sum_square = mean(sum_square, n)
    # var = avg_sum_square - avg_square
    root_var = std(avg_sum_square, avg_square)    

    return ci_min(avg, 1.96, root_var, n), ci_max(avg, 1.96, root_var, n)

def ci95_round(samples: List[int], roundNum: int):
    ci_min, ci_max = ci95(samples)
    return round(ci_min, roundNum), round(ci_max, roundNum)

def ci99(samples: List[int]):
    n = len(samples)

    sum, sum_square = calculate_sum_and_sum_square(samples)

    avg = mean(sum, n)
    avg_square = (avg ** 2)
    avg_sum_square = mean(sum_square, n)
    # var = avg_sum_square - avg_square
    root_var = std(avg_sum_square, avg_square)    

    return ci_min(avg, 2.57, root_var, n), ci_max(avg, 2.57, root_var, n)