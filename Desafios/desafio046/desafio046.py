from time import sleep
from modules.cores import creturn
for i in range(10,0,-1):
    print(i)
    sleep(1)
print('{} {} {}'.format(creturn('BOMMM!',c='blue'),creturn('BOMM!',c='red'),creturn('BOMM!',c='yellow')))