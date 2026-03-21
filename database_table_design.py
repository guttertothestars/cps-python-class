def create_table():
    sql_statement = "create table asset (asset_id integer, device_type text, assigned_user text, os_version text, status text)"
    pass


def drop_table():
    sql_statement = "drop table if exists assets"
    pass


def insert_row():
    sql_statement = "insert into asset values (?, ?, ?, ?, ?)"
    pass


def select_all():
    sql_statement = "select * from assets"
    pass


def update_row():
    sql_statement = "update asset set assigned_user = ? where asset_id = ?"
    pass


def delete_row():
    sql_statement = "delete from asset where asset_id = ?"
    pass


def display_menu():
    while True:
        print("\nMenu: ")
        print("Enter S to start new DB")
        print("Enter C to insert a new row")
        print("Enter R to retrieve all rows")
        print("Enter U to update an existing row")
        print("Enter D to delete and existing row")
        print("Enter F to load data from file")
        print("Enter Q to quit")
        choice = input("Enter your choice: ").upper()

        if choice == "S":
            drop_table()
            create_table()
        elif choice == "C":
            insert_row()
        elif choice == "R":
            select_all()
        elif choice == "U":
            update_row()
        elif choice == "D":
            delete_row()
        elif choice == "Q":
            break
        else:
            print("You have entered an invalid value. Try again.")


def main():
    pass


# TODO - fill in this later
