import math
import random

T_awal = 1538 #inisiasi temperatur awal
T_akhir = 0.01 #kondisi loaping berhenti saat temperatur cooling down to 0

#inisiasi nilai random x1 dan x2 
x1 = random.uniform(-10,10)
x2 = random.uniform(-10,10)

def fungsi(x1,x2): #fungsi soal
    return -(abs(math.sin(x1)*math.cos(x2)*math.exp(abs(1 - math.sqrt((x1**2)+(x2**2))/math.pi))))

def probability(n_state,c_state,t): #menghitung probabilitas
    return math.exp(-(n_state - c_state)/t)

def max_random(x): #membatasi random agar tidak terlalu jauh dan melebihi batas
    a = x + random.uniform(-1,1)
    while not (a<= 10 and a>= -10):
        a = x + random.uniform(-1,1)
    return a

#inisiasi state state
cost = fungsi(x1,x2) 
c_state = cost
b_state = c_state


while T_awal>T_akhir: #looping sampai temperatur dingin
    for i in range(10): #iterasi 10 kali di temperatur yg sama        
        new_x1 = max_random(x1)
        new_x2 = max_random(x2)
        n_state = fungsi(new_x1,new_x2)
        p = probability(n_state,c_state,T_awal)
        check = random.uniform(0,1)
        if n_state < c_state: #jika new state lebih bagus dari current state
            x1 = new_x1
            x2 = new_x2
            c_state = n_state
            b_state = n_state
            #print(i,b_state, T_awal,check,p)
        else: #jika new state lebih jelek dari current
            if p>check:
                x1 = new_x1
                x2 = new_x2
                c_state = n_state
                #print(i,b_state,T_awal,check,p)      
    T_awal = T_awal - 0.01

print("Nilai X1:",x1)
print("Nilai X2:",x2)
print("Minimum Fungsi:",b_state)
