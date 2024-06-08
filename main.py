#BookBot
# a simple terminal based program that generates a report over a book or txt file printing out how many characters are used and how many times and how many words are there in it.
import string


def appearance(word):                         #function to count how many times a letter appeared in a string
    char_count ={}                            #creating an empty dictionary to store resutls
    word = str(word)                          #typecasting the argument into string as .lower fucntion treats it as a list
    lowered_string = word.lower()             # using the .lower function to convert the string to lowercase to avoid double counting
    for char in lowered_string:               #for loop to loop over the lowered string 
        if char in char_count:                #if the character already exists then it's value will be increased
            char_count[char] +=1
        else:                                 #if a character doesn't exist it will be added to dictionary
            char_count[char] = 1
    return char_count


def alphachecker(alp):                       #takes a dictionary as input
    new_alp = {}                              # creating new empty dictionary
    for char, count in alp.items():           # looping over both key and values of input dictionary using .items functions which allows to loop over key and value in one loop
            if char.isalpha():                # checking if the key is alpha
                new_alp[char] = count           # asigning the key it's value but in new dictionary
    return new_alp                             #returning the dictionary


def main():
    with open("Books/books.txt") as f:           #opens the file as variable f
        file_content = f.read()                  #reads the content of file and stores it int file_content
    
    print("--- Begin Report ---")
    word = file_content.split()                  #splits the string whitespace and stores it in word
    print(len(word), " words were found in the document")                            #print length of word
     
    char_count = appearance(word)                 #calling the appearance function

    new_alp = alphachecker(char_count)
    for char,count in new_alp.items():
        print(f"The {char} character was found {count} times ")

    print("--- End Report ---")


if __name__=="__main__":                         #usese namespace to use main function
    main() 