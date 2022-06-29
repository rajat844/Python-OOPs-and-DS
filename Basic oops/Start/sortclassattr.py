lst_name = ["rajat","avnish", "pushan","manish","kunal","ujjwal","navneet,"]
lst_age = [23,21,22,23,23,21,22]
lst_rollNo = [21,1,12,33,72,20,15]
lst_cgpa = [8.08,8.1,8.5,8.9,9.3,7.8,8.4]

lst_object = []
for i in range(len(lst_name)):
    lst_object.append((lst_name[i],lst_age[i],lst_rollNo[i],lst_cgpa[i]))

print(lst_object)
name = sorted(lst_object,key=lambda x : x[0])
age = sorted(lst_object,key=lambda x : x[1])
rollNo= sorted(lst_object,key=lambda x : x[0])
cgpa = sorted(lst_object,key = lambda x : x[3])
print(name)
print(age)
print(rollNo)
print(cgpa)
