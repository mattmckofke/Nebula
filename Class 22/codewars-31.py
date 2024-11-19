def dont_give_me_five(start,end):
    new_nums = []
    for num in range(start, end+1):
        if "5" not in str(num): new_nums.append(num)
        
    return len(new_nums)

print(dont_give_me_five(1, 9))

def dont_give_me_five2(start,end):
    return len([num for num in range(start, end+1) if "5" not in str(num)])

print(dont_give_me_five2(1, 9))