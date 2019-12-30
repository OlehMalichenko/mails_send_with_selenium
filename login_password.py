import csv


class LoginPassword():

    def __init__(self, path_file):
        self.path_file = path_file

    def login_password(self):
        try:
            with open(self.path_file, 'r', newline='\n', encoding='utf8') as file:
                reader = csv.reader(file)
                reader_list = list(reader)
                result = {'login': reader_list[0][0],
                          'password': reader_list[0][1]
                         }
        except:
            return None
        else:
            return result