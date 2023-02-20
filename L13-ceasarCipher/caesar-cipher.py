
def getDoubleAlphabet(alphabet):                                                # Define getDoubleAlphabet as function that takes a string argument concatenates or combines the given string
    doubleAlphabet = alphabet + alphabet                                        # Define var doubleAlphabet that concatenates the function strings into one string
    print(doubleAlphabet)                                                       # prints var doubleAlphabet
    return doubleAlphabet                                                       # returns doubleAlphabet

def getMessage():                                                               # Define getMessage as a function that gets input (function) string arguments from user                
    stringToEncrypt = input("Please enter a message to encrypt: ")              # define ver stringToInput gets input from user to use as a function string
    return stringToEncrypt                                                      # return stringToFunction
    
def getCipherKey():                                                             # define getCipherKey as a function that gets input (function) string arguments from user
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")       # define var shiftAmount gets input from user to use as a function string
    return shiftAmount                                                          # return shiftAmount
    
def encryptMessage(message, cipherKey, alphabet):                               # define encryptMessage as a function that takes function string arguments from (above 3 functions) message, cipherKey and alphabet 
    encryptedMessage = ""                                                       # define var encryptedMessage as empty string
    uppercaseMessage = ""                                                       # define var uppercaseMessage as empty string 
    uppercaseMessage = message.upper()                                          # define var uppercaseMessage to new value as message.upper()
    for currentCharacter in uppercaseMessage:                                   # loop for currentCharacters in uppercaseMessage   
        position = alphabet.find(currentCharacter)                              # define var position that finds alphabet in currentMessage  
        newPosition = position + int(cipherKey)                                 # define var newPosition that concatenates position and integer cipherKey
        if currentCharacter in alphabet:                                        # check if currentCharacter in alphabet    
            encryptedMessage = encryptedMessage + alphabet[newPosition]         # define var encryptedMessage to new value that concatenates var encryptedMessage with function argument alphabet(newPosition)
        else:                                                                   # else 
            encryptedMessage = encryptedMessage + currentCharacter              # defines new value for var encryptedMessage as concatenates of encryptedMessage and currentCharacter     
    return encryptedMessage                                                     # return encryptedMessage
    
def decryptMessage(message, cipherKey, alphabet):                               # define decryptMessage as a function that takes function string arguments from (3 function arguments) message, cipherKey and alphabet 
    decryptKey = -1 * int(cipherKey)                                            # define var decryptKey as -1 * integer(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)                        # returns encryptMessage functions with three arguments message, decryptKey and alphabet   
    
def runCaesarCipherProgram():                                                   # define runCaesarCipherProgram as function with no arguments
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"                                     # define var myAlphabet with string
    print(f'Alphabet: {myAlphabet}')                                            # print formatted string with var myAlphabet
    myAlphabet2 = getDoubleAlphabet(myAlphabet)                                 # define var myAlphabet2 as getDoubleAlphabet function with argument as myAlphabet
    print(f'Alphabet2: {myAlphabet2}')                                          # print formatted string with var myAlphabet2
    myMessage = getMessage()                                                    # define myMessage as getMessage function     
    print(myMessage)                                                            # print var myMessage    
    myCipherKey = getCipherKey()                                                # define var myCipherKey as getCipherKey function 
    print(myCipherKey)                                                          # print var myCipherKey        
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)    # define var myEncryptedMessage as decryptedMessage function with 3 arguments myEncryptedMessage, myCipherKey, myAlphabet2
    print(f'Encrypted Message: {myEncryptedMessage}')                           # print formatted string with var myEncryptedMessage
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)   # define var myDecryptedMessage as decryptMessage function with 3 arguments myEncryptedMessage, myCipherKey, myAlphabet2
    print(f'Decrypted Message: {myDecryptedMessage}')                           # print formatted string with var myDecryptedMessage
    
runCaesarCipherProgram()                                                        # calls the function runCaesarCipherProgram()