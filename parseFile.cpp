/*Encode using ascii start with 32 and end with 126
 * This includes all printable characters
 *logic is as follows:
 Key word ascii value is added to target (pswwd) value
 if the sum is greater than 126 the sum is subtracted from 126 and 
 added to 32.
 */

/* Decode logic using the ascii value of the key word subtract from ascii target
 * value.  If the value is less than 32 the value is subtracted from 126
 * to get the decoded ascii value of the target char. 
*/

/*Program Arguments
 * Argument 1 = psswd file
 * Argument 2 = code word
 */


#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

/////////////////////////////Start//////////////////////////
//Set key value
//Getters and setters Accessors and Mutators
char *key;
void setKey(char *keyValue) { key = keyValue; }
char *getKey() { return key; }

//Convert string to Char array
char *strToCharArray(string str)
{
	//create char array from string
	char *convert = new char[str.length() + 1];
	//copy string into char array
	strcpy(convert, str.c_str());
	//return array
	return convert;
}

//calculate new value
int calculateValue(char target, char key){
int val = 0;
return val;

}

//Encoding file
void encode(string value)
{
	char *strValue = strToCharArray(value);
	char *keyValue = getKey();
	char *encodeValue = new char[value.length() + 1];
	int count = 0;
	int keySize = strlen(keyValue);
	int valueSize = strlen(encodeValue);

//	printf("keyvalue size = %d\n", keySize);

	for (int b = 0; b < value.length(); b++)
	{
		printf("%c", strValue[b]);
		printf("%c", keyValue[count]);
		//incrementing keyvalue with out over running array
		count ++;
		//increment count to move to next key letter
		if(count > keySize)
		{
			count = 0;
		}
		
		
	}

	//prints one line at a time
	printf("\n");

	for (int x = 0; x < keySize; x++)
	{
		printf("%c", keyValue[x]);
	}

	printf("\n");
}

void encodeline(char *key, string)
{
	//ascii of encoded value
}

void asciiValue(string str3)
{
	//convert str to char
	char *convert = new char[str3.length() + 1];
	//copy string into char array
	strcpy(convert, str3.c_str());
	//print value of each char
	for (int b = 0; b < str3.length(); b++)
	{
		printf("char value is %c  ", convert[b]);
		printf("ascii value is %d\n", (int)convert[b]);
	}

	encode(str3);
}

void swapp(string str2)
{
	string test = "naked";
	size_t found = str2.find(test);

	if (found != string::npos)
	{
		printf("found naked");
		asciiValue(str2);
	}
}

//Open fle and read line by line
void openpasswdFile(char *fileName, char *key)
{
	//set Keyvalue to key
	setKey(key);
	//open pswwd file
	ifstream file(fileName);
	string str;

	//read file line by line
	while (getline(file, str))
	{
		//Call function str = line of text
		//
		//Insert function here
		//asciiValue(str);
		encode(str);

	}
	
	//Close string
	file.close();
}

//Main application
int main(int argc, char *argv[])
{

	//string parsefile;

	//check if file and keyword are present
	if (argc < 3)
	{
		printf("please enter parse file and key word\n");
		return 0;
	}

	char *codeword = argv[2];
	char *fileName = argv[1];

	//Test arguments
	printf("file Name is %s, and keyword is %s \n", fileName, codeword);
	//Open file call
	openpasswdFile(fileName, codeword);
}
