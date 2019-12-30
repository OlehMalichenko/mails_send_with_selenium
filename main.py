from time import sleep
from path_key import PathKey
from start_driver import StartDriver
from read_csv import ReadCsv
from write_csv import WriteCsv
from pprint import pprint
from datetime import datetime


def main():

    # driver after SignIn at mailbox page
    driver_in_box = driver_after_signin()
    if driver_in_box is None:
        return

    # get all data from csv
    data = ReadCsv().get_data()
    if data is None:
        driver_in_box.close()
        return

    # iterate over data
    for dic in data:
        work_with_one_mail(dic, driver_in_box)

    driver_in_box.close()

def driver_after_signin():
    # driver after SignIn at mailbox page
    driver_start = StartDriver()
    driver_in_box = driver_start.go()
    if driver_in_box is None:
        return None
    sleep(10)
    return driver_in_box

def work_with_one_mail(dic: dict, driver_in_box):
    try:
        email = dic['email']
        name = dic['name']
        admin = dic['admin']
        site = dic['site']
    except:
        return

    path = PathKey(email, name, admin, site)

    # open a new-mail window
    path_key = path.newmail()
    driver_new_mail = new_mail(driver_in_box, path_key)
    if driver_new_mail is None:
        return
    sleep(3)

    # fill address to form
    path_key = path.address()
    mail_active(driver_new_mail, path_key)
    sleep(1)

    # fill title to form
    path_key = path.title()
    mail_active(driver_new_mail, path_key)
    sleep(1)

    # fill mail-body
    path_key = path.body()
    mail_active(driver_new_mail, path_key)
    sleep(1)

    # send mail
    path_key = path.send_mail()
    mail_active(driver_new_mail, path_key)
    sleep(2)

    # write sended mails
    w = WriteCsv(email, name, datetime.now()).write()



def new_mail(driver, path_key, try_num=1):
    path = path_key[0]
    key = path_key[1]
    try:
        driver.find_element_by_xpath(path).send_keys(key)
    except:
        print('No find element New mail button')
        if try_num > 10:
            return None
        try_num = try_num + 1
        sleep(3)
        new_mail(driver, path_key, try_num)
    else:
        return driver


def mail_active(driver, path_key, try_num=1):
    path = path_key[0]
    key = path_key[1]
    try:
        driver.find_element_by_xpath(path).send_keys(key)
    except:
        print('Not found:  ' + path)
        if try_num > 10:
            return
        try_num = try_num + 1
        sleep(3)
        mail_active(driver, path_key, try_num)


if __name__=='__main__':
    main()
