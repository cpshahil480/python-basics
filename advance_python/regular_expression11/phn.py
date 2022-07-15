import re

rule = '[+][9][1]\d{10}'
f=open('phone.txt', 'r')
for i in f:
    data=i.rstrip("\n")
    matcher=re.fullmatch(rule,data)
    if matcher is not None:
        print(data)