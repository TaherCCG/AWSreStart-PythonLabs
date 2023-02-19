print("Mixed type list/n")

""" Creating a mixed-type list """

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]   # defines myMixedTypeList as variable with mixed types of data
for item in myMixedTypeList:                                                # goes through each item separated by comma in the list variable
    print("{} is of the data type {}".format(item,type(item)))              # prints each list item, then item class (object type) as formatted message.
   
    