from model.group import Group
import random


def test_edit_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create((Group(name="test", header="test2", footer="test3")))
    old_groups = db.get_group_list()
    index = random.randrange(len(old_groups))
    group = old_groups[index]
    changed_group = Group(name="change_name", header="change_header", footer="change_footer", id=group.id)
    app.group.edit_group_by_id(changed_group.id, changed_group)
    new_groups = db.get_group_list()
    old_groups[index] = changed_group
    assert len(old_groups) == app.group.count()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)