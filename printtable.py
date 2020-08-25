def multtable(start, stop, number):
    """
    Print multiplication table for <number>
    from <start> to including <stop> 
    """
    for i in range(start, stop+1):
        print(f"{i} x {number} = {i*number}")


    
def powertable(to_power_of, the_base):
    """
    Prints the table with numbers resulting in counting all 
    results of power to to_power_of, numbers in range of one to the_base
    """
    for i in range(1,the_base+1):
        x = (i**to_power_of)
        print (x)
        
if __name__ == '__main__':
    powertable(3,3)