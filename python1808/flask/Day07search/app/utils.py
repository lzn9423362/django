from flask import g


def login_log():
    print(g.username)


def login_ip_log():
    pass