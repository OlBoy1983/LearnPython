inputFile = open ('C:\\Docs\\QA\\Python\\myimage.png', 'rb')
outputFile = open ('myoutputimage.jpg', 'wb')

msg = inputFile.read(10)
while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10)
inputFile.close()
outputFile.close()