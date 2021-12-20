def printInstructions(instruction):
     print(instruction)

def getUserScore(userName):
     try:
          f = open('userScores.txt', 'r')
          for line in f:
               content = line.split(', ')
               if content[0] == userName:
                    return content[1]
                    f.close
          f.close()
          return '-1'
     except IOError:
          f = open('userScores.txt', 'w')
          f.close()
          return '-1'

from os import remove, rename

def updateUserScore(newUser, userName, score):
     if newUser == True:
          f = open('userScores.txt', 'a')
          f.write('\n' + userName + ', ' + str(score))
          f.close()
     else:
          f_t = open('userScores.tmp', 'w')
          f = open('userScores.txt', 'r')
          for line in f:
               content = line.split(', ')
               if content[0] == userName:
                    f_t.write(content[0] + ', ' + str(score) + '\n')
               else:
                    f_t.write(content[0] + ', ' + content[1])
          f.close()
          f_t.close()
          remove('userScores.txt')
          rename('userScores.tmp', 'userScores.txt')


updateUserScore(False, 'Benny', 158)
# updateUserScore(True, 'Oleg', 100)

# Oleg, 50
# Sasha, 100


