import numpy as np
import seaborn as sns

def unif01_prn(seed=123456789, count=10000):
    result = np.zeros(count)
    x = seed
    for n in range(count):
        x = (x*12773+1)%(2**31 -1)
        r = x/(2**31 -1)
        result[n] = r
    return result

t1 = unif01_prn()
sns.histplot(data=t1,color='grey')


def gen_unif_prn(seed=123456789, count=10000, lower_limit=0, upper_limit=1):
    result = np.zeros(count)
    x = seed
    for n in range(count):
        x = (x*12773+1)%(2**31 -1)
        r = x/(2**31 -1)
        result[n] = lower_limit+(upper_limit-lower_limit)*r
    return result

t2 = gen_unif_prn()
sns.histplot(data=t2)

t3 = gen_unif_prn(lower_limit=10,upper_limit=11)
sns.histplot(data=t3)

t4 = gen_unif_prn(count=100000,lower_limit=5,upper_limit=7)
sns.histplot(data=t4)
