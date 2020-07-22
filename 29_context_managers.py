# with-block - control flow structure for managing resources 
# with blocks can be used with any object that supports context manager protocol

with open('wasteland.txt', mode='wt', encoding='utf-8') as f:
  f.write('What are the roots that clutch. ')
  f.write('what branches grow\n')