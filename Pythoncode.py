import time
import os
pid = os.getpid()

time_start = time.perf_counter()

fin = open(r'C:\Users\ITAG\Downloads\TranslateWords Challenge\t8.shakespeare.txt')
fout = open(r'C:\Users\ITAG\Downloads\TranslateWords Challenge\french_dictionary.csv')
ft = open(r'C:\Users\ITAG\Downloads\TranslateWords Challenge\find_words.txt')

text1 = ""

data1 = fin.readlines()
data2 = fout.readlines()
data3 = ft.readlines()

text = "".join([i for i in data1])

l1,l2=[],[]

for i in data2:
    temp = i.split(",")
    l1.append(temp[0])
    if('\n' in temp[1]):
        l2.append(temp[1][:-1:])
    else:
        l2.append(temp[1])
        
text1 = text1 + ("English Word,French Word,Frequency\n")
        
for i,j in zip(data3,l2):
    k=text.count(i[:-1:] if "\n" in i else i)
    text1 = text1 + "{0},{1},{2}\n".format(i[:-1:] if "\n" in i else i,j,k)


for i,j in zip(l1,l2):
    text = text.replace(i,j)
fin.close()

fin = open('t8.shakespeare.translated.txt','w')
fout = open('frequency.csv','w')
fin.write(text)
fout.write(text1)
fin.close()
fout.close()
  

time = (time.perf_counter() - time_start)

gin = open('parformance.txt','w')

text3 = ""

text3 = text3 + ("Time to process: 0 minutes %5.1f seconds\nMemory used : %5.1f MB"%(time,pid/1024.0))

gin.write(text3)
gin.close()
