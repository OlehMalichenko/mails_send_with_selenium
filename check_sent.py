import csv

class ReadSent():

    def get_data(self):
        with open('sended_mails.csv', newline='\n', encoding='utf8') as file:
            reader = csv.reader(file)
            mails = list()
            for line in reader:
                mails.append(line[0])
            return mails


class CheckSent():

    def __init__(self, mails: list):
        self.mails = mails

    def check(self, mail):
        if mail in self.mails:
            return False
        else:
            return True