#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from blog.settings import base


def main():
    """Run administrative tasks."""

    settings = 'blog.settings.local' if base.DEBUG else 'blog.settings.produccion'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
