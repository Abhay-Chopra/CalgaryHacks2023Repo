import sqlite3

connect = sqlite3.connect('events.db')
pointer = connect.cursor()

def db_initialize(pointer):
    # Creating DB table for the first time
    pointer.execute("""CREATE TABLE event (
            event_name text,
            event_desc text, 
            start_date int,
            end_date int,
            start_time int, 
            end_time int
            )""")
   
# For first time run, uncomment and run the db_initialize function 
# db_initialize(pointer=pointer)

# Ending the connection
connect.commit()
connect.close()

