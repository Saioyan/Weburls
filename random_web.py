import random
import sys,os
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
num = file_path.rfind('/')
fun = file_path[0:num]+'/function.txt'
out = file_path[0:num]+'/output.txt'
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False
inum = input('輸入欲抽取數量:')
if is_number(inum) == True:
    print('Check input is number')
else:
    print('Check input not number')
    sys.exit()
h = int(inum)
with open(file_path,"r",encoding="utf-8") as fp:
    strr = fp.read()
strr = strr.split("\n")
with open(fun,"r",encoding="utf-8") as fp:
    strr2 = fp.read()
lenurl = len(strr)
if h > lenurl :
    print('抽取數量大於庫存')
    sys.exit()
dic1={}
for i in range(0,lenurl):
    dic1.setdefault(i,strr[i])
lenurl2 = lenurl
li2=[]
for i in range(0,h) :
    c = int(random.uniform(0, lenurl2))
    li2.append(strr[c])
    strr.remove(strr[c])
    lenurl2 = len(strr)
n=1
body=''
head = '    insert(c);'+'\n'+'function insert(c){'+'\n'+'    if (c==0){'+'\n'+'document.getElementById("iframe").src="https://zi.media/@kk665403pixnetnetblog/post/XIBcLv";'+'\n'+'}'+'\n'
tail = '}'+'\n'+'</script>'+'\n'+'</body>'+'\n'+'</html>'
for i in li2 :
    body += '    else if(c=='+str(n)+'){'+'\n'+'document.getElementById("iframe").src="'+str(i)+'";'+'\n'+'}'+'\n'
    n+=1
body += '\n'+ '}'+'\n'
s = 'c=getRandom(0,'+str(len(li2))+');'
strr2 += '\n'+s+'\n'
total = strr2 + head + body + tail
print(total)
fg = open(out, "w", encoding="utf-8")
fg.write(total)
