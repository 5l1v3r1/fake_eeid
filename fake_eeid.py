#!/usr/local/bin/python3

import datetime
import random
from datetime import timedelta

#TODO Test for g2_weight case
#TODO Test for ctr == 0 case
#TODO Random gen

def control(id_no_ctr, weight):
    
    ctr = 0

    for index in range(len(id_no_ctr)):
    
        ctr += int(id_no_ctr[index]) * weight[index]
        ctr %= 11

    return ctr

def rand_id():

    d1 = datetime.datetime.strptime('1/1/1800', '%m/%d/%Y')
    d2 = datetime.datetime.strptime('12/31/2199', '%m/%d/%Y')

    print(random_date(d1,d2))

    sex_century = random.randrange(1,8)
    year        = random.randrange(0,99)
    month       = random.randrange(1,12)
    date        = 3 
    serial      = 29 
     
def random_date(start, end):
    range_td = end - start
    range_i = random.randrange(range_td.days)

    delta = timedelta(days = range_i)

    return delta + start
 
def main():

    rand_id()

    sex_century = 3
    year        = 76 
    month       = 5 
    date        = 3 
    serial      = 29 
    # control     = 8
    
    ee_id_no_control = str(sex_century) + str(year) + str(month).zfill(2) + str(date).zfill(2) \
                        + str(serial).zfill(3) 
    
    print(ee_id_no_control)
    
    g1_weight = [1,2,3,4,5,6,7,8,9,1]
    g2_weight = [3,4,5,6,7,8,9,1,2,3]
    
    ctr = control(ee_id_no_control, g1_weight)

    if ctr == 10:
        ctr = control(ee_id_no_control, g2_weight)

    if ctr == 10:
        ctr = 0
   
    print(ctr)


if __name__ == "__main__":
    main()
