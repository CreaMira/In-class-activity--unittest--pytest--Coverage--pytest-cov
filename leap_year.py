def is_leap_year(years):

    divisible_4 = years%4

    if divisible_4 == 0:
        
        divisible_100 = years%100
        
        if divisible_100 == 0:
            
            divisible_400 = years%400
            
            if divisible_400 == 0:
                #print(years, "is leap year")
                return True
            else:
                #print(years, "is not leap year")
                return False
        
        else:
            #print(years, "is leap year")
            return True
        
    else:
        #print(years, "is not leap year")
        return False

if __name__ == '__main__':
    is_leap_year(1)
    is_leap_year(100)
    is_leap_year(8)
    is_leap_year(400)