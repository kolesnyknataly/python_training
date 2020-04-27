from model.contacts import Contacts
from random import randrange


def test_edit_some_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create((Contacts(first_name="test", middle_name="test2", last_name="test3", nickname="test4",
                                      title="test5", company="test_company", address="trtrtrt", home="64645",
                                      mobile="75675", work="8787", fax="55657", email="testing@gna.yt",
                                      email_2="hgjgj2TR.UY", homepage="rtete.com", b_year="1993", address_2="ytyt",
                                      phone2="phone2", notes="hghg")))
    old_contacts = app.contacts.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contacts(first_name="change_first_name", middle_name="change.middle_name", last_name="change.last_name",
                       nickname="change.nickname", title="change.title", company="test_company",
                       address="changeaddress", home="changehome", mobile="changemobile", work="changework",
                       fax="changefax", email="change.email", email_2="change.email_2", homepage="change.homepage",
                       b_year="1993", address_2="change.address_2", phone2="changephone2", notes="changenotes")
    contact.id = old_contacts[index].id
    app.contacts.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
