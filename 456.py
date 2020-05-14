c=[None]
d=c*997
def none(n):
    if not d[n-1]:
        d[n-1] = none(n-1)+none(n-2) if (n > 0) else 1
    return d[n-1]
print(none(995))
print(d)
print(none(995)/none(994))
