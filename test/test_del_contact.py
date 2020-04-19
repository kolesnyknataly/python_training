import time
from model.contacts import Contacts


def test_delete_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create((Contacts(first_name="test", middle_name="test2", last_name="test3", nickname="test4",
                                      title="test5", company="test_company", address="trtrtrt", home="64645", mobile="75675",
                                      work="8787", fax="55657", email="testing@gna.yt", email_2="hgjgj2TR.UY",
                                      homepage="rtete.com", b_year="1993", address_2="ytyt", notes="hghg")))
    old_contacts = app.contacts.get_contact_list()
    app.contacts.delete_first_contact()
    time.sleep(1)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

