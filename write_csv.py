import csv

class WriteCsv():

    def __init__(self, email, name, time):
        self.email = email
        self.name = name
        self.time = time

    def write(self):
        with open('sended_mails', 'a', newline='\n', encoding='utf8') as file:
            writer = csv.writer(file)
            writer.writerow([self.email, self.name, self.time])