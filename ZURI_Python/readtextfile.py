# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):

    #open file
    file = open(filename, "r")
    
    #read content of file
    content = file.read()

    #close file
    file.close()
    
    #return file content
    return content


# count words in story.txt
def count_words():
    #split text into words
    text = read_file_content("./story.txt")
    words = text.split()
    
    #empty dictionary
    word_count = {}
    
    #loop through word
    for word in words:

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    #return dictionary
    return word_count

print(count_words())





#return {"as": 10, "would": 20}
