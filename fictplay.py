# -*- coding: utf-8 -*-
from __future__ import division  
from matplotlib.pyplot import plot, show, legend, savefig, hist
from random import uniform, choice

def fictplay(t):
    x_0 = [uniform(0, 1)]
    x_1 = [uniform(0, 1)]
    a_0 = x_1[0]
    a_1 = x_0[0]

    for i in range(t):
        if x_0[i] < 0.5:
            a_0_t = 1
        elif x_0[i] == 0.5:
            a_0_t = choice([0, 1])
        else:
            a_0_t = 0
        a_0 += a_0_t    
        x_1_t = a_0 / (i+2)
        x_1.append(x_1_t)

        if x_1[i] < 0.5:
            a_1_t = 1
        elif x_1[i] == 0.5:
            a_1_t = choice([0, 1])
        else:
            a_1_t = 0
        a_1 += a_1_t    
        x_0_t = a_1 / (i+2)
        x_0.append(x_0_t)

    return x_0, x_1


#x_0, x_1 = fictplay(100)
         
#plot(x_0, 'r-', label="x_0(t)")
#plot(x_1, 'b-', label="x_1(t)")
#legend()
#savefig('fictplay0.png')
#show()

x_0_t = []
for i in range(100):
    x_0, x_1 = fictplay(100)
    x_0_t.append(x_0[-1])
hist(x_0_t, 100)
savefig('fictplay_hist.png')
show()

