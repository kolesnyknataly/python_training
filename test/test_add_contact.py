# -*- coding: utf-8 -*-
from model.contacts import Contacts
import time


def test_add_contact(app):
    app.contacts.create(
        Contacts(first_name="Annaa", middle_name="Maria", last_name="Ivanova", nickname="marie", title="ree",
                 company="test_company", address="trtrtrt", home="64645",
                 mobile="75675", work="8787", fax="55657", email="testing@gna.yt", email_2="hgjgj2TR.UY",
                 homepage="rtete.com", b_year="1993", address_2="ytyt",
                 notes="hghg"))


def test_add_empty_contact(app):
    app.contacts.create(
        Contacts(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="", home="", mobile="", work="", fax="", email="", email_2="",homepage="", b_year="", address_2="", notes=""))
