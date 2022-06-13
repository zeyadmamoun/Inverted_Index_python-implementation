import string
from nltk import PorterStemmer

# removing punctuation from text.
def removePunc(text):
    return text.translate(str.maketrans('', '', string.punctuation))


# Stemming everyword in a list of words to its root.
def stemWord(words):
    ps = PorterStemmer()
    stemWords = []
    for w in words:
        stemWords.append(ps.stem(w,True))

    return stemWords

# Get the number of occurence for every word in the doucment.
def getFrequancy(word,listOfWords):
    freq = listOfWords.count(word)
    return freq


def mergeConjuctionSearch(list1,list2):
    temp_list1 = []
    temp_list2 = []
    temp_list1 = list1
    temp_list2 = list2
    answer_list = []

    x,y = (0,0)

    while x != len(temp_list1) and y != len(temp_list2):
        if temp_list1[x] == temp_list2[y]:
            answer_list.append(temp_list1[x])
            x=x+1
            y=y+1
        elif temp_list1[x] > temp_list2[y]:
            y =y+1
        elif temp_list1[x] < temp_list2[y]:
            x=x+1
    
    return answer_list

def retreivingLists(list1,list2):
    temp_list1 = []
    temp_list2 = []
    temp_list1 = list1
    temp_list2 = list2
    answer_list = []

    answer_list = temp_list1 +  temp_list2
    answer_list = list(set(answer_list ))
    return answer_list