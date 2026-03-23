import sqlite3


# User input and validation functions
def ask_for(data_type, prompt, low, high):
    while True:
        try:
            x = data_type(input(prompt))
            if x < low or x > high:
                print(f"Must print a value between {low} and {high}")
            else:
                return x
        except ValueError:
            print("Invalid value, try again")


# valid values not being used, but could be to check for specific strings
def ask_for_str(prompt, valid_values):
    if valid_values is not None:
        lower_valid_values = {value.lower() for value in valid_values}
    while True:
        x = input(prompt)
        if valid_values is None:
            break
        if x.lower() in lower_valid_values:
            break
        else:
            print("You must enter one of the following", valid_values)
    return x


def create_table(db_conn):
    sql_statement = "CREATE TABLE assets (asset_id integer, device_type text, assigned_user text, os_version text, status text)"
    db_conn.execute(sql_statement)
    print("\nTable created.")


def drop_table(db_conn):
    sql_statement = "DROP TABLE IF EXISTS assets"
    db_conn.execute(sql_statement)
    print("\nTable dropped.")


def insert_row(db_conn):
    sql_statement = "INSERT INTO assets VALUES (?, ?, ?, ?, ?)"

    # ask for table data
    asset_id = ask_for(int, "Enter the asset ID", 0, 1000)
    device_type = input("Enter the device type: ")
    assigned_user = input("Enter the assigned user: ")
    os_version = input("Enter the OS version: ")
    status = input("Enter the asset status: ")

    # build the tuple needed to be passed in to database.execute()
    tuple_of_values = (asset_id, device_type, assigned_user, os_version, status)

    db_conn.execute(sql_statement, tuple_of_values)
    # after execute, have to commit
    db_conn.commit()
    print("\nrow inserted.")


def select_all(db_conn):
    sql_statement = "SELECT * FROM assets"
    result_set = db_conn.execute(sql_statement)
    print("Print the type of the results set is ", type(result_set))

    for row in result_set:
        print(row)


def update_row(db_conn):
    # determine which row gets updated based on asset id (primary key)
    asset_id = ask_for(int, "Enter the asset ID for the row to be updated: ", 0, 1000)

    # determine if whole row or single field to be updated
    update_whole_row = ask_for(
        int, "Press 1 to update whole row, 2 to update single field: ", 1, 2
    )
    if update_whole_row == 1:
        device_type = input("Enter the device type: ")
        assigned_user = input("Enter the assigned user: ")
        os_version = input("Enter the OS version: ")
        status = input("Enter the asset status: ")

        sql_statement = """UPDATE assets SET
            device_type = ?, 
            assigned_user = ?, 
            os_version = ?, 
            status = ? 
            WHERE asset_id = ?"""

        # build the tuple needed to be passed in to database.execute()
        tuple_of_values = (device_type, assigned_user, os_version, status, asset_id)
        db_conn.execute(sql_statement, (tuple_of_values))
    elif update_whole_row == 2:
        # dict of column names to validate against.
        valid_choices = {
            1: "device_type",
            2: "assigned_user",
            3: "os_version",
            4: "status",
        }

        menu_prompt = """
        Select a field to update:
        1: Device Type
        2: Assigned User
        3: OS Version
        4: Status
        > """

        choice_num = ask_for(int, menu_prompt, 1, 4)
        column_name = valid_choices[choice_num]

        # determine update value - fstring literals in sql has some apparent serious risks if not careful
        new_value = input(f"Enter the new value for {column_name}: ")

        sql_statement = f"UPDATE assets SET {column_name} = ? WHERE asset_id = ?"
        db_conn.execute(
            sql_statement, (new_value, asset_id)
        )  # SET comes first, then WHERE

    # provide reassurance and commit
    db_conn.commit()
    print(f"\nAsset {asset_id} updated successfully.")


def delete_row(db_conn):
    sql_statement = "DELETE FROM assets WHERE asset_id = ?"
    asset_id = ask_for(int, "Enter the asset ID for the row to be deleted: ", 0, 1000)

    db_conn.execute(sql_statement, (asset_id,))
    db_conn.commit()
    print(f"\nRow deleted for {asset_id}.")


def load_from_file(db_conn):
    # Open a CSV file-could import csv module, but this is easier
    file_ptr = open("assets.csv", "r")
    headers = file_ptr.readline()  # reads in as a string

    # read in each row from CSV
    for line in file_ptr:
        print(line)

    # insert all rows into DB


def display_menu(db_conn):
    while True:
        print("""\nMenu: 
        Enter C to insert a new row
        Enter R to retrieve all rows
        Enter U to update an existing row
        Enter D to delete an existing row
        Enter F to load data from file
        Enter Q to quit
        Enter S to start new DB""")
        choice = input("Enter your choice: ").upper()

        if choice == "S":
            drop_table(db_conn)
            create_table(db_conn)
        elif choice == "C":
            insert_row(db_conn)
        elif choice == "R":
            select_all(db_conn)
        elif choice == "U":
            update_row(db_conn)
        elif choice == "D":
            delete_row(db_conn)
        elif choice == "F":
            load_from_file(db_conn)
        elif choice == "Q":
            print("Thanks for DB connecting today. \nGoodbye")
            break
        else:
            print("You have entered an invalid value. Try again.")


def main():
    # setup steps
    # establish a connection to the DB
    db_conn = sqlite3.connect("assets.db")

    display_menu(db_conn)
    # close the DB connection when finished
    db_conn.close()


main()

# to create a tuple w/one value tuple_of_one_value = (val, )
# Note the comma. It is necessary
