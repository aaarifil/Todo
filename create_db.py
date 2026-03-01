from core.db import create_db_and_tables
from models import models


def main():
    create_db_and_tables()
    print("Database tables created")


if __name__ == '__main__':
    main()
