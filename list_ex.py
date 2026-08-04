list1=[1,2,3]
list2=[9,7,8]

# list1.append(list2)
# print(list1)

list1.extend(list2)

print(list1)

list1.sort()
print(list1)



#sorted() (returns a new sorted list)
numbers = [5, 2, 8, 1, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)  # Original list remains unchanged


#Sorting in decending order
numbers.sort(reverse=True)
print(numbers)