import re
#a='今天是ffsdf期的g六'
#print(re.sub('[a-zA-z0-9]','',a))
#file_object=open('/Users/han/PycharmProjects/NLP/w0.txt')
#file_content=file_object.read()
#file_object.close()
#to_convert=file_content
#converted=re.sub('[a-zA-z0-9]','',to_convert)
#f=open('clean.txt','w+')
#f.write(converted)

file=open('/Users/han/PycharmProjects/NLP/opencc-python-reimplemented-0.1.5/clean.txt')
content=file.read()
file.close()
articles=content
#articles=articles.split('\n')
def token(string):
    return re.findall('\w+',string)
#articles_clean=[''.join(token(str(a)))for a in articles]
articles_clean=''.join(token(articles))
f=open('clean1.txt','w+')
f.write(articles_clean)
#with open('clean1star.txt','w') as f:
#    for a in articles_clean:
#        f.write(a+'\n')