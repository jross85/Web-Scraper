from bs4 import BeautifulSoup 
import urllib2 
import re 

opener = urllib2.build_opener() 
opener.addheaders = [('User-agent', 'Mozilla/5.0')] 

url = ('http://en.wikipedia.org/wiki/List_of_American_comedy_films') 

ourUrl = opener.open(url).read() 

soup = BeautifulSoup(ourUrl) 

for link in soup.findAll('a', attrs={'href': re.compile("^/wiki/")}):  
	find = re.compile('/wiki/(.*?)"') 
	searchMovie = re.search(find, str(link)) 
	movie = searchMovie.group(1) 
	print movie 
	outfile = open('c:\users\justin\desktop\pythonstuff\learningpython\movies.txt', 'w')
	outfile.write(str(soup.find) + '\n') 