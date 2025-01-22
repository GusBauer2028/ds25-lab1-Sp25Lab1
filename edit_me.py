
def find_max(lst):
    """return the maximum element"""
#Author G. Bauer 1/22/2025
    current_max = lst[0]

    
    for i in range(1,len(lst)):
        if lst[i]> current_max:
            current_max = lst[i]
            

        
    

            return current_max

    return current_max

test_list = [2112*i % 2024 for i in range(10000)]

print(find_max(test_list))
