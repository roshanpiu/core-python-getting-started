# Data type for sequence of bytes
# Raw binary data
# Fixed with single byte encoding
# Files and network resources are transmitted as byte streams


byte1 = b'data'
byte1[0] 

string = "Test"

print(string.encode('utf8'))

print(string.encode('utf8').decode('utf8'))