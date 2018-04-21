from gevent import monkey
from .psycogreen import patch_psycopg


def patch_all():
    monkey.patch_all()
    patch_psycopg()


patch_all()
