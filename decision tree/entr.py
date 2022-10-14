import numpy as np

def calc_entropy(p):
    return np.sum(p*np.log2(1/p))

def calc_igr(H_c, H_1,H_2, H_x):
    return (H_c-(H_1+H_2))/H_x




