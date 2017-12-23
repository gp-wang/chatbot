
import re
class Chatbot:

    def __init__(self, qa_list):
        self.qa_list=[(question.lower(), answer.lower()) for question,answer in qa_list]


    def answer(self, user_question):
        user_question=user_question.lower().strip()
        max=0
        potential_ans=None
        potential_question=None
        for question, answer in self.qa_list:

            if question == user_question:
                return answer
            score = self.similarity(user_question, question)

            if score > self.getThres() and score > max:
                max=score
                potential_ans = answer
                potential_question=question

        print("highest score: " + str(max) + ", question: \n" + potential_question)
        return potential_ans




    def similarity(self, strA, strB):
        score = 0
        setB = set([x.strip() for x in re.split(r'[;,.?\s]\s*', strB)])

        listA = [x.strip() for x in re.split(r'[;,.?\s]\s*', strA)]

        for wd in listA:
            if wd in setB:
                score +=1

        return score


    def start(self):

        while True:
            user_question = None

            while user_question == None:
                try:
                    user_question = str(input("Enter your question: ")).strip()
                except:
                    return

            ans=self.answer(user_question)
            if ans:
                print(ans)
            else:
                print('Null')

    def getThres(self):
        return 0

from fuzzywuzzy import fuzz
class FuzzyChatBot(Chatbot):
    def similarity(self, strA, strB):
        return fuzz.ratio(strA, strB)
    def getThres(self):
        return 50



from qa import  QAs
list1=[(qa['question'], qa['answer']) for qa in QAs]
list2=[("what is the price?", "$5"), ("hello", "hi")]


botOne = Chatbot(list1)
botTwo = Chatbot(list2)
botThree = FuzzyChatBot(list2)
botFour = FuzzyChatBot(list1)






