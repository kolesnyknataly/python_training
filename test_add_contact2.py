# -*- coding: utf-8 -*-
from contacts import Contacts
from application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contacts(first_name="Annaa", middle_name="Maria", last_name="Ivanova", nickname="marie", title="ree", company="test_company", address="trtrtrt", home="64645",
                            mobile="75675", work="8787", fax="55657", email="testing@gna.yt", email_2="hgjgj2TR.UY", homepage="rtete.com", b_year="1993", address_2="ytyt",
                            notes="hghg"))
    app.logout()

