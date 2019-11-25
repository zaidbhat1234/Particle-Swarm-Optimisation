from random import randrange

def fitness(x,y):
    '''Function to be minimized is defined here'''
    return (x**2)+(y**2)

def velocity(v,c1,r1,pbest,x,c2,r2,gbest,inertia=1):
    '''Calculate velcity for next iteration'''
    return inertia*v + c1*r1*(pbest-x) + c2*r2*(gbest-x)

def position(x,v):
    '''Caculate position value for next iteration'''
    return x+v

def calc_gbest(arr):
    '''Calculate 'gbest' based on fitness values'''
    fit_arr = [ fitness(i[0],i[1]) for i in arr ]
    min_fit = min(fit_arr)
    indx = fit_arr.index(min_fit)
    return arr[indx]

def psoa():

    pos = [ [2.7045, 4.8030],
            [4.5974, 2.8793],
            [1.8710, 4.0528],
            [1.6400, 1.3202],
            [3.3392, 0.9963] ]

    vel = [ [0.4752, 0.6987],
            [0.4141, 0.4020],
            [0.7797, 0.9433],
            [0.6183, 0.5749],
            [0.2530, 0.9398] ]

    c1 = 2      #Cognitive Constant 1
    c2 = 2      #Cognitive Constant 2
    inertia = 1 #Inertial parameter

    iterations = 2

    r1 = 0.34
    r2 = 0.86

    pbest = pos[:]

    for ix in range(iterations):

        gbest = calc_gbest(pos)

        pos_n = pos[:]
        vel_n = vel[:]

        for row in range(len(pos)):

            for col in range(len(pos[0])):
                vel_n_val = velocity(vel[row][col],c1,r1,pbest[row][col],pos[row][col],c2,r2,gbest[col])
                vel_n[row][col] = vel_n_val
                pos_n[row][col] = pos[row][col] + vel_n_val

            if fitness(vel_n[row][0],vel_n[row][1]) < fitness(vel[row][0],vel[row][1]):
                pbest[row] = vel_n[row]

        vel = vel_n
        pos = pos_n

    for i in vel:
        print(i)

    print()

    for j in pos:
        print(j)

psoa()




