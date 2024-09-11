#1. Join items of a given list using "-" and print the string. 
weekdays = ['sun','mon','tue','wed','thu','fri','sat']
# result = " - ".join(weekdays)
print(" - ".join(weekdays))


# 2. count the occurrences of a particular element in the
#list and output highest occurring element
days = ['sun','mon','mon','tue','wed','thu','fri','sat','mon','thu',]
count_with_name = {}

for i in days:
    if i in count_with_name:
        count_with_name[i] += 1
    else:
        count_with_name[i] = 1

max_element = max(count_with_name, key=count_with_name.get)
print("The highest occurring is", max_element, "with", count_with_name[max_element],"occurrences.")



# 3. Merge dictionaries a and b. The resultant dict must contain all items of 
# both dicts. If key is common then the value of key in resultant dict 
# must be the sum of value in a and b.
a = {'x': 1, 'y': 2, 'z': 3}
b = {'a': 4, 'b': 5, 'y': 6}
def dictMerge(a, b):
  result = {}
  
  for i in a:
    result[i]= a[i]
  for i in b:
    if i in result:
      result[i] += b[i]
    else:
      result[i] = b[i]
      
  return result
  
print(dictMerge(a, b))



#4. Return the Item with highest value count
items = [{'Delhi': 3}, {'Mumbai': 9}, {'Goa': 7}, {'Gujrat': 4}] 
def highest_count(items):

    max_city = None
    max_val = float('-inf')  

    for item in items:
        for city, value in item.items():  
            if value > max_val:  
                max_val = value
                max_city = city
    
    return max_city  

result = highest_count(items)
print("The item with the highest value count is:", result)
# #Output: Mumbai

   


 #5. Implement a group_by_owners function that:
#Accepts a dictionary containing the file owner name for each file name.
#Returns a dictionary containing a list of file names for each owner #name, in any order.
#files = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} 
#the group_by_owners function should return 
# output = {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

def group_by_owners(files):
    grped_files = {}
    
    for file_name, owner in files.items():
        
        if owner in grped_files:
            grped_files[owner].append(file_name)
        else:
            grped_files[owner] = [file_name]
    
    return grped_files

files = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
output = group_by_owners(files)
print(output)