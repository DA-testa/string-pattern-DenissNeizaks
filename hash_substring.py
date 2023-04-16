def read_input():
    input_method = input()
    if "I" in input_method:
        pattern = input()
        text = input()
        return (pattern, text)
    elif "F" in input_method:
        file = "06.txt"
        file = ("tests/" + file)
        with open(file,'r') as f:
            pattern = f.readline()
            text = f.readline()
        f.close()
        return (pattern, text)
    
    
def print_occurences(output):
    print (output)
    
    
def get_occurences(pattern, text):
    String = ""
    array = []
    for i in range (len(text)):
        if (text[i] == pattern[0]):
            test = True
            currenttext = text [i:i+len(pattern)]

            for j in range (len(currenttext)):
                if (len(currenttext) < len(pattern)):
                    test = False
                    break
            
                if (pattern[j] == currenttext[j]):

                    continue
                
                else:
                    test = False
                    break
        
            if (test == True):
                array.append(i)
            
    for i in range (len(array)):
        String = String + str(array[i]) + " "
    return (String)
    
if __name__ == '__main__':
    input_list = read_input()
    
    a = input_list[0]
    a = a[0:len(a)-1]

    print_occurences(get_occurences(a, input_list[1]))
