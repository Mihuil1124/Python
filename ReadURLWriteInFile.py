import urllib.request
tab = input('Write URL - ')
page = urllib.request.urlopen(tab)
FuncRead = page.read()
text = FuncRead.decode("utf8")
page.close()

f = open('Site.txt', 'w')
f.writelines(text)
f.close()
