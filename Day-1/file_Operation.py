file = open('newfile.txt', 'w')
file.write('I am created for the course. \n')
file.write('How about you? ')
file.write('How is your exam?')
file.close()

file = open('newfile.txt', 'r')
#print(file.read())
#print(file.read(10))
#print(file.readline())
print(file.readlines())
file.close()

file = open('newfile.txt', 'r')
for line in file :
    print(line)
file.close()