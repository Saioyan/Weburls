fun = 'D:\\urldb\\function.txt'
out = 'D:\\urldb\\output.txt'
with open("D:\\urldb\\jf.txt","r",encoding="utf-8") as fp:
    stc=fp.read()
with open(fun,"r",encoding="utf-8") as fp:
    strr=fp.read()
number = stc.count('https')
li = []
for i in range(number):
    num = stc.find('https')
    stc = stc[num:]
    num2 = stc.find('"')
    url = stc[:num2]
    li.append(url)
    stc = stc[num2:]
for i in li:
    if 'zi.media' not in i:
        li.remove(i)
lenurl = len(li)

n=1
body=''
head = '    insert(c);'+'\n'+'function insert(c){'+'\n'+'    if (c==0){'+'\n'+'document.getElementById("iframe").src="https://zi.media/@kk665403pixnetnetblog/post/XIBcLv";'+'\n'+'}'+'\n'
tail = '}'+'\n'+'</script>'+'\n'+'</body>'+'\n'+'</html>'
for i in li :
    body += '    else if(c=='+str(n)+'){'+'\n'+'document.getElementById("iframe").src="'+str(i)+'";'+'\n'+'}'+'\n'
    n+=1

s = 'c=getRandom(0,'+str(len(li))+');'
strr += '\n'+s+'\n'
total = strr + head + body + tail
print(total)
fg = open(out, "w", encoding="utf-8")
fg.write(total)
