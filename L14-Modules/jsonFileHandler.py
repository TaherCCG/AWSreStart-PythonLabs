import json									                                     # import json module 	

def readJsonFile(fileName):                                                      # define readJsonFile(fileName) as function with fileName as argument
    data=""                                                                      # define var as data with empty string
    try:                                                                         # try
        with open('files/insulin.json') as json_file:                            # open file as json_file   
            data = json.load(json_file)                                          # define var data with new value as load jason_file 
    except IOError:                                                              # on try error
         print("Could not read file")                                            # print message
    return data                                                                  # return data (function)