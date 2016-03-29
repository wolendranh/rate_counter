# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from celery.task import task
from .models import Institute, StudentGroup, Subject
import requests
from bs4 import BeautifulSoup
import re


@task
def get_institutes_id():

    url = 'http://www.lp.edu.ua/node/40?inst=1&&semestr=1&semest_part=1'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # я подивився структуру сторінки розкладу і виявив, що всі назви і значення інститутів і груп
    # завжди містяться між тегами <option>. Але також там містяться значення поточного семестру і його половини,
    # тобто, весняний(0), осінній(1), перша(1) і друга(2).
    # Список всіх інститутів міститься на будь-якій сторінці розкладу,
    # а список груп, тільки на сторінці де вказаний інститут до якого вони належать.


    # Заповнення бази даних інститутами
    for option in soup.find_all('option'):
        if len(option.text) == 4:
            print option.text
            if not Institute.objects.filter(name=option.text).exists():
                obj = Institute()
                obj.name = option.text
                obj.site_id = option.get('value')
                obj.save()
    print 'done with insts'
    get_group_id()
    get_subject_list()


def get_group_id():

    # В цій функції я формую URL залежно від ID інституту і заповнюю базу даних групами
    for inst_obj in Institute.objects.all():
        print 'processing', inst_obj.name
        url = 'http://www.lp.edu.ua/node/40?inst=' + \
              str(inst_obj.site_id) + \
              '&group=semestr=1&semest_part=1'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        for option in soup.find_all('option'):
            if re.match(ur'.+-.+', option.text):
                print option.text
                if not StudentGroup.objects.filter(name=option.text).exists():
                    grp_obj = StudentGroup()
                    grp_obj.name = option.text
                    grp_obj.site_id = option.get('value')
                    grp_obj.institute = inst_obj
                    grp_obj.save()
    print 'done with group'


def get_subject_list():
    sem = 1
    sem_part = 1
    for grp_obj in StudentGroup.objects.all():
        print 'processing ' + grp_obj.institute.name + ' ' + grp_obj.name
        url = 'http://www.lp.edu.ua/node/40' \
              '?inst=' + grp_obj.institute.site_id + \
              '&group=' + grp_obj.site_id + \
              '&semestr='+str(sem) + \
              '&semest_part='+str(sem_part)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        # вся інформація про предмет (назва, викладач) міститься в цій div з таким класом.
        subjects = soup.find_all('div', {'class': 'vidst'})
        group_subjects = []
        for subject in subjects:
            # тут витягую тільки текст першого компонента в заданому div (безпосередньо назву предмету)
            subject_name = subject.contents[0].text
            if subject_name not in group_subjects:
                group_subjects.append(subject_name)
        for subj in group_subjects:
            print subj
            sub_obj = Subject()
            sub_obj.name = subj
            sub_obj.group = grp_obj
            sub_obj.save()
