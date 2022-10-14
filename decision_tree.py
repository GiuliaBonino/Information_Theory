#%%

import numpy as np

v=np.asarray([[30, 0, 10, 0], [30, 0, 70, 0], [30, 1, 20, 0], [30, 1, 80, 1], [60, 0, 40, 0], [60, 0, 60, 1], [60, 1, 50, 0], [60, 1, 60, 1]])
c=v[:,3]

v=np.delete(v, 3, 1)




# %%
def find_best_threshold(v,c):
    max_igr=0
    best_t=0
    for x in v:
        t=x #fix a threshold
        vtot=np.column_stack(v,c)
        v1=vtot[vtot[:,0]>t, :] #vector with values larger than threshold
        v2=vtot[vtot[:,0]<=t,:] #vector with values smaller than threshold
        p00=np.count_nonzero(v2[:,1]==0)/np.shape(vtot)[0]
        p01=np.count_nonzero(v2[:,1]==1)/np.shape(vtot)[0]
        p10=np.count_nonzero(v1[:,1]==0)/np.shape(vtot)[0]
        p11=np.count_nonzero(v1[:,1]==1)/np.shape(vtot)[0]

        
        H_c=calc_entropy(np.count_nonzero(c==1), np.count_nonzero(c==0))
        H_x=calc_entropy((np.count_nonzero(v1[:,1]==1))/np.shape(vtot)[0], (np.count_nonzero(v1[:,1]==0))/np.shape(vtot)[0])
        #entropy of c given that x>t
        H_xc=calc_entropy(p00, p01)+calc_entropy(p10, p11)


        inf_gain=H_c+H_x-H_xc
        igr=inf_gain/H_x
        if igr > max_igr:
            max_igr=igr
            best_t=t
    return  max_igr, best_t




def calc_entropy(p_1, p_2):
    return p_1*np.log2(1/p_1)+p_2*np.log2(1/p_2)


def build(v):
    #stopping conditions
    #1) tutte le classi del vettore sono uguali->classifico il nodo
    if np.all(v[:,3]==v[0,3]):
        #TO DO creo nodo e lo classifico
        #class=v[0,3]
        return


    max_max_igr=0
    best_best_t=0
    for i in range(np.shape(v)[1]):
        #per ogni feature
        max_igr, best_t=find_best_threshold(v[:,i],c)
        if max_igr>max_max_igr:
            max_max_igr=max_igr
            best_best_t=best_t
    v1=v[v[:,0]>best_best_t, :] #vector with values larger than threshold
    v2=v[v[:,0]<=best_best_t,:]

    build(v1)
    build(v2)

    #recur left, recur right
    

