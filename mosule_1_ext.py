grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = (sorted(students))
x = 0
res_stud = {}
for c in grades[x]:
    grades[x] = (sum(grades[x])/len(grades[x]))
    res_stud[students[x]] = grades[x]
    x = x+1
print(res_stud)
