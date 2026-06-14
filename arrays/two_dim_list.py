# Given 2D list calculate the sum of diagonal elements.
# Example

my_list_2dim = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def sum_diagonal(a):
    return sum(a[i][i] for i in range(len(a)))


sum_diagonal(my_list_2dim)  # 15
