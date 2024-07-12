N,M,K = input().split()
int_N = int(N)
int_M = int(M)
int_K = int(K)

n_list = list(map(int, input().split()))
total = 0

n_list_sorted = sorted(n_list, reverse=True)

max_value_cnt = n_list.count(n_list_sorted[0])

if max_value_cnt == 1:
    i = 0
    for m in range(int_M):
        if i < int_K:
            total += n_list_sorted[0]
            print(n_list_sorted[0])
            print(',')
            i += 1
            print("print i =", i)
        elif i >= int_K:
            total += n_list_sorted[1]
            print(n_list_sorted[1])
            print(',')
            i = 0
else:
    i = 0
    for m in range(int_M):
        if i < int_K*max_value_cnt:
            total += n_list_sorted[0]
            print(n_list_sorted[0])
            print(',')
            i += 1
        elif i >= int_K:
            total += n_list_sorted[1]
            print(n_list_sorted[1])
            print(',')
            i = 0
        
            
print(total)
    