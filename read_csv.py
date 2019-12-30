import csv
from pprint import pprint


class ReadCsv():

    def get_data(self):
        data = self._read_from_csv()
        return data


    def _read_from_csv(self):
        try:
            with open('dou_data.csv', newline='\n', encoding='utf8') as file:
                reader = csv.reader(file)
                result = list()
                for line in reader:
                    dic = {
                        'name' : line[0],
                        'email' : line[6],
                        'admin' : self._clear_data_admin(line[9]),
                        'site' : line[3]
                    }
                    if dic['email'] is not '' and dic['admin'] is not '':
                        result.append(dic)
                    else:
                        continue

                return result
        except:
            return None


    def _clear_data_admin(self, s: str):
        if s is '[]':
            return []

        s = s.replace('[[\'', '')
        s = s.replace('\']]', '')
        s = s.replace('\'', '')
        l = s.split('], [')

        res = list()

        for l_1 in l:
            l_2 = l_1.split(', ')
            if len(l_2) == 2:
                res.append(l_2[1])

        names = self._create_names(res)

        return names


    def _create_names(self, res: list):
        if len(res) == 0:
            return ''
        elif len(res) == 1:
            return res[0]
        elif len(res) == 2:
            return ' and '.join(res)
        else:
            last = res[-1]
            res = res[:-1]
            names = ', '.join(res) + ' and ' + last
            return names


if __name__=='__main__':
    obj = ReadCsv()
    data = obj.get_data()

