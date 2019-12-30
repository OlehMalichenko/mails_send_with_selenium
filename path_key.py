from selenium.webdriver.common.keys import Keys
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.formatted_text import FormattedText

class PathKey(object):

    def __init__(self, email='', name='', admin='', site=''):
        self.email = email
        self.name = name
        self.admin = admin
        self.site = site

    def send_mail(self):
        return ['//*[@class="T-I J-J5-Ji aoO v7 T-I-atl L3"]', Keys.RETURN]

    def body(self):
        return ['//div[@aria-label="Тело письма"]', 'Hello, \n{0}\n\nHappy New Year!\n'
                                                    'I wish you, in particular, and the '
                                                    '"{1}" team further prosperity\n\n'
                                                    'Stay cool. Move forward!\n'
                                                    '({2})\n'
                                                    .format(self.admin, self.name, self.site)]

    def title(self):
        return ['//input[@aria-label="Тема"]', 'For "{}" team'.format(self.name)]

    def address(self):
        return ['//textarea[@aria-label="Кому"]', self.email]

    def newmail(self):
        return ['//*[text ()="Написать"]', Keys.RETURN]

    def login(self):
        return '//input[@id="identifierId"]'

    def password(self):
        return '//input[@name="password"]'


if __name__=='__main__':
    obj = PathKey('advokat1141@gmail.com', 'OM-company', 'Oleh Malichenko', 'om@good.com')
    print(obj.body())