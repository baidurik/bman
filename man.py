import argparse
import re
import requests
parser = argparse.ArgumentParser()
parser.add_argument('command', metavar='command', type=str)

args = parser.parse_args()
url = 'https://www.opennet.ru/man.shtml?topic='
text = requests.get(url + args.command).text
match = re.search('<PRE>.*</PRE>', text, flags=(re.DOTALL))
if match == None:
    print('This command was not found in opennet database')
    exit()
out = '\n'.join(re.split('\n+', ''.join(re.split('&.*?;', ''.join(re.split('<.*?>', match[0]))))))
l = 0 
r = out.find('\n')
while r != -1 and r >= l:
    print(out[l:r])
    l = r + 1
    r = out[l:].find('\n') + l
    s = input()
    if s == 'q':
        break
