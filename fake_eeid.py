#!/usr/local/bin/python3

#TODO Test for g2_weight case
#TODO Test for ctr == 0 case
#TODO Random gen

def control(id_no_ctr, weight):
    
    ctr = 0

    for index in range(len(id_no_ctr)):
    
        ctr += int(id_no_ctr[index]) * weight[index]
        ctr %= 11

    return ctr
    
 
def main():
    
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
