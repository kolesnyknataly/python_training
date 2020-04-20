import time
from model.contacts import Contacts
from random import randrange


def test_delete_some_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create((Contacts(first_name="test", middle_name="test2", last_name="test3", nickname="test4",
                                      title="test5", company="test_company", address="trtrtrt", home="64645", mobile="75675",
                                      work="8787", fax="55657", email="testing@gna.yt", email_2="hgjgj2TR.UY",
                                      homepage="rtete.com", b_year="1993", address_2="ytyt", notes="hghg")))
    old_contacts = app.contacts.get_contact_list()
    index = randrange(len(old_contacts))
    app.contacts.delete_contact_by_index(index)
    time.sleep(1)
    assert len(old_contacts) - 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

