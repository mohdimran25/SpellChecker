from textblob import TextBlob

with open("demo_file.txt","r+") as file:
    a = file.read()
    print("Original Text : ",str(a))
    b = TextBlob(a)
    print("Correct text: ",str(b.correct()))
with open("demo_file.txt","w") as file:
    file.write(str(b.correct()))