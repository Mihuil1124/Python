import urllib.request
tab = input('Write URL - ')
page = urllib.request.urlopen(tab)
FuncRead = page.read()
text = FuncRead.decode("utf-8")
page.close()

f = open('Site.txt', 'w', encoding="utf-8")
f.writelines(text)
f.close()
