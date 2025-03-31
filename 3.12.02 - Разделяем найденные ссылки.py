import re

urls = re.findall(r'https?://\S+', input())

prot = r'(?<!\S)https?(?=://)'
dom = r'(?<=://)[a-z\.]+?(?=\/)'
param = r'\?[a-zA-Z0-9_=&]+?(?=#)'
yako = r'#[a-z]+'


for url in urls:
    print(url)
    print