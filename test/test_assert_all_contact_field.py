import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contacts.get_contact_list()[0]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_emails_on_home_page(app):
    contact_from_home_page = app.contacts.get_contact_list()[0]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_address_on_home_page(app):
    contact_from_home_page = app.contacts.get_contact_list()[0]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.address == contact_from_edit_page.address


def test_first_name_on_home_page(app):
    contact_from_home_page = app.contacts.get_contact_list()[0]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name


def test_last_name_on_home_page(app):
    contact_from_home_page = app.contacts.get_contact_list()[0]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contacts.get_contact_from_view_page(0)
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email_2, contact.email_3]))))
