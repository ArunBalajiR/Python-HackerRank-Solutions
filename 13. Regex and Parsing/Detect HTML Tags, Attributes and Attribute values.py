# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print('-> '+str(i[0])+' > '+str(i[1]))
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print('-> '+str(i[0])+' > '+str(i[1]))

html=''''''
for _ in range(int(input())):
    html+=input().rstrip()
    html+='\n'
p=parser()
p.feed(html)
