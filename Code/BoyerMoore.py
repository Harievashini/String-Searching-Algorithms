# Boyer Moore algorithm

#importing the time package
import time

NO_OF_CHARS = 256  #Number of characters

#Function to preprocess the pattern using ad character heuristic
def badCharacterHeuristic(pattern, pattern_len): 
    badChar = [-1]*NO_OF_CHARS  #initializing all occurences as -1
    for i in range(pattern_len): 
        badChar[ord(pattern[i])] = i; 
    return badChar 
  
# Function to implement string searching
def boyermoore_search(pattern, text): 
    pattern_len = len(pattern)  #length of pattern
    text_len = len(text)        #length of text
    no_of_searches=0     #To keep count of the searches
    badChar = badCharacterHeuristic(pattern, pattern_len)  #Preprocess the pattern
    s = 0  #s is the shift of the pattern with respect to text
    while(s <= text_len-pattern_len): 
        j = pattern_len-1
        while j>=0 and pattern[j] == text[s+j]: 
            j -= 1
        #output the index at which the pattern is found
        if j<0: 
            print("Pattern found at index = {}".format(s)) 
            no_of_searches+=1
            s += (pattern_len-badChar[ord(text[s+pattern_len])] if s+pattern_len<text_len else 1) 
        else: 
            s += max(1, j-badChar[ord(text[s+j])])
    #checking the ocurrences of pattern
    if(no_of_searches==0):
        print("Pattern not found")
    else:
        print(no_of_searches," Results found")

#Fetching the file and reading the input from the file
txt=open("littlewomen.txt" ,"r")
string_text=txt.readlines()
txt.close()
text=""
#converting the input from list form to string form
for i in string_text:
    text+=i
#pattern to be searched
pattern = "Was it all self-pity, loneliness, or low spirits?  Or was it the waking\n"+"up of a sentiment which had bided its time as patiently as its\n"+"inspirer?  Who shall say?"
if(pattern==''):
    print("The pattern is empty, searching not required")
else:
    if(text==''):
        print("Text file is empty, cannot search the pattern")
    else:
        #Start time of the execution
        start = time.time()
        #search the pattern using boyermoore algorithm, call to boyermoore_search function
        boyermoore_search(pattern,text)
        #End time of the execution
        finish = time.time() 
        #Output the amount of time taken to implement the algorithm
        print("Execution time =",(finish-start),"s")   
