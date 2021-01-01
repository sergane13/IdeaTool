from django.db import models


class Idea(models.Model):

    title = models.CharField(max_length=30)

    # Describe the idea in 20-25 words
    optimism_1 = models.CharField(max_length=75, null=True, blank=True)

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

    optimism_1_grade = models.CharField(max_length=1, null=True, blank=True, choices=GRADES)

    # How did you come up with the idea
    optimism_2 = models.TextField(null=True, blank=True)

    # How do you imagine the idea
    optimism_3 = models.TextField(null=True, blank=True)

    # What problem do you wanna solve
    neutralism_1 = models.TextField(null=True, blank=True)
    neutralism_1_grade = models.CharField(max_length=1, null=True, blank=True, choices=GRADES)

    # Who has this problem

    # Description of person
    neutralism_2 = models.TextField(null=True, blank=True)

    # Estimated number of people
    neutralism_2_number = models.IntegerField(null=True, blank=True)

    # Moments when this problem occur
    neutralism_2_moments = models.TextField(null=True, blank=True)

    # Times per day when problem occur
    neutralism_2_times = models.IntegerField(null=True, blank=True)
    neutralism_2_grade = models.CharField(max_length=1, null=True, blank=True, choices=GRADES)

    # Importance of the problem
    neutralism_3 = models.TextField(null=True, blank=True)
    neutralism_3_grade = models.CharField(max_length=1, null=True, blank=True, choices=GRADES)

    # Team capability to do the project
    neutralism_4_team = models.TextField(null=True, blank=True)

    # What is wrong with the idea
    pessimism_1 = models.TextField(null=True, blank=True)
    pessimism_1_grade = models.CharField(max_length=1, null=True, blank=True, choices=GRADES)

    # What are the reasons for this idea to fail
    pessimism_2 = models.TextField(null=True, blank=True)
    pessimism_2_grade = models.CharField(max_length=1, null=True, blank=True, choices=GRADES)

    # A competition analysis independent page to be continued...

    objects = models.Manager()
