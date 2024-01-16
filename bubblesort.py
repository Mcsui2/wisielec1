a=[0,1,0,6,3,5]
def bubblesort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[j]>list[i]:
                list[j],list[i] = list[i],list[j]
bubblesort(a)
print(a)

