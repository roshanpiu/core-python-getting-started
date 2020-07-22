import sys
default_encoding = sys.getdefaultencoding()
print(default_encoding)

# Writing text to a file
# mode='wt' means write text mode='wb' mean write binary
f = open('wasteland.txt', mode='wt', encoding='utf-8')
f.write('What are the roots that clutch. ')
f.write('what branches grow\n')

# mode='rt' read text
g = open('wasteland.txt', mode='rt', encoding='utf-8')
print(g.readline())

g.close()