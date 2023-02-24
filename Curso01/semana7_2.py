for i in [5, 4, 3, 2, 1] :
    print(i)
print("BlastoF!")

largest_so_far = -1
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    largest_so_far
    print(largest_so_far, the_num)
print("After", largest_so_far)

counter = 0
print("Before", counter)
for the_num in [9, 41, 12, 3, 74, 15] :
    counter += 1
    print("counter", the_num)
print("After", counter)

found = False
counter = 0
print("Before", counter)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num == 3 :
        found = True
    counter += the_num
    print("counter", the_num)
print("After", counter)
print("After", found)

# if smallest is None => "smallest === None"