#!/usr/bin/env python
# coding: utf-8

from experta import *
import questionary


# ## Creating utilities for CLI using questionary

def binary_question(prompt:str, choices = ['Sí', 'No']) -> bool:
    question = questionary.select(
        prompt,
        choices=choices).ask()
    
    return question


# ### Reading Question from 'questions.txt'

with open('questions.txt', 'r', encoding='utf-8') as file:
    questions = file.readlines()
    questions = [question.strip() for question in questions]


# #### Create Question Class

class Question(Fact):
    """
    Fact given from binary question at a given step.
    
    Parameters
    ----------
    number: L(int) | int
        Current step in the flow chart
    answer: L(str) | str
        Answer given by user
    """
    
    number = Field(int, default = 0)
    answer = Field(str, default = "no")
    


# ### Knoladge Engine

class MedicalDiagnosis(KnowledgeEngine):
    
    @DefFacts()
    def _initial_action(self):
        """
        Defines the Initial Fact as "Diagnose".

        Parameters
        ----------
        self : DiagnosisLaptop
            The instance of the KnowledgeEngine.

        Yields
        -------
        Fact
            Yields the initial fact with action set to "Diagnose"
        """
        yield Fact(action="Diagnose")

    # Questions
    @Rule(NOT(Question(number=L(0))))
    def question0(self):
        answer: str = binary_question(questions[0])
        self.declare(Question(number=0, answer=answer))
        
    
    @Rule(NOT(Question(number = L(1))), Question(number=L(0), answer=L('Sí')))
    def question1(self):
        answer: str = binary_question(questions[1])
        self.declare(Question(number=1, answer=answer))
        
    
    
    @Rule(NOT(Question(number = L(2))), 
              Question(number=L(0), answer=L('Sí')), 
              Question(number = L(1), answer = L('Sí')))
    def question2(self):
        answer: str = binary_question(questions[2])
        self.declare(Question(number=2, answer=answer))
    
    
    @Rule(NOT(Question(number = L(3))),
          OR(
              Question(number = L(0), answer = L('No')),
              Question(number = L(1), answer = L('No'))
          ))
    def question3(self):
        answer: str = binary_question(questions[3])
        self.declare(Question(number=3, answer=answer))
        
    
    @Rule(NOT(Question(number = L(4))),
            Question(number = L(3), answer = L('No')))
    def question4(self):
        answer: str = binary_question(questions[4])
        self.declare(Question(number=4, answer=answer))
        
    @Rule(NOT(Question(number = L(5))),
    Question(number = L(4), answer = L('Sí'))
    )
    def question5(self):
        answer: str = binary_question(questions[5])
        self.declare(Question(number=5, answer=answer))
        

    @Rule(NOT(Question(number = L(6))),
    Question(number = L(4), answer = L('No'))
    )
    def question6(self):
        answer: str = binary_question(questions[6])
        self.declare(Question(number=6, answer=answer))
        
    @Rule(NOT(Question(number = L(7))),
              Question(number = L(6), answer = L('Sí'))
    )
    def question7(self):
        answer: str = binary_question(questions[7])
        self.declare(Question(number=7, answer=answer))
        
    
    @Rule(NOT(Question(number = L(8))),
              Question(number = L(6), answer = L('No'))
    )
    def question8(self):
        answer: str = binary_question(questions[8])
        self.declare(Question(number=8, answer=answer))
        
    
    @Rule(NOT(Question(number = L(9))),
              Question(number = L(8), answer = L('Sí'))
    )
    def question9(self):
        answer: str = binary_question(questions[9])
        self.declare(Question(number=9, answer=answer))
        
    @Rule(NOT(Question(number = L(10))),
              Question(number = L(9), answer = L('No'))
    )
    def question10(self):
        answer: str = binary_question(questions[10])
        self.declare(Question(number=10, answer=answer))
        
    
    @Rule(NOT(Question(number = L(11))),
              Question(number = L(10), answer = L('No'))
    )
    def question11(self):
        answer: str = binary_question(questions[11])
        self.declare(Question(number=11, answer=answer))
        
    @Rule(NOT(Question(number = L(12))),
              Question(number = L(8), answer = L('No'))
    )
    def question12(self):
        answer: str = binary_question(questions[12])
        self.declare(Question(number=12, answer=answer))
        
        
    @Rule(NOT(Question(number = L(13))),
              Question(number = L(12), answer = L('No'))
    )
    def question13(self):
        answer: str = binary_question(questions[13])
        self.declare(Question(number=13, answer=answer))
        
        


engine = MedicalDiagnosis()
engine.reset()
engine.run()




