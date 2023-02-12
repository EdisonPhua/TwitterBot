import functions


print('Time to generate new articles')
exec(open("Source/NewsData.py").read())
print('Generated')  

tweet, link = functions.NewsLooper()

text = sent_tokenize(tweet)[:5]
text = ' '.join(text)
count = 0

print(text)