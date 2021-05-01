from django.db import models
from datetime import date

class Tree(models.Model):
    number = models.CharField('number',max_length= 255,null=True,blank=True)
    name = models.CharField('name',max_length= 255,null=True,blank=True)
    temp = models.BooleanField(default=False)
    notes = models.TextField(null=True)
    question = models.CharField('question',max_length= 1024,null=True,blank=True)
    answer1 = models.CharField('answer1',max_length= 255,null=True,blank=True)
    answer2 = models.CharField('answer2',max_length= 255,null=True,blank=True)
    answer3 = models.CharField('answer3',max_length= 255,null=True,blank=True)
    answer4 = models.CharField('answer4',max_length= 255,null=True,blank=True)
    answer5 = models.CharField('answer5',max_length= 255,null=True,blank=True)
    result1 = models.CharField('result1',max_length= 255,null=True,blank=True)
    result2 = models.CharField('result2',max_length= 255,null=True,blank=True)
    result3 = models.CharField('result3',max_length= 255,null=True,blank=True)
    result4 = models.CharField('result4',max_length= 255,null=True,blank=True)
    result5 = models.CharField('result5',max_length= 255,null=True,blank=True)
    def __str__(self):
        return self.question

class Answer(models.Model):
    number = models.CharField('number',max_length= 255,null=True,blank=True)
    name = models.CharField('name',max_length= 2550,null=True,blank=True)
    temp = models.BooleanField(default=False)
    notes = models.TextField(null=True)
    q1 = models.CharField('q1',max_length= 255,null=True,blank=True)
    q2 = models.CharField('q2',max_length= 255,null=True,blank=True)
    q3 = models.CharField('q3',max_length= 255,null=True,blank=True)
    q4 = models.CharField('q4',max_length= 255,null=True,blank=True)
    q5 = models.CharField('q5',max_length= 255,null=True,blank=True)
    q6 = models.CharField('q6',max_length= 255,null=True,blank=True)
    q7 = models.CharField('q7',max_length= 255,null=True,blank=True)
    q8 = models.CharField('q8',max_length= 255,null=True,blank=True)
    q9 = models.CharField('q9',max_length= 255,null=True,blank=True)
    q10 = models.CharField('q10',max_length= 255,null=True,blank=True)
    outcome = models.CharField('outcome',max_length= 20,null=True,blank=True)
    date_arose = models.DateField(auto_now=False,null=True)
    date_identified = models.DateField(auto_now=False,null=True)
    nature = models.TextField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    why_reportable = models.TextField(null=True,blank=True)
    how_identified = models.TextField(null=True,blank=True)
    duration = models.TextField(null=True,blank=True)
    representative_details = models.TextField(null=True,blank=True)
    how_rectified = models.TextField(null=True,blank=True)
    remediation = models.TextField(null=True,blank=True)
    future_compliance = models.TextField(null=True,blank=True)
    reported = models.BooleanField(default=False)
    email_code = models.IntegerField(null=True)
    information = models.BooleanField(default=False)
    ho_review = models.BooleanField(default=False)
    ho_reg_affairs_review = models.BooleanField(default=False)
    quality = models.BooleanField(default=False)
    ho_reg_affairs_comments = models.TextField(null=True,blank=True)

    def __str__(self):
        if self.name is None:
            result = "Query " + str(self.pk) + ": No name given"
        else:
            result = "Query " + str(self.pk) + ": " + self.name
        return result
    def classified(self):
        return self.outcome == "Event" or self.outcome == "No event"
    def age(self):
        if self.date_identified == None:
            result = "Enter Date Identified"
        else:
            result = (date.today() - self.date_identified).days
        return result

    def next_step(self):
        if self.outcome != "Event" and self.outcome != "No event":  result = "1. Determine outcome"
        elif self.information == False:                             result = "2. Complete information"
        elif self.ho_review == False:                               result = "3. Head Of Review"
        elif self.ho_reg_affairs_review == False:                   result = "4. Head Of Reg Affairs Review"
        elif self.quality == False:                                 result = "5. Speak to HO Reg Affairs about commentary"
        else:                                                       result = "6. Submit to ASIC"
        return result

    def email_day(self):
        next_step_text = str(self.next_step())
        print(next_step_text)
        if self.age() == "Enter Data Identified":
            result = 0
        else:
            try:
                result = int((self.age() - 1) / 7) * 7 + 7
                if next_step_text[0] == '1': result = int((self.age() - 1) / 7) * 7 + 7
            except:
                result = 0
        return result

    def colour(self):
        # this needs to be fixed
        step = int(self.next_step()[0])
        trigger_day = (step) * 3
        limit_day = trigger_day + 3
        colour = "green"
        try:
            if self.age() > trigger_day: colour = "amber"
            if self.age() > limit_day: colour = "red"
        except:
            colour = "red"
        if self.reported():
            colour = "green"
        print(colour)
        return colour