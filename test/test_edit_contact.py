from model.contacts import Contacts


def test_edit_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create((Contacts(first_name="test", middle_name="test2", last_name="test3", nickname="test4",
                                      title="test5", company="test_company", address="trtrtrt", home="64645",
                                      mobile="75675", work="8787", fax="55657", email="testing@gna.yt",
                                      email_2="hgjgj2TR.UY", homepage="rtete.com", b_year="1993", address_2="ytyt",
                                      notes="hghg")))
    old_contacts = app.contacts.get_contact_list()
    contact = Contacts(first_name="change_first_name", middle_name="change.middle_name", last_name="change.last_name",
                       nickname="change.nickname", title="change.title", company="test_company",
                       address="change.address", home="change.home", mobile="change.mobile", work="change.work",
                       fax="change.fax", email="change.email", email_2="change.email_2", homepage="change.homepage",
                       b_year="1993", address_2="change.address_2", notes="change.notes")
    contact.id = old_contacts[0].id
    app.contacts.edit_first_contact()
    assert len(old_contacts) == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
