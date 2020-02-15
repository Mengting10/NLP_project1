import random
import re
import jieba
import pandas as pd
from collections import Counter
"""
filename='/Users/han/Desktop/datasource-master/sqlResult_1558435.csv'
content=pd.read_csv(filename,encoding='gb18030')
articles=content['content'].tolist()
def token(string):
    return re.findall('\w+',string)
articles_clean=[''.join(token(str(a)))for a in articles]
with open('a0.txt','w') as f:
    for a in articles_clean:
        f.write(a+'\n')
def cut(string): return list(jieba.cut(string))
TOKEN=[]
for i,line in enumerate((open('a0.txt'))):
    TOKEN+=cut(line)
words_count=Counter(TOKEN)
def prob_1(word):
    return words_count[word] / len(TOKEN)
TOKEN=[str(t) for t in TOKEN]
TOKEN_2_GRAM=[''.join(TOKEN[i:i+2]) for i in range(len(TOKEN[:-2]))]
words_count_2=Counter(TOKEN_2_GRAM)
def prob_2(word1, word2):
    if word1 + word2 in words_count_2: return words_count_2[word1+word2] / words_count[word2]
    else:
        return 1 / len(TOKEN_2_GRAM)

file=open('/Users/han/Desktop/NLP/lesson 1/article_9k.txt')
content=file.read()
file.close()
articles=content
def token(string):   #去除特殊符号
    return re.findall('\w+',string)
articles_clean=''.join(token(articles))    #与上面写法的区别：不留空格
f=open('clean2.txt','w+')
f.write(articles_clean)
"""
file=open('/Users/han/PycharmProjects/NLP/opencc-python-reimplemented-0.1.5/clean2.txt')
content=file.read()
file.close()
articles=content
converted=re.sub('[a-zA-z0-9]','',articles)   #去除英文与数字
f=open('clean2star.txt','w+')
f.write(converted)