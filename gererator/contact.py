from model.group import Group
from model.contacts import Contacts
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
               for i in range(n)
           ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testData))
