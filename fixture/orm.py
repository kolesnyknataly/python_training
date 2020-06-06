from datetime import datetime
from pony.orm import *
from model.group import Group
from model.contacts import Contacts


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups",
                       lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        first_name = Optional(str, column='firstname')
        last_name = Optional(str, column='lastname')
        address = Optional(str, column='address')
        home = Optional(str, column='home')
        mobile = Optional(str, column='mobile')
        work = Optional(str, column='work')
        phone2 = Optional(str, column='phone2')
        email = Optional(str, column='email')
        email_2 = Optional(str, column='email2')
        email_3 = Optional(str, column='email3')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts",
                     lazy=True)

    def __init__(self, host, name, user, password):
        try:
            self.db.bind('mysql', host=host, database=name, user=user, password=password)
            self.db.generate_mapping()
            sql_debug(True)
        except BindingError:
            pass

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)

        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contacts):
            return Contacts(id=str(contacts.id), first_name=contacts.first_name, last_name=contacts.last_name,
                            address=contacts.address, home=contacts.home, mobile=contacts.mobile, work=contacts.work,
                            phone2=contacts.phone2, email=contacts.email, email_2=contacts.email_2,
                            email_3=contacts.email_3)

        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_from_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))
