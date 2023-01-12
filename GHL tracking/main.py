'''This Python program was designed to track my guided learning hours for the HyperionDev
Software Engineering bootcamp. It allows a user to input dates, times, and descriptions of
each session attended and prints the total guided learning hours currently tracked. The program
saves data entered during previous uses of the program in sessions.txt and reads this file
to the program at the beginning of each use so that previously tracked hours are included
in the total.'''

from datetime import *


class Session:
    def __init__(self, start_time, end_time, description):
        '''Session class represents each session attended and stores its respective data.
        start_time and end_time are datetime objects and should be the same date.
        end_time should be after start_time. The description is a string describing
        the session.'''
        self.start_time = start_time
        self.end_time = end_time
        self.description = description

    def length(self):
        '''Returns timedelta object representing the length of the session'''
        session_length = self.end_time - self.start_time
        return session_length

    def file_string(self):
        '''Returns a string to be written in sessions.txt'''
        session_string = f"{self.start_time.date()}&{self.start_time.time()}&{self.end_time.time()}&{self.description}\n"
        return session_string

    def print_info(self):
        print(f"{self.start_time.date()}, {self.start_time.time()}-{self.end_time.time()}")
        print(f"Description: {self.description}\n---")


# =========== Create working list from sessions.txt file ==============================
sessions_list = []
try:
    session_file = open("sessions.txt", "r")
    for line in session_file:
        line = line.split("&")
        line_date = date.fromisoformat(line[0])
        line_start_time = time.fromisoformat(line[1])
        line_start_time = datetime.combine(line_date, line_start_time)
        line_end_time = time.fromisoformat(line[2])
        line_end_time = datetime.combine(line_date, line_end_time)
        add_session = Session(line_start_time, line_end_time, line[3].strip())
        sessions_list.append(add_session)
    session_file.close()
except FileNotFoundError:
    session_file = open("sessions.txt", "x")
    session_file.close()


# ================== Define out of class methods ==========================
def print_list_info():
    '''Prints the total guided learning hours as calculated by summing the lengths of each
    session currently stored in the working list'''
    total_length = timedelta(0, 0)
    for session in sessions_list:
        total_length += session.length()
    print(f"\nCurrent total guided learning hours: {total_length.__str__()}")


def overwrite_file():
    '''Writes all sessions in the current working list over the current contents of sessions.txt'''
    session_file = open("sessions.txt", "w")
    for session in sessions_list:
        session_file.write(session.file_string())
    session_file.close()


# ==================== Main loop =============================================
'''Prints current total guided learning hours and asks user to enter the details of a new session.
If user enters exit at any time the program will end. Data saves to sessions.txt after entering the 
session description.'''
while True:
    print_list_info()
    print("Enter exit at anytime to exit the program (will not save current entry)")
    print("Enter print instead of date to see list of current entries")

    new_date = input("\nPlease enter the date of the learning hours as YYYY-MM-DD: ").strip().lower()
    if new_date == "exit":
        break
    if new_date == "print":
        [session.print_info() for session in sessions_list]
        continue
    # Check to make sure it is in proper format and change to proper format if possible
    if len(new_date) != 10:
        if new_date.find("-") == 2:
            new_date = "20" + new_date
        if not new_date[5:7].isdigit():
            new_date = new_date[:5] + "0" + new_date[5:]
        if len(new_date) < 10:
            new_date = new_date[:8] + "0" + new_date[8:]
    try:
        new_date = date.fromisoformat(new_date)
    except Exception:
        print("Bad input; please try again\n")
        continue

    new_start = input("Please enter start time as HH:MM (24-hr clock): ")
    if new_start == "exit":
        break
    try:
        new_start = time.fromisoformat(new_start)
        start_datetime = datetime.combine(new_date, new_start)
    except Exception:
        print("Bad input; please try again\n")
        continue

    input_end = input("Please enter end time as HH:MM (24-hr clock): ")
    if input_end == "exit":
        break
    input_end = input_end.strip().split(":")
    try:
        new_end = time(int(input_end[0]), int(input_end[1]))
        end_datetime = datetime.combine(new_date, new_end)
        if end_datetime < start_datetime:
            raise ValueError
    except Exception:
        print("Bad input; please try again\n")
        continue

    new_description = input(
        "Please enter a description (e.g. lecture, supplementary lecture, careers webinar, etc):\n").replace("&", "and")
    if new_description.strip().lower() == "exit":
        break

    new_session = Session(start_datetime, end_datetime, new_description)
    sessions_list.append(new_session)
    print("\nSaving new session to sessions.txt.\n")
    overwrite_file()

