import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 12857763
    API_HASH = "7b71e8bca0d5e1c6d8383ae818d9ec8d"
    BOT_TOKEN = "6375262996:AAFZBXDHSjs6Yn5M_1CbV_XS-tWQqG_wYX4"
    DATABASE_URL = "postgres://kprfogjs:z1cQQkrgTItmMGBVBbNQIJ3HWhY8kFRT@arjuna.db.elephantsql.com/kprfogjs"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "SiArab_Store"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]

       #✗ Pᴏᴡᴇʀᴇᴅ Bʏ: Navya Op!
