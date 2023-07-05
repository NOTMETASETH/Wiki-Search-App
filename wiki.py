import wikipedia

query = input("Enter the topic name : \n")

result = wikipedia.summary(query)

print(result)