# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

zero = '0'
one = '1'
two = '2'
three = '3'
four = '4'
five = '5'
six = '6'
seven = '7'
eight = '8'
nine = '9'
ten = '10'

GRADES = [
    (zero, '0'),
    (one, '1'),
    (two, '2'),
    (three, '3'),
    (four, '4'),
    (five, '5'),
    (six, '6'),
    (seven, '7'),
    (eight, '8'),
    (nine, '9'),
    (ten, '10'),
]


class Idea(models.Model):

    title= models.CharField(max_length=30, null=True, blank=True)

    @property
    def class_name(self):
        try:
            return "".join(self.title.split())
        except:
            return self.title

    # Describe the idea in 20-25 words
    optimism_1 = models.CharField(max_length=75, null=True, blank=True)

    optimism_1_grade = models.CharField(max_length=2, null=True, default='0', blank=True, choices=GRADES)

    # How did you come up with the idea
    optimism_2 = models.TextField(null=True, blank=True)

    # How do you imagine the idea
    optimism_3 = models.TextField(null=True, blank=True)

    # What problem do you wanna solve
    neutralism_1 = models.TextField(null=True, blank=True)
    neutralism_1_grade = models.CharField(max_length=2, null=True, default='0', blank=True, choices=GRADES)

    # Who has this problem

    # Description of person
    neutralism_2 = models.TextField(null=True, blank=True)

    # Estimated number of people
    neutralism_2_number = models.IntegerField(null=True, blank=True, default=0)

    # Moments when this problem occur
    neutralism_2_moments = models.TextField(null=True, blank=True)

    # Times per day when problem occur
    neutralism_2_times = models.IntegerField(null=True, blank=True,  default=0)
    neutralism_2_grade = models.CharField(max_length=2, null=True, default='0', blank=True, choices=GRADES)

    # Importance of the problem
    neutralism_3 = models.TextField(null=True, blank=True)
    neutralism_3_grade = models.CharField(max_length=2, null=True, default='0', blank=True, choices=GRADES)

    # Team capability to do the project
    neutralism_4_team = models.TextField(null=True, blank=True)

    # What is wrong with the idea
    pessimism_1 = models.TextField(null=True, blank=True)
    pessimism_1_grade = models.CharField(max_length=2, null=True, default='0', blank=True, choices=GRADES)

    # What are the reasons for this idea to fail
    pessimism_2 = models.TextField(null=True, blank=True)
    pessimism_2_grade = models.CharField(max_length=2, null=True, default=0, blank=True, choices=GRADES)

    @property
    def grade_one(self):
        try:
            return int(self.optimism_1_grade) * 10
        except:
            return 0

    @property
    def grade_two(self):
        try:
            return ((int(self.neutralism_1_grade) + int(self.neutralism_2_grade) + int(self.neutralism_3_grade))/3) * 10
        except:
            return 0

    @property
    def grade_three(self):
        try:
            return ((int(self.pessimism_1_grade) + int(self.pessimism_2_grade))/2) * 10
        except:
            return 0

    @property
    def completion_rate(self):
        try:
            o1 = 0 if self.optimism_1 == '' else 1
            o2 = 0 if self.optimism_2 == '' else 1
            o3 = 0 if self.optimism_3 == '' else 1
            n1 = 0 if self.neutralism_1 == '' else 1
            n2 = 0 if self.neutralism_2 == '' else 1
            n2n = 0 if self.neutralism_2_number == 0 else 1
            n2m = 0 if self.neutralism_2_moments == '' else 1
            n2t = 0 if self.neutralism_2_times == 0 else 1
            n3 = 0 if self.neutralism_3 == '' else 1
            n4 = 0 if self.neutralism_4_team == '' else 1
            p1 = 0 if self.pessimism_1 == '' else 1
            p2 = 0 if self.pessimism_2 == '' else 1

            return round((o1 + o2 + o3 + n1 + n2 + n2n + n2m + n2t + n3 + n4 + p1 + p2) * 8.33)
        except:
            return 0

    objects = models.Manager()


class Opinions(models.Model):

    name = models.CharField(max_length=20, null=True, blank=True)

    opinion = models.TextField(null=True, blank=True)

    idea_opinion = models.ForeignKey(
        Idea,
        on_delete=models.CASCADE,
    )

    objects = models.Manager()