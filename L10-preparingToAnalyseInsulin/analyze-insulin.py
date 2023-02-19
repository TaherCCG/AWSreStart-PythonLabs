"""
attempt 1 at making this 1 time use program that will extract the amino acid from cleaned source file to target text files
creates target files if they dont exist. copies the characters into new files and verifies the char count.
"""

from contextlib import redirect_stdout                          # imported to make the output goto file

myList=[]                                                       # set myList as empty 
""" Source File """
with open ('preproinsulin-seq-clean.txt', 'rt') as mainFile:    # Open preproinsulin-seq-clean.txt for reading text as mainFile 
    for myList in mainFile:                                     # gets all characters from mainFile to store in myList
        print()
mainFile.close()                                                # close myfile        

""" Target Files """
with open ('lsinsulin-seq-clean.txt', 'w') as file1:            # open as file1 with write permission
    with redirect_stdout(file1):                                # redirect output to file1
        print(myList[0:24])                                     # prints chars. from 0 to 24 to file1
file1.close()                                                   # close file1

with open ('binsulin-seq-clean.txt', 'w') as file2:             # open as file2        
    with redirect_stdout(file2):                                # redirect output to file2    
        print(myList[24:54])                                    # prints chars. from 25 to 54 to file2    
file2.close()                                                   # close file2

with open ('cinsulin-seq-clean.txt', 'w') as file3:             # Repeated steps as above
    with redirect_stdout(file3):
        print(myList[54:89])                                    # prints chars. from 55 to 89 to file3 
file3.close()

with open ('ainsulin-seq-clean.txt', 'w') as file4:             # same as above
    with redirect_stdout(file4):
        print(myList[89:110])                                   # prints chars. from 90 to 110 to file4 
file4.close()

# Dictionary with files to verify characters in the files
verify={0:'preproinsulin-seq-clean.txt',1:'lsinsulin-seq-clean.txt',2:'binsulin-seq-clean.txt',3:'cinsulin-seq-clean.txt',4:'ainsulin-seq-clean.txt'}
for x in verify:                                                    # loop through number of files in dict.
    with open (verify[x], 'r') as file:                             # Open files in dict. with read access
        data=file.read().strip()                                            # Read data in file
        dataLen=len(data)                                           # check data length                                         
        if x == 0:
            print ("Source file name :{}\n-Number of characters in file :{}\n-Characters: {}\n".format(verify[x],dataLen,data))
        else:
            print ("Target file name :{}\n-Number of characters in file :{}\n-Characters: {}\n".format(verify[x],dataLen,data))
file.close()                                                        # close file


"""
notes.
will try to automate this process on next attempt.
ask user for files to be created.
ask user for number of amino acid chars that need to go in each file
"""