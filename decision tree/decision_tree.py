#%%

import numpy as np
from node import Node
import entr
parent=Node(None,None, None, None)
v=np.asarray([[30, 0, 10, 0], [30, 0, 70, 0], [30, 1, 20, 0], [30, 1, 80, 1], [60, 0, 40, 0], [60, 0, 60, 1], [60, 1, 50, 0], [60, 1, 60, 1]])
c=v[:,3]
#t1=np.linspace(np.min(v[:,0]), np.max(v[:,0]), np.shape(np.unique(v[:,0]))[0]+1)[1:-1]
#t2=np.linspace(np.min(v[:,1]), np.max(v[:,1]), np.shape(np.unique(v[:,1]))[0]+1)[1:-1]
#t3=np.linspace(np.min(v[:,2]), np.max(v[:,2]), np.shape(np.unique(v[:,2]))[0]+1)[1:-1]
t1=np.unique(v[:,0])
t2=np.unique(v[:,1])
t3=np.unique(v[:,2])
threshold_l=list()
threshold_l.append(t1)
threshold_l.append(t2)
threshold_l.append(t3)




# %%
def find_best_threshold(v,c, used, index):
   
    max_igr=0
    best_t=0
    for i in range(np.shape(v[:,index])[0]):
        
        if(v[:,index] in threshold_l[index]): #check if the threshold for the specific feature has already been used
            t=v[:,index] #fix a threshold
           
        
            v1=v[v[:,0]>t, :] #vector with values larger than threshold
            v2=v[v[:,0]<=t,:] #vector with values smaller than threshold
            p1=np.count_nonzero(v1[:,1]==1)/np.shape(v1)[0]
            p2=np.count_nonzero(v2[:,1]==1)/np.shape(v2)[0]
            w1=np.shape(v1)[0]/np.shape(v)[0]
            w2=np.shape(v2)[0]/np.shape(v)[0]
            H1=w1*entr.calc_entropy(np.array([p1,1-p1]))
            H2=w2*entr.calc_entropy(np.array([p2,1-p2]))
            

            
            H_c=entr.calc_entropy(np.array[np.count_nonzero(c==1), np.count_nonzero(c==0)])
            H_x=entr.calc_entropy(np.array[w1,w2])
            igr=entr.calc_igr(H_c, H1, H2, H_x)
            if igr > max_igr:
                max_igr=igr
                best_t=t
    return  max_igr, best_t


used=np.zeros([np.shape(v)[0], 3])
def build(v, parent):
    

    max_max_igr=0
    best_best_t=0
    best_feat=0
    for i in range(3):
        #per ogni feature
        max_igr, best_t=find_best_threshold(v[:,[i,3]],c, used, i)#passo come matrice la colonna della feature presa in considerazione e quella delle classi
        if max_igr>max_max_igr:
            max_max_igr=max_igr
            best_best_t=best_t
            best_feat=i
    threshold_l[best_feat].remove(best_t)

    parent.threshold=best_best_t
    v1=v[v[:,best_feat]>best_best_t, :] #vector with values larger than threshold
    v2=v[v[:,best_feat]<=best_best_t,:]

    if np.all(v1[:,3]==v1[0,3]):#il vettore v1 è tutto uguale come classe
        parent.c1=v1[0,3]
    else:
        build(v1,parent.c1)
    if np.all(v2[:,3]==v2[0,3]):
       parent.c2=v2[0,3]#il vettore v2 è tutto uguale come classe
    else:
        build(v2,parent.c2)

   
    return

    #recur left, recur right
    