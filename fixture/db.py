import pymysql
from model.group import Group
from model.contacts import Contacts


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2 from addressbook "
                "where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, first_name, last_name, address, email, email_2, email_3, home, mobile, work, phone2) = row
                list.append(Contacts(id=str(id), first_name=first_name, last_name=last_name, address=address,
                                     email=email, email_2=email_2, email_3=email_3, home=home, mobile=mobile, work=work,
                                     phone2=phone2))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
