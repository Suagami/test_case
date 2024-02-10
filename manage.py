#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from time import sleep

MAX_RETRIES_NUM = 100

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_case.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    from django.db import connections
    conn = connections['default']
    no_host_available = True
    retry_count = 0
    sleep_time = 1

    while no_host_available:
        try:
            conn.connect()
        except Exception as err:

            if retry_count == MAX_RETRIES_NUM:
                sys.exit()
            print(f"Возникла ошибка: {err}. Пробуем переподключиться")
            sleep(sleep_time)
        else:
            no_host_available = False

        sleep_time *= 1.5
        retry_count += 1
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
