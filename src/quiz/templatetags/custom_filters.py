from django import template

register = template.Library()


# filter
def negative(value):        # -5
    return -value


# filter
def multi(value, arg):
    return value * arg


# filter
def dived(value, arg):
    return value // arg


def arr(value, arg):
    return (arg / (value + arg)) * 100


def results(value, arg):
    if value - arg < 0:
        return 0
    else:
        return value - arg


register.filter('negative', negative)
register.filter('multi', multi)
register.filter('dived', dived)
register.filter('arr', arr)
register.filter('results', results)
