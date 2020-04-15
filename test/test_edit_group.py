from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create((Group(name="test", header="test2", footer="test3")))
    old_groups = app.group.get_group_list()
    group = Group(name="change_name", header="change_header", footer="change_footer")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
