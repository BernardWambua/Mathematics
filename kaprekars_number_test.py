def kaprekars_number_test(n):
    original_n = n
    iteration = 1
    if n == 6174:
        return (f"You entered the Kaprekars number {n}, which already holds true.")
    while n != 6174:
        str_n = str(n)
        lst_str=list(str_n)
        ascending_n = lst_str.copy()
        descending_n = lst_str.copy()
        ascending_n.sort(key = int)
        descending_n.sort(key = int, reverse = True)
        new_ascending_n = ""
        for x in ascending_n:
            new_ascending_n += x
        
        new_descending_n = ""
        for x in descending_n:
            new_descending_n += x
        n = int(new_descending_n)-int(new_ascending_n)
        print(f"The number is {n} for iteration {iteration}")
        iteration +=1
        if n == 0:
            return (f"The test does not hold true for {original_n}.")  
    return (f"The test is done for {original_n} which holds true.")
