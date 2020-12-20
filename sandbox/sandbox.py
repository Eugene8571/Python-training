'''
У вас есть парк из 50 грузовиков. 
Каждый из них полностью заправлен и может проехать 100 км. 
Как далеко с их помощью вы можете доставить определенный груз? 
Что будет, если в вашем распоряжении N грузовиков?
'''

N = 50 #Trucks
L = 100 #Km
V = 100 #Liters


C = [100]*N #cortege
M = 0
def drop_truck(C, M, N, L, V):
    free_space = 0
    for truck in C[:len(C)]:
        free_space += V - truck
    if free_space >= C[-1]:
        for i in range(len(C)-1):
            while C[-1] > 0 and C[i] < 100:
                C[-1] -= 1
                C[i] += 1
        if C[0] <= 0:
            return M
        C.pop()
    M += 1
    drop_truck(C, M, N, L, V)


res = drop_truck(C, M, N, L, V)

print(f"{res=}")