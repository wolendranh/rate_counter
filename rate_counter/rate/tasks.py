# -*- encoding: utf-8 -*-
import requests
import logging
import re
from bs4 import BeautifulSoup

from celery.task import periodic_task
from .models import Institute, StudentGroup, Subject


@periodic_task(run_every=60*60)  # periodicity of execution in seconds (1 hour)
def parse_data():

    get_institutes()
    get_logger().info('Completed institutes collection')
    get_groups()
    get_logger().info('Completed groups collection')
    get_subjects()
    get_logger().info('Completed subjects collection')
    get_logger().info('DB is up-to-date')


def get_institutes():

    soup = set_bs(get_url())

    # in source code of NULP site's schedule page all names and IDs of institutes and groups are located in <option> tag
    # list of all of the institutes is present on any schedule page,
    # list of groups is present in page, URL of which contain ID of related institute

    # Filling database with Institute objects
    for option in soup.find_all('option'):
        if len(option.text) == 4:
            inst_obj, created = Institute.objects.get_or_create(name=option.text, site_id=option.get('value'))
            message(inst_obj, created)


def get_groups():

    for inst_obj in Institute.objects.all():
        get_logger().info(u"Processing Institute {}".format(inst_obj.name))
        soup = set_bs(get_url(str(inst_obj.site_id)))

        for option in soup.find_all('option'):
            if re.match(ur'.+-.+', option.text):
                grp_obj, created = StudentGroup.objects.get_or_create(name=option.text,
                                                                      site_id=option.get('value'),
                                                                      institute=inst_obj)
                message(grp_obj, created)


def get_subjects():
    sem = 1
    sem_part = 1
    for grp_obj in StudentGroup.objects.all():
        get_logger().info(u"Processing Group {0} of {1} Institute".format(grp_obj.name, grp_obj.institute.name))
        soup = set_bs(get_url(grp_obj.institute.site_id, grp_obj.site_id, str(sem), str(sem_part)))

        # all information about subject (name, lecturer) located in div object with such class
        subjects = soup.find_all('div', {'class': 'vidst'})

        for subject in subjects:
            # getting first component of div object (directly the name)
            sub_obj, created = Subject.objects.get_or_create(name=subject.contents[0].text, group=grp_obj)
            message(sub_obj, created)


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger


def message(obj, created):
    """
    Creating a message if new object is added
    """
    if created:
        get_logger().info(u"Adding {}".format(obj.name))


def set_bs(url):
    """
    setting up a BeautifulSoup
    """
    r = requests.get(url)
    return BeautifulSoup(r.content, "html.parser")


def get_url(inst='1', group='', semestr='1', semestr_part='1'):
    """
    Forming URL of page for parsing data
    """
    return 'http://old.lp.edu.ua/node/40?inst={0}&group={1}&semestr={2}&semest_part={3}'.format(inst,
                                                                                                group,
                                                                                                semestr,
                                                                                                semestr_part,
                                                                                                )
