list1 = ['sh','hr','re','apple','bat','python']
list2=[]
for i in list1:
    list2.append(i)
print(list2)

list3 = [ele for ele in list1 if 'n' in ele]
print(list3)
