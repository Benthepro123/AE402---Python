# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 19:45:40 2020

@author: edric
"""

class Human():
    def __init__(self, height ,weight, iq):
        self.height = height
        self.weight = weight
        self.iq = iq
        
    def learn(self,time):
        self.time = time
        if self.time <= 20:
            self.iq = "Preschool"
        elif self.time >= 20 and self.time <=30:
            self.iq = "Kindergarten"
        elif self.time >= 30 and self.time <=40:
            self.iq = "Elementary School"
        elif self.time >= 40 and self.time <=50:
            self.iq = "Middle School"
        elif self.time >= 50 and self.time <=60:
            self.iq = "High School"
        elif self.time >= 70 and self.time <=100:
            self.iq = "University"
        elif self.time >= 100 and self.time <=120:
            self.iq = "Master Dergree"
        elif self.time >= 120 and self.time <=210:
            self.iq = "P.H.D."
        else:
            self.iq = "Superhuman"
        return self.iq
Ben = Human(129,26,"none")
print(Ben.learn(60))
