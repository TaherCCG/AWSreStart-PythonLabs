import jsonFileHandler                                                          # import jsonFileHandler

data = jsonFileHandler.readJsonFile('files/insulin.json')                       # define var data as  jsonFileHandler.readJsonFile('files/insulin.json') reads file insulin.json

if data != "" :                                                                 # if var data is not empty/none
    bInsulin = data['molecules']['bInsulin']                                    # define var bInsulin as data value (from file) molecules dictionary and bInsulin as key
    aInsulin = data['molecules']['aInsulin']                                    # define var aInsulin as data value (from file) molecules dictionary and aInsulin as key
    insulin = bInsulin + aInsulin                                               # define var insulin as concatenate of bInsulin and aInsulin    
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']         # define var molecularWeightInsulinActual as data (from file) molecularWeightInsulinActual key
    print('bInsulin: ' + bInsulin)                                              # print bInsulin
    print('aInsulin: ' + aInsulin)                                              # print aInsulin
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual)) # print molecularWeightInsulinActual as a string

    
    # Calculating the molecular weight of insulin  
    # Getting a list of the amino acid (AA) weights  
    aaWeights = data['weights']                                                 # define var aaWeights as data( from file) as weights key
    # Count the number of each amino acids  
    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  
    # above line defines aaCountInsulin as x as a float and counts uppercase in insulin for each character
    
    # Multiply the count by the weights  
    molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in        # defines var molecularWeightInsulin and calculates x as aaCountInsulin[x]*aaWeights[x] ([x] is each character)
    # and loops x the amount of time it finds the following characters
    ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  
    print("The rough molecular weight of insulin: " +  str(molecularWeightInsulin))   # prints  molecularWeightInsulin as a string
    print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100)) 
    #above line prints above calculation as a string to output the percentage error
else:                                                                           # else    
    print("Error. Exiting program")                                             # print error message