import psycopg2
from gevent.socket import wait_read, wait_write
from psycopg2 import extensions


def patch_psycopg():
    extensions.set_wait_callback(_psycopg_gevent_wait)


def _psycopg_gevent_wait(conn, timeout=None):
    while True:
        state = conn.poll()
        if state == extensions.POLL_OK:
            break
        elif state == extensions.POLL_READ:
            wait_read(conn.fileno(), timeout=timeout)
        elif state == extensions.POLL_WRITE:
            wait_write(conn.fileno(), timeout=timeout)
        else:
            raise psycopg2.OperationalError("Bad result from poll: %r" % state)
