import math, sys, os
import numpy as np

#------------------------------------------------------------------------------

def dist(x,y): return math.sqrt(x[0]-y[0])**2+math.sqrt(x[1]-y[1])**2

#------------------------------------------------------------------------------

def agglomerate(a,b,t):
    global R, V, s, p, t_step, t_acc, t_now
    ta = (s[b]-s[a])/t
    x_new = (V[a,0]*R[a]**2+V[b,0]*R[b]**2*ta)/(R[a]**2+R[b]**2*ta)
    y_new = (V[a,1]*R[a]**2+V[b,1]*R[b]**2*ta)/(R[a]**2+R[b]**2*ta)
    V[a,0] = (V[a,0]*R[a]**2*s[a]+V[b,0]*R[b]**2*s[b])/ \
                   (R[a]**2*s[a]+R[b]**2*s[b])
    V[a,1] = (V[a,1]*R[a]**2*s[a]+V[b,1]*R[b]**2*s[b])/ \
                   (R[a]**2*s[a]+R[b]**2*s[b])
    R[a]   = math.sqrt(R[a]**2*s[a] + R[b]**2*s[b])
    R[b] = 0
    V[b,0] = 0
    V[b,1] = 0
    p[b] = p[a]
    s[a] += s[b]
    s[b] = 0
    print(a,b,ta,x_new,y_new,s[a])
    t_acc = min(t_acc, t)
    while t_now <= s[a] :
        t_now += t_step
    t_now -= t_step
    for k in range(N):
        if R[k]**2 != 0:
            V[k,0] = (V[k,0]-v_inf[0])*(1 - t_step/s[k]) + v_inf[0]
            V[k,1] = (V[k,1]-v_inf[1])*(1 - t_step/s[k]) + v_inf[1]
            d = np.array([x_new-x_old[k], y_new-y_old[k]])
            x_old[k] += d[0]*t_step/s[k]
            y_old[k] += d[1]*t_step/s[k]
            s[k] -= t_step
            if k != a and dist([x_old[a], y_old[a]], [x_old[k], y_old[k]]) <= (R[a]+R[k])**2 :
                agglomerate(a,k,t)


#------------------------------------------------------------------------------

with open(sys.argv[1]+'.txt', 'r') as infile, \
     open(sys.argv[1]+'.out', 'w') as outfile:
    N = int(infile.readline())
    x, y, v_x, v_y, r = np.loadtxt(infile, delimiter=', ').T
    R = r**2
    V = np.array([v_x, v_y]).T
    p = np.zeros(N,int)
    s = np.ones(N,int)

    # Find closest pair first

    t_acc = 1e99
    for i in range(N):
        for j in range(i+1, N):
            if R[i] != 0 and R[j] != 0:
                d = dist([x[i], y[i]], [x[j], y[j]]) - (R[i]+R[j])**2
                if d < 0:
                    ta = ((R[i]**2+R[j]**2)*s[i]-d)/(R[i]**2+R[j]**2)
                    if ta < t_acc:
                        t_acc = ta
                        a = i
                        b = j
                    elif ta == t_acc:
                        if d+1e-6 < 0: a, b = b, a

    if t_acc < 1e99:
        agglomerate(a,b,t_acc)
    while t_now < 1e9:
        t_best = t_now+1e99
        for k in range(N):
            if R[k] != 0 and t_best > s[k]:
                t_best = s[k]
        t_step = min(t_step, 0.9*(t_best-t_now))
        t_now += t_step
        for k in range(N):
            if R[k] != 0:
                d = np.array([v_inf[0]*t_step, v_inf[1]*t_step])
                x_old[k] += d[0]
                y_old[k] += d[1]
                s[k] -= t_step
                for l in range(k+1,N):
                    if R[l] != 0 and dist([x_old[k], y_old[k]], [x_old[l], y_old[l]]) <= (R[k]+R[l])**2 :
                        agglomerate(k,l,t_now)
    drops = sum([R[k] != 0 for k in range(N)])
    outfile.write(f'{drops} {t_now:.6f}')