global_variable = 100 
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'} 
def process_numbers(): 
    global global_variable 
    local_variable = 5 
    numbers = [1, 2, 3, 4, 5] #Numbers should be a variable in the function not defined here

    while local_variable > 0: 
        if local_variable % 2 == 0: 
            numbers.remove(local_variable) #What if its not in numbers?
        local_variable -= 1 

    return numbers 

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} #Duplicate numbers in set
result = process_numbers(numbers=my_set) #Function called needs to be updated to allow argument

def modify_dict(): 
    local_variable = 10 
    my_dict['key4'] = local_variable 

modify_dict(5) #Function does not expect an argument

def update_global(): #Function defined but not called
    global global_variable 
    global_variable += 10 

for i in range(5): 
    print(i) #i prints 0-4
    i += 1 #Before print if you want i to print as 1-5 

if my_set is not None and my_dict['key4'] == 10: #Use .get to acces key4?
    print("Condition met!")

if 5 not in my_dict: #My_dict.values to see if 5 is a value in my_dict
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)
