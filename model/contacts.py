from sys import maxsize


class Contacts:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None,
                 address=None, home=None, mobile=None, work=None, fax=None, email=None, email_2=None, email_3=None,
                 homepage=None, b_year=None, address_2=None, notes=None, id=None, phone2=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.b_year = b_year
        self.address_2 = address_2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
