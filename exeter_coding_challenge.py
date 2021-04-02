from collections import Counter
import pandas as pd
df=pd.read_csv(r"location of frech_dictionary.csv")
f1 = open('t8.shakespeare.txt', 'r')
f2 = open('t8.shakespeare.translated.txt', 'w')
checkWords=[]
repWords=[]
lines=f1.readlines()
list1=[]
list2=[]
def hello(data):
	frequencies = {}
	for item in data:
		if item in frequencies:
			frequencies[item] += 1
		else:
			frequencies[item] = 1
	return(frequencies)
for i in range(len(df)):
    a=df.iloc[i]
    checkWords.append(a[0])
    repWords.append(a[1])
for i in range(len(lines)):
    line=lines[i]
    for j in (line.split()):
        #print(j)
        if j in checkWords:
            #print(j)
            list2.append(j)
            for check, rep in zip(checkWords,repWords): 
                j=j.replace(check,rep)
            list1.append(j)
for i in range(len(lines)):
    line=lines[i]
    for check, rep in zip(checkWords,repWords):        
        line=line.replace(check,rep)
    f2.write(line)
data1=hello(list1)
data2=hello(list2)
df = pd.DataFrame(list(data1.items()),columns = ['French word','Frequency']) 
df1 = pd.DataFrame(list(data2.items()),columns = ['column1','column2']) 
list3=df1['column1']
df['English word'] = pd.Series(list3)
df = df.reindex(columns=['English word','French word','Frequency'])
df.to_csv('frequency.csv')
print(df)
f1.close()
f2.close()
