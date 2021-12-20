class Game:
    noOfQuestions = 0
    def __init__ (self, noOfQuestions):
        self._noOfQuestions = noOfQuestions

    @property
    def noOfQuestions(self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            self._noOfQuestions = 1
            print('Minimum Number of Questions = 1 \nHence, number of questions will be set to 1')
        elif value > 10:
            self._noOfQuestions = 10
            print('Maximum Number of Questions = 10 \nHence, number of questions will be set to 10')
        else:
            self._noOfQuestions = value

class BinaryGame(Game):
    def generateQuestions(self):
        from random import randint
        score = 0
        for i in range(self.noOfQuestions):
            base10 = randint(1, 100)
            prompt = 'Переведите число %d в двоичную систему:' % (base10)
            userResult = input(prompt)

t1 = BinaryGame(2)

t1.generateQuestions()



