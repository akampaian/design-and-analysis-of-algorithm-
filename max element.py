def find_high(array):

    high=array[0]            

    for i in array:
        if i>high:
            high=i
    return high

array=[20,70,50,40,6,3,75,36]
high_value=find_high(array)
print(f"The highest element is {high_value}")