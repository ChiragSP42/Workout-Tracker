import pandas as pd


class Exercise:
    def __init__(self, workout_name: str, date_started):
        self.workout_name = workout_name
        self.date_started = date_started

    def __str__(self):
        return f"Workout name: {self.workout_name}\nDate started: {self.date_started}"

    def add(self, date_recorded, reps: int, sets: int, weight: float):
        """
        Add date recorded, reps, sets and weights to a csv file TODO: Store values in a database

        :param date_recorded: datetime
        :param reps: int
        :param sets: int
        :param weight: float
        :return:
        """


w1 = Exercise("Bicep curl", "08/05/2024")
print(w1)
