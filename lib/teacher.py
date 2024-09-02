#!/usr/bin/env python

from user import User
import random

class Teacher(User):
    knowledge = [
        "str is a data type in Python",
        "programming is hard, but it's worth it",
        "JavaScript async web request",
        "Python function call definition",
        "object-oriented teacher instance",
        "programming computers hacking learning terminal",
        "pipenv install pipenv shell",
        "pytest -x flag to fail fast",
    ]

    def __init__(self, first_name, last_name):
        # Call the parent class (User) constructor to initialize first_name and last_name
        super().__init__(first_name, last_name)
        # Initialize the knowledge attribute
        self.knowledge = Teacher.knowledge

    def teach(self):
        # Use random.randint to pick a random index from 0 to the length of the knowledge list minus 1
        random_index = random.randint(0, len(self.knowledge) - 1)
        # Return the knowledge at the random index
        return self.knowledge[random_index]
