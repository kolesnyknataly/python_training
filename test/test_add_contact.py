# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_add_contact(app):
    old_contacts = app.contacts.get_contact_list()
    contact = Contacts(first_name="Annaa", middle_name="Maria", last_name="Ivanova", nickname="marie", title="ree",
                       company="test_company", address="trtrtrt", home="64645",
                       mobile="75675", work="8787", fax="55657", email="testing@gna.yt", email_2="hgjgj2TR.UY",
                       email_3="testin3g@gna.yt", homepage="rtete.com", b_year="1993", address_2="ytyt", notes="hghg",
                       phone2="5635")
    app.contacts.create(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contact)
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)


"""def test_add_empty_contact(app):
    old_contacts = app.contacts.get_contact_list()
    contact = Contacts(first_name="", middle_name="", last_name="", nickname="", title="",
                       company="", address="", home="",
                       mobile="", work="", fax="", email="", email_2="",
                       homepage="", b_year="", address_2="",
                       notes="")
    app.contacts.create(contact)
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contact)
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)"""



