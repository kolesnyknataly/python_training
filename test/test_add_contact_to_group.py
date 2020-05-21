from model.contacts import Contacts
from fixture.orm import ORMFixture
from model.group import Group

import operator


def test_add_contact_to_group(app, db):
    if len(app.group.get_group_list()) == 0:
        app.group.create((Group(name="test", header="test2", footer="test3")))
    app.contacts.create((Contacts(first_name="test123", middle_name="test2", last_name="test3", nickname="test4",
                                  title="test5", company="test_company", address="trtrtrt", home="64645",
                                  mobile="75675", work="8787", fax="55657", email="testing@gna.yt",
                                  email_2="hgjgj2TR.UY", email_3="testin3g@gna.yt", homepage="rtete.com",
                                  b_year="1993", address_2="ytyt", phone2="phone2", notes="hghg")))
    contacts = app.contacts.get_contact_list()
    contact_for_group = contacts[len(contacts) - 1]
    group_id = app.contacts.get_random_group_for_add_contact()
    old_contacts_from_group = app.contacts.get_contact_list_from_group(group_id)
    app.contacts.add_contact_to_group_by_id(contact_for_group.id, group_id)
    new_contacts_from_group = app.contacts.get_contact_list_from_group(group_id)
    old_contacts_from_group.append(contact_for_group)
    assert sorted(old_contacts_from_group, key=Contacts.id_or_max) == sorted(new_contacts_from_group,

                                                                             key=Contacts.id_or_max)


def test_add_contact_to_group_db(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create((Group(name="test2", header="test2", footer="test3")))
    app.contacts.create((Contacts(first_name="firstName", middle_name="test2", last_name="test3", nickname="test4",
                                  title="test5", company="test_company", address="trtrtrt", home="64645",
                                  mobile="75675", work="8787", fax="55657", email="testing@gna.yt",
                                  email_2="hgjgj2TR.UY", email_3="testin3g@gna.yt", homepage="rtete.com",
                                  b_year="1993", address_2="ytyt", phone2="phone2", notes="hghg")))
    contacts = sorted(app.contacts.get_contact_list(), key=lambda x: x.id)
    contact_for_group = contacts[len(contacts) - 1]
    group_id = app.contacts.get_random_group_for_add_contact()
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    old_contacts_from_group = db.get_contacts_from_group(Group(id=group_id))
    app.contacts.add_contact_to_group_by_id(contact_for_group.id, group_id)
    new_contacts_from_group = db.get_contacts_from_group(Group(id=group_id))
    old_contacts_from_group.append(contact_for_group)
    assert sorted(old_contacts_from_group, key=Contacts.id_or_max) == sorted(new_contacts_from_group,
                                                                             key=Contacts.id_or_max)
