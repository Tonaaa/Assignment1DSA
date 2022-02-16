elements = int(input("How many elements do you want to have in the list? "))
lst = []
for elem in range(elements):
    number = int(input("Enter a list element "))
    lst.append(number)
    print("Element added")
print("This is the list:")
print(lst)

k = int(input("Enter the k value "))
lst.sort(reverse=True)
new_lst = []

for i in lst:
    if lst.index(i) < k:
        new_lst.append(i)

summation = 0
for j in new_lst:
    summation += j
print("The sum of the largest " + str(k) + " numbers is " + str(summation))
