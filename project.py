from collections import defaultdict
import Tools

def main():
    print("--------------------------------------------------------------",'\n')

    files = ["document1.txt","document2.txt","document3.txt","document4.txt","document5.txt"]
    collection = [] 

# here we read the files and remove punc and tokenize them.
    for i in range(len(files)):
        text = open(files[i],'r+').read()
        text = Tools.removePunc(text)
        collection.append(text.split())

# stemming the words of the collection.
    for i in range(0,len(collection)):
        temp_list = Tools.stemWord(collection[i])
        collection[i] = temp_list

    collection_dict = defaultdict(list)

# saving the collection terms to inverted index.
    for i in range(0,len(collection)): 
        doc = collection[i]
        for word in doc:
            
            if word not in collection_dict.keys():
                collection_dict[word] = [i+1]
            else:
                collection_dict[word].append( i+1 )

    for k,v in collection_dict.items():
        print(k,"-->",v)


    x = input("Enter query: ")
    x = x.split()
    operation = x[1]
    key1 = x[0]
    key2 = x[2]
    key1_doc_list = []
    key2_doc_list = []

    for key, val in collection_dict.items():
        if key1 in key:
            key1_doc_list = val
        elif key2 in key:
            key2_doc_list = val

    if operation == "and" or operation == "AND":
        result = Tools.mergeConjuctionSearch(key1_doc_list,key2_doc_list)
    elif operation == "or" or operation == "OR":
        result = Tools.retreivingLists(key1_doc_list,key2_doc_list)

    print(result)
    
    
if __name__ == "__main__":
    main()