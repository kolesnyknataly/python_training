from model.contacts import Contacts
from random import randrange


def test_edit_some_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contacts.create((Contacts(first_name="test", middle_name="test2", last_name="test3", nickname="test4",
                                      title="test5", company="test_company", address="trtrtrt", home="64645",
                                      mobile="75675", work="8787", fax="55657", email="testing@gna.yt",
                                      email_2="hgjgj2TR.UY", email_3="testin3g@gna.yt",  homepage="rtete.com",
                                      b_year="1993", address_2="ytyt", phone2="phone2", notes="hghg")))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = old_contacts[index]
    changed_contact = Contacts(first_name="change_first_name", middle_name="change.middle_name", last_name="change.last_name",
                       nickname="change.nickname", title="change.title", company="test_company",
                       address="changeaddress", home="changehome", mobile="changemobile", work="changework",
                       fax="changefax", email="change.email", email_2="change.email_2", email_3="changetestin3g@gna.yt",
                       homepage="change.homepage", b_year="1993", address_2="change.address_2", phone2="changephone2",
                       notes="changenotes", id=contact.id)
    app.contacts.edit_contact_by_id(changed_contact.id, changed_contact)
    assert len(old_contacts) == app.contacts.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = changed_contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
