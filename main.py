import urllib

link = "https://en.wikipedia.org/wiki/Main_Page"
f = urllib.urlopen(link)
data = f.read()
print data
