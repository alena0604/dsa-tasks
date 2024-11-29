def best_score(my_list):
    my_list.sort()
    sorted_list = list(set(my_list))
    print(sorted_list[-2:])


my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]

best_score(my_list)
