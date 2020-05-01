# -*- coding: utf-8 -*-
from model.contacts import Contacts
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testData = [
               Contacts(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="",
                        home="",
                        mobile="", work="", fax="", email="", email_2="", email_3="", homepage="", b_year="",
                        address_2="",
                        notes="", phone2="")] + [
               Contacts(first_name=random_string("first_name", 10), middle_name=random_string("middle_name", 20),
                        last_name=random_string("last_name", 20), nickname=random_string("nickname", 20),
                        title=random_string("title", 20),
                        company=random_string("company", 20), address=random_string("address", 20),
                        home=random_string("home", 20), mobile=random_string("mobile", 20),
                        work=random_string("work", 20), fax=random_string("fax", 20), email=random_string("email", 20),
                        email_2=random_string("email_2", 20), email_3=random_string("email_3", 20),
                        homepage=random_string("homepage", 20),
                        b_year=random_string("b_year", 20), address_2=random_string("address_2", 20),
                        notes=random_string("notes", 20),
                        phone2=random_string("phone2", 20))
               for i in range(5)
           ]


@pytest.mark.parametrize("contacts", testData, ids=[repr(x) for x in testData])
def test_add_contact(app, contacts):
    old_contacts = app.contacts.get_contact_list()
    app.contacts.create(contacts)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contacts)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)