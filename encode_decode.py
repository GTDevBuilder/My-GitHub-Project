#! /usr/bin/python3

import sys

#defining characters arrays
array1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

array2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

array3 = ['~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}',']','|',':','<','>','.','?']

array4 = ['1','2','3','4','5','6','7','8','9','0']

#setting the offset for each array
offset1 = 0
offset2 = len(array1)
offset3 = len(array2) + offset2 
offset4 = len(array3) + offset3
totalChars = len(array4) + offset4

#Printing offsets and totals
print(f' os1 {offset1} os2 {offset2} os3 {offset3} os4 {offset4}')
print(f'Total chars all arrays = {len(array4) + offset4}')


#testing argument 
print(sys.argv[1:])
for chars in sys.argv[1:]:
    print("%s \n" % chars)

#copy arguments to key array
# sys.argv[1] is chars  sys.argv[1:] is word
#copy key argument into key_array
key_array = list(sys.argv[1])
print('key_array is %s' % key_array)

############################ input character get index number #########
#get array index from character
def get_index(character):
    #setting array index to copy
    count = 0
    temp_array = character

    #find which array contains the character
    for elem in character:
        #print(elem)
        if elem in array1:
            aryIndex = array1.index(elem)
           #print("%s index is %d"% (elem, aryIndex))
            temp_array[count] = aryIndex
        if elem in array2:
            aryIndex = array2.index(elem)
            #print("%s index is %d"% (elem, (aryIndex + offset2)))
            temp_array[count] = (aryIndex + offset2)
        if elem in array3:
            aryIndex = array3.index(elem)
            #print("%s index is %d"% (elem, (aryIndex + offset3)))
            temp_array[count] = (aryIndex + offset3) 
        if elem in array4:
            aryIndex = array4.index(elem)
            #print("%s index is %d"% (elem, (aryIndex + offset4)))
            temp_array[count] = (aryIndex + offset4)
        count = count +1
    return temp_array
#####################################################################

##########################
#convert key array to offset values
key_offset = get_index(key_array)
print(f'key offset array {key_offset}')

######################### Input index number and get Character ###########
#return character at array index number
#this is called from the get_character function
def get_element(arrayNumber, indexNumber):
    letter = ''
    letter = arrayNumber[indexNumber]
    return letter

#determine array from index number
def get_character(indexNumber):
    letter = 'x'
    # Array 4
    if indexNumber >= offset4:
        letter = get_element(array4, (indexNumber - offset4))
    # Array 3    
    elif indexNumber >= offset3:
        letter = get_element(array3, (indexNumber - offset3))
    # Array 2    
    elif indexNumber >= offset2:
        letter = get_element(array2, (indexNumber - offset2))
    # Array 1    
    else:
        letter = get_element(array1, indexNumber)
    return letter

#########################################################################

######################### Read in file line by line ###################
#read file line by line into a list
#get password file into line array
#Array of each line of the password file
lines = []
def readFile(psswrdFile):
    with open(psswrdFile) as f:
        global lines
        lines = f.readlines()


####################################################################

#print out file line by line
def printFile(lineArray):
    count = 0
    for line in lineArray:
        count += 1
        if len(lines[count -1].split()) > 1:
            print(f'line {count}: {line}')
        else:
            print(f'line {count}')

#test function
readFile('passwordFile.txt')
#printFile(lines)

################################## convert number to letter ###########
#Iterate words in each line
#Convert to number to letter
def numbArray_to_letter(numbArray):
    wdArray = ''
    for x in range(len(numbArray)):
        nb = int(numbArray[x])
        #print(f' nb is {nb}')
        wdArray += get_character(nb)
        #print(f' word array is {wdArray}')
    return wdArray

###################################################################

#test function
#tmpWdArray = ['27', '40', '39', '29', '26', '32', '30']
#tstArray = numbArray_to_letter(tmpWdArray)
#print(f'numb to letter {tstArray}')

#################################convert word to number array#########
#this works and is easier than all of the temp arrays
#convert each word to number array
#then convert number array back to word
#we can now add in the offset
lnCount = 0
lnArray = []
nlArray = []
#encode line by line
for line in lines:
    lnCount += 1
    #print(f'line {lnCount} {line}')
    tmpEncode = get_index(list(line))
    lnArray.append(tmpEncode)
    #print(f'line {lnCount} {tmpEncode}')
    # encode word for word
    for w in line.split():
        print(f'word is  {w}')
        tmpEncode = get_index(list(w))
        print(f'tmpEncode is {tmpEncode}')
        #insert encode command
        #encodeArray(tmpEncode, key_array)
        ##The next two functions will be in the decoder
        nlArray = numbArray_to_letter(tmpEncode)
        print(f'back to word = {nlArray}')
        #wdArray.append(tmpEncode)
####################################################################3



########################---Testing functions ---------------##################

#Building the encodyer
#Encode the file by adding the key value to the password
#all works 
#added checks in for greater than total characters
#if greater subtract total characters from number
#This with will cause the function to loop through all of the arrays
#function takes int array not char array need to convert char to numbers before calling
#####################Encode array with Key value ###############
keyCounter = 0
def encodeArray(encArray, keyArray):
    print(f' keyArray length = {len(keyArray)}')
    global keyCounter
    p = 0
    tmpArray = ''
    for x in encArray:
        #reset key counter to re run key value
        if keyCounter > len(keyArray) -1:
            keyCounter = 0
        
        print(f' x = {x}')
        print(f' keyArray Value = {keyArray[keyCounter]}')
        p = int(x) + int(keyArray[keyCounter])
        #check if encoded value is greater than total chars
        #if so subtract total chars to wrap around to first array
        if p > totalChars:
            print('have to wrap')
            p = p - totalChars
        tmpArray += get_character(int(p))
        print(f' p Value = %s {p}')
        keyCounter += 1
    print(f' tmpArrayChar = {tmpArray}')
    return tmpArray

#######################################################################3

#testing encoder

#tmpWdArray = ['27', '40', '39', '29', '26', '32', '30']
tmpWdArray = ['0', '1', '2', '3', '4', '5', '6']
bbArray = encodeArray(tmpWdArray, key_array)
print(f' bbaray test {bbArray}')

#decoder
keyCounter1 = 0
def decodeArray(encArray, keyArray):
    print(f' keyArray length = {len(keyArray)}')
    global keyCounter1
    p = 0
    tmpArray = ''
    for x in encArray:
        #reset key counter to re run key value
        if keyCounter1 > len(keyArray) -1:
            keyCounter1 = 0
        
        print(f' x = {x}')
        print(f' keyArray Value = {keyArray[keyCounter1]}')
        p = int(x) - int(keyArray[keyCounter1])
        #check if encoded value is greater than total chars
        #if so subtract total chars to wrap around to first array
        if p < 0:
            print('have to add totalChars')
            p = p - totalChars
        tmpArray += get_character(int(p))
        print(f' p Value = %s {p}')
        keyCounter1 += 1
    print(f' tmpArrayChar = {tmpArray}')
    return tmpArray


#delete encryption file before writing
def deleteFile(FileName):
    with open(FileName, 'w') as f:
        pass
    
#how to write to a file
def writeToFile(encArray):
    with open('encrypted_File.txt', 'w') as writer:
        writer.write(encArray)


#testing writeToFile function
writeToFile(bbArray)
deleteFile('encrypted_File.txt')
writeToFile(bbArray)



#Encoder 
#def encodeFile(pswdFile, key):
    #read password file  line by line
    #turn words to list of chars
    #turn chars to numbers
    #encode numbers with key
    #turn encoded numbers back to letters
    #write to file

#end of function

