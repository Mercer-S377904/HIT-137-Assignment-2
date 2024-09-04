global_variable = 100 
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'} 

def process_numbers(numbers):  #Accepts numbers as an argument to the function
    global global_variable 
    #Removed the line as numbers argument is now passed as an argument
    local_variable = 5 

    while local_variable > 0: 
        if local_variable % 2 == 0: 
            if local_variable in numbers:  #Check if in numbers before removing
                numbers.remove(local_variable)
        local_variable -= 1 

    return numbers 

my_set = {1, 2, 3, 4, 5}  #Removed duplicate elements in the set
result = process_numbers(my_set)  #Numbers is an argument for the function, so we dont need to include 'numbers='

def modify_dict():  
    local_variable = 10 
    my_dict['key4'] = local_variable

modify_dict()  #Removed argument as function does not expect argument

def update_global(): 
    global global_variable 
    global_variable += 10 

update_global()  #Added the function call to actually update the global variable

for i in range(5):
    i += 1 #Moved the line 'i += 1' to be before print
    print(i) #Now prints i as 1 to 5 instead of 0 to 4

if my_set is not None and my_dict.get('key4') == 10:  #Used .get to access key4 value
    print("Condition met!")

if 5 not in my_dict.values():  #Used .values to correctly check if 5 is in the dictionary values
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)


 
