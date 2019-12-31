import csv
from pprint import pprint

class ReadSent():

    def get_data(self):
        with open('sended_mails.csv', newline='\n', encoding='utf8') as file:
            reader = csv.reader(file)
            mails = list()
            for line in reader:
                mails.append(line[0])
            return mails

if __name__=='__main__':
    data = ReadSent().get_data()
    pprint(data)
    print(len(data))