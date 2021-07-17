print("Please enter the name of data-file :")

name = input()

with open(name, 'r') as f:
    List = f.read().split("\n")

def mergeSort(myList) :
    """
    Function to sort strings according to their sizes implemented using Merge Sort.
    
    Input : List[] of strings.
    Output : Void (Original List[] is changed).
    """
    if len(myList) > 1 :
        mid = len(myList) // 2
        left = myList[ :mid]
        right = myList[mid: ]
        mergeSort(left)
        mergeSort(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right) :
            if len(left[i])<len(right[j]) :
                myList[k]=left[i]
                i=i+1
            else :
                myList[k]=right[j]
                j=j+1
            k=k+1
        while i<len(left):
            myList[k] = left[i]
            i=i+1
            k=k+1
        while j<len(right) :
            myList[k] = right[j]
            j=j+1
            k=k+1

mergeSort(List)
print(List)