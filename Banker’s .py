no_of_processes = 5
no_of_resources = 3

allocate = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
max_need = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [4, 2, 2], [5, 3, 3]]

available = [3, 3, 2]

finish = [0] * no_of_processes
safe_seq = [0] * no_of_processes

need = [[0] * no_of_resources for i in range(no_of_processes)]

for i in range(no_of_processes):
    for j in range(no_of_resources):
        need[i][j] = max_need[i][j] - allocate[i][j]

index = 0
for k in range(5):
    for i in range(no_of_processes):
        if finish[i] == 0:
            flag = True
            for j in range(no_of_resources):
                if need[i][j] > available[j]:
                    flag = False
                    break
            if flag:
                safe_seq[index] = i
                index += 1
                for y in range(no_of_resources):
                    available[y] += allocate[i][y]
                finish[i] = 1

print("The SAFE Sequence is:")
for i in range(no_of_processes - 1):
    print(" P->", safe_seq[i], end='')
print(" P->", safe_seq[no_of_processes - 1])
