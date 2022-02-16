# Big O Notation: O(n^2) because of the nested for loops

def occurrence():
    lstSize = len(lst)
    parity = True
    for i in range(0, lstSize):
        counter = 0
        for j in range(0, lstSize):
            if lst[i] == lst[j]:
                counter += 1
        if counter % 2 == 0:
            parity = False
    if parity:
        print("True, all elements of the list occur an odd number of times.")
    else:
        print("False, all elements of the list do not occur an odd number of times.")


elements = int(input("How many elements do you want to have in the list? "))
lst = []
for elem in range(elements):
    number = int(input("Enter a list element "))
    lst.append(number)
    print("Element added")
print("This is the list:")
print(lst)
occurrence()


