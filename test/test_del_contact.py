import time
from model.contacts import Contacts
import random


def test_delete_some_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contacts.create((Contacts(first_name="test", middle_name="test2", last_name="test3", nickname="test4",
                                      title="test5", company="test_company", address="trtrtrt", home="64645", mobile="75675",
                                      work="8787", fax="55657", email="testing@gna.yt", email_2="hgjgj2TR.UY",
                                      homepage="rtete.com", b_year="1993", address_2="ytyt", notes="hghg")))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contacts.delete_contact_by_id(contact.id)
    time.sleep(1)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == app.contacts.count()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts

