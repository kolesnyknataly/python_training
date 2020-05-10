# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_add_contact(app, db, json_contacts):
    contacts = json_contacts
    old_contacts = db.get_contact_list()
    app.contacts.create(contacts)
    new_contacts = db.get_contact_list()
    old_contacts.append(contacts)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)