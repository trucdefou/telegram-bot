import os

ADD_TO_LIST = 1
DELETE_FROM_LIST = 2
ADD_TO_REMINDER = 3
DELETE_FROM_REMINDER = 4
GET_DATE = 5
GET_TEXT = 6


def get_allowed_users():
    ALLOWED_USERS = []
    if os.environ.get('ALLOWED_USERS', None) is not None:
        ALLOWED_USERS = os.environ['ALLOWED_USERS'].split(",")
    return ALLOWED_USERS
def get_add_to_list():
    return ADD_TO_LIST

def get_delete_from_list():
    
    return DELETE_FROM_LIST

def get_add_to_reminder():
    return ADD_TO_REMINDER

def get_date_for_reminder():
    return GET_DATE

def get_text_for_reminder():
    return GET_TEXT