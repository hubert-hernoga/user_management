from django import template
from ..models import Group

register = template.Library()

@register.filter(name='user_in_group')
def user_in_group(name_group):
    group = Group.objects.get(name=name_group)
    users = group.users.all()

    return ", ".join([str(user) for user in users])

@register.filter(name='user_groups')
def user_groups(groups, user):
    groups_list = []
    for group in groups:
        if group.users.filter(pk=user.id):
            groups_list.append(group.name)
    return ", ".join([str(group) for group in groups_list])
