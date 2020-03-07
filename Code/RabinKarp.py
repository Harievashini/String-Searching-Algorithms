# Rabin-Karp algorithm

#importing the time package
import time

d = 256 # Number of characters in the input alphabet
q = 101 # A prime number 

# Function to implement string searching
def rabinkarp_search(pattern, text): 
    pattern_len = len(pattern)   #length of pattern
    text_len = len(text)         #length of text
    p = 0    # hash value for pattern
    t = 0    # hash value for text 
    h = 1
    no_of_searches=0  #To keep count of the searches
    #h=pow(d,pattern_len-1)%q
    for i in range(pattern_len-1): 
        h = (h*d)%q 
    for i in range(pattern_len): 
        p = (d*p + ord(pattern[i]))%q  # calculating hash value of pattern
        t = (d*t + ord(text[i]))%q     # calculating hash value for first window of text
    for i in range(text_len-pattern_len+1): 
        #checking the hash value of both match
        if p==t: 
            for j in range(pattern_len): 
                if text[i+j] != pattern[j]: 
                    break
            j+=1
            #output the index at which the pattern is found
            if j==pattern_len: 
                print("Pattern found at index " + str(i))
                no_of_searches+=1 
        #calculating hash value for the next window of text
        if i < text_len-pattern_len: 
            t = (d*(t-ord(text[i])*h) + ord(text[i+pattern_len]))%q  
            if t < 0: 
                t = t+q 
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
        #search the pattern using rabinkarp algorithm, call to rabinkarp_search function
        rabinkarp_search(pattern,text)
        #End time of the execution
        finish = time.time() 
        #Output the amount of time taken to implement the algorithm
        print("Execution time =",(finish-start),"s")   

