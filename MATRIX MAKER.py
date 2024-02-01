list1 = ["roosevelt","balintawak","monumento","5th avenue","r.papa","abad santos","blumentrit","tayuman","bambang","doroteo Jose","carriedo","central terminal","united nations","pedro gil","quirino","vito cruz","gil puyat","libertad","edsa","baclaran"]
list2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 33, 35]
list2.reverse()

# for i in range(13,36):
#     print(f"{i},", end=" ")

for i in list1:
    for j in range(len(list1)):
        print(f"('{i}','{list1[j]}'): {list2[j-1]} ,")