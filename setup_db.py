import sqlalchemy

def connect(user, password, db, host='localhost', port=5433):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

con, meta = connect('gaopeng', 'viewchat', 'chatbot')


from sqlalchemy import Table, Column, Integer, String, ForeignKey

QuestionAnswer = Table('questionanswer', meta,
    Column('question', String, primary_key=True),
    Column('answer', String)
)




# Create the above tables
meta.create_all(con)

from qa import QAs
con.execute(meta.tables['questionanswer'].insert(), QAs)


def answer(question):
    res=[]
    clause = QuestionAnswer.select().where(QuestionAnswer.c.question == question)
    for row in con.execute(clause):
        res.append(row['answer'])
    return res


def questionsTo(answer):
    res=[]
    clause = QuestionAnswer.select().where(QuestionAnswer.c.answer == answer)
    for row in con.execute(clause):
        res.append(row['question'])
    return res

def addQA(questionStr, answerStr):
    clause = QuestionAnswer.insert().values(question=questionStr, answer=answerStr)
    con.execute(clause)

def clearTables():
    con.execute(QuestionAnswer.delete())








