def seasons(year, month, day):
    """
    (int, int, int) -> [str, int]
    A function that is passed a month and day, determines the season, and then 
    calculates the number of days since the current season begins and returns
    the season and days as a two element list.

    Students may assume that the seasons begin on the 21st day of March, June,
    September and December. Student SHOULD consider leap year. 

    Please refer to the handout for test cases and error conditions.
    """
    # Here I declair the number of days in the respective months of a year.
    
    days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    output = ['str', 1]
        
    if (year % 4 == 0 and year % 100 !=0) or (year % 4 == 0 and year % 100 == \
        0 and year % 400 == 0):
        num_year = 366                  # Number of years in a leap year.
        print ("leap year")
        days_in_months[1] = 29          # Takes care of change in number of 
                                        #days in February due to leap year.
    else:
        num_year = 365                  # Number of years in a normal year.
    days_since_beginning = 0
    
    if month >= 1:
        days_since_beginning += 0
    if month >= 2:
        days_since_beginning += days_in_months[0] 
    if month >= 3:
        days_since_beginning += days_in_months[1] 
    if month >= 4:
        days_since_beginning += days_in_months[2] 
    if month >= 5:
        days_since_beginning += days_in_months[3] 
    if month >= 6:
        days_since_beginning += days_in_months[4] 
    if month >= 7:
        days_since_beginning += days_in_months[5]  
    if month >= 8:
        days_since_beginning += days_in_months[6] 
    if month >= 9:
        days_since_beginning += days_in_months[7]
    if month >= 10:
        days_since_beginning += days_in_months[8]
    if month >= 11:
        days_since_beginning += days_in_months[9] 
    if month >= 12:
        days_since_beginning += days_in_months[10]
    days_since_beginning += day
    
    print("days since the year is: ", days_since_beginning)
        
    if (days_since_beginning >= 52 + days_in_months[1] and days_since_beginning < 144 + days_in_months[1]):
        output[0] = "spring"
        output[1] = days_since_beginning - (52 + days_in_months[1])
    elif (days_since_beginning >= 144 + days_in_months[1] and days_since_beginning < 236 + days_in_months[1]): 
        output[0] = "summer"
        output[1] = days_since_beginning - (144 + days_in_months[1])
    elif (days_since_beginning >= 236 + days_in_months[1] and days_since_beginning < 327 + days_in_months[1]): 
        output[0] = "autumn"
        output[1] = days_since_beginning - (236 + days_in_months[1])
    elif days_since_beginning >= 0 or days_since_beginning >= 327 + days_in_months[1]:
        output[0] = "winter"
        if days_since_beginning < 52 + days_in_months[1]:
            output[1] = (10 + days_since_beginning)
        else:
            output[1] = days_since_beginning - (327 + days_in_months[1])
            
    if month > 12 or month < 1:
        output = ['invalid month', -1]
    elif day > 31 or day < 1:
        output = ['invalid day', -1]
    elif (month == 4 or month == 6 or month == 9 or month == 11) \
          and day > 30:
        output = ['invalid month', -1]
    elif (month == 2) and (day > days_in_months[1]):
        output = ['invalid day', -1]

    return output


        
    
    
    