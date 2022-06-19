class QuizBrain:
    def __init__(self, question_list) :
        self.question_number = 0
        self.question_list = question_list
        self.score=0

    def still_has_question(self):
        """Checks whether there are questions remaining for the loop to work!"""
        # if self.question_number< len(self.question_list):
        #     return True
        # else:
        #     return False    
        #We could have used the logic above, below is smaller alternative
        return self.question_number< len(self.question_list)


    def next_question(self):
        #retrive the item from current question number from the question_list
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)
        print(f"Your current score is {self.score}/{self.question_number}")    
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got the right answer!")
            self.score+=1
        else:
            print("You got the wrong answer!")
        print(f"The correct answer is {correct_answer}")    