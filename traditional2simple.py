from opencc import OpenCC
cc=OpenCC('t2s')  #cc1=OpenCC('t2s')
file_object=open('/Users/han/PycharmProjects/NLP/opencc-python-reimplemented-0.1.5/wiki_00')
file_content=file_object.read()
file_object.close()
to_convert=file_content
converted=cc.convert(to_convert)
f=open('w0.txt','w+')
f.write(converted)

