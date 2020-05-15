import re
from model.contacts import Contacts


def test_assert_all_contact_field(app, db):
    contact_from_home_page = app.contacts.get_contact_list()
    contact_from_db = db.get_contact_list()
    assert sorted(contact_from_home_page, key=Contacts.id_or_max) == sorted(contact_from_db, key=Contacts.id_or_max)


def clear(s):
    return re.sub("[() -]", "", s)

"""
def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email_2, contact.email_3])))"""
