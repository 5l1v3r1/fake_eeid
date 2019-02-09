#!/usr/local/bin/python3

import datetime
import random
from datetime import timedelta
from random import randint
import weights

#TODO Test for g2_weight case
#TODO Test for ctr == 0 case / 5711030188
#TODO Random gen


def control(ee_id_no_control):

    g1_weight = weights.g1
    g2_weight = weights.g2
    grade = 1
    
    ctr = calc_control(ee_id_no_control, g1_weight)

    if ctr == 10:
        ctr = calc_control(ee_id_no_control, g2_weight)
        grade = 2

        if ctr == 10:
            ctr = 0

    return ctr, grade

def calc_control(id_no_ctr, weight):
    
    ctr = 0

    for index in range(len(id_no_ctr)):
    
        ctr += int(id_no_ctr[index]) * weight[index]
        ctr %= 11

    return ctr

def random_id(rand_date):

    sex_century = (int(rand_date.year / 100) - 17) * 2 - randint(0, 1)
    year        = rand_date.year % 100
    month       = rand_date.month
    date        = rand_date.day
    serial      = random.randrange(0,999)

    ee_id_no_control = str(sex_century) + str(year) + str(month).zfill(2) + str(date).zfill(2) \
                        + str(serial).zfill(3) 
    
    return ee_id_no_control
     
def random_date(start, end):
    range_td = end - start
    range_i = random.randrange(range_td.days)

    delta = timedelta(days = range_i)

    return delta + start
 
def main():

    d1 = datetime.datetime.strptime('1/1/1800', '%m/%d/%Y')
    d2 = datetime.datetime.strptime('12/31/2199', '%m/%d/%Y')

    rand_d = random_date(d1, d2)
    ee_id_no_control = random_id(rand_d)
    
    ctr, grade = control(ee_id_no_control)
    
    ee_id = ee_id_no_control + str(ctr)
   
    print("Random Date     : ", rand_d)
    print("Personal Number : ", ee_id)
    print("Grade           : ", grade)


if __name__ == "__main__":
   main()
    
