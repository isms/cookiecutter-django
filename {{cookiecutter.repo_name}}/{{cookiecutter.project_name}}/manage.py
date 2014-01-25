#!/usr/bin/env python
import os
import sys
import dotenv

if __name__ == "__main__":
    dotenv.read_dotenv(os.path.abspath('../.env'))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Local")

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)