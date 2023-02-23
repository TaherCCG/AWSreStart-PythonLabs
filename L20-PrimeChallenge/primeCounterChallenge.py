from contextlib import redirect_stdout                          # imported to make the output goto file

start = 1                                                       # define var start for Starting number      
end = 250                                                       # define var end for ending number

print("You can also find the results in 'results.txt' file.")   # print message to notify the results will be in results.txt file
with open ('results-google.txt', 'w') as f1:                           # with open file results.txt as f1
    f1.write("Prime numbers between 1 and 250 are:\n")          # Prints message at line 1 of file
    for num in range(start,end):                                # loop num in range of start to end
        prime=True                                              # define var prime as True     
        for x in range(2, num):                                 # loop x in range 2 to num
            if (num%x == 0):                                    # if num remainder x = 0
                prime=False                                     # then var prime is false
        if prime:                                               # if prime then
            with redirect_stdout(f1):                           # with open redirect standard output to file f1
                print(str(num))                                 # print string num to f1 (file: results.txt)
f1.close()                                                      # close file f1 (results.txt)
