# -*- coding: utf-8 -*-
from model.group import Group
import time


def test_add_group(app):
    app.group.create(Group(name="wr", header="dgdf", footer="dfgdg"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
