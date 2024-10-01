class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for starting, ending in self.calendar:
            if starting < end and ending > start:
                return False
        self.calendar.append((start, end))
        return True