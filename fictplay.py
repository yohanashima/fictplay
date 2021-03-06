# -*- coding: utf-8 -*-
from __future__ import division  
import matplotlib.pyplot as plt
from random import uniform, choice
import numpy as np

def fictplay(t):
    x_0_t = [uniform(0, 1)]
    x_1_t = [uniform(0, 1)]
    gain_0 = np.array([[1, -1], [-1, 1]])   #player0
    gain_1 = np.array([[-1, 1], [1, -1]])   #player1
	
    for i in range(t):
        pro_1 = np.array([1-x_0_t[i], x_0_t[i]])      #probability: player1 choice 0 or 1
        exp_gain_0 = np.dot(gain_0, pro_1)            #expected gain = gain ×　probability
        if exp_gain_0[0] > exp_gain_0[1]:
            a_0_i = 0
        elif exp_gain_0[0] == exp_gain_0[1]:
            a_0_i = choice([0, 1])
        else:
            a_0_i = 1

        pro_0 = np.array([1-x_1_t[i], x_1_t[i]])   
        exp_gain_1 = np.dot(gain_1, pro_0)
        if exp_gain_1[0] > exp_gain_1[1]:
            a_1_i = 0
        elif exp_gain_1[0] == exp_gain_1[1]:
            a_1_i = choice([0, 1])
        else:
            a_1_i = 1
        
        x_0_i1 = x_0_t[i] + (a_1_i - x_0_t[i]) / (i+2)
        x_1_i1 = x_1_t[i] + (a_0_i - x_1_t[i]) / (i+2)
        x_0_t.append(x_0_i1)
        x_1_t.append(x_1_i1)

    return x_0_t, x_1_t


x_0_t, x_1_t = fictplay(1000)
         
plt.plot(x_0_t, 'r-', label="x_0(t)")
plt.plot(x_1_t, 'b-', label="x_1(t)")
plt.legend()
#plt.savefig('fictplay0.png')
plt.show()

#x_0_t = []
#for i in range(100):
#    x_0, x_1 = fictplay(100)
#    x_0_t.append(x_0[-1])
#plt.hist(x_0_t)
#plt.savefig('fictplay_hist.png')
#plt.show()
