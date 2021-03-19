def find_substr(s1, s2):
    if s1.find(s2) == -1:
        print("No")
    else:
        print("yes")

find_substr('watermelon', 'water')
find_substr('water', 'wt')
find_substr('foo', 'foo-foo')
find_substr('foo', 'foofoo')

def in_substr(s1,s2):
    if s2 in s1:
        print("yes")
    else:
        print("No")

in_substr('watermelon', 'water')
in_substr('water', 'wt')
in_substr('foo', 'foo-foo')
in_substr('foo', 'foofoo')


def re_substr(s1,s2):
    from re import search

    if search(s2,s1):
        print("yes")
    else:
        print("No")

re_substr('watermelon', 'water')
re_substr('water', 'wt')
re_substr('foo', 'foo-foo')
re_substr('foo', 'foofoo')