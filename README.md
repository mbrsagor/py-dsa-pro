#### Data structures & algorithms pro
Here, the repo is python data structures and algorithms pro and implement ``python3.8`` latest features.

# Setup
``git clone https://github.com/mbrsagor/py-dsa-pro/tree/master``

After that, create a virtualenv inside the project directory or somewhere else. Then activate the virtualenv and 
follow the code.

## Special features
- Sorting algorithms
    - Bubble sort
    - Selection sort
    - Insertion sort

- Searching algorithms
    - Linear search
    - Binary search
- Tree
- Queue
- Stack
- Fibonacci series
- Factorial
- OOP base algorithms


##### How to backup database using python script?
```python
import os
import time
import datetime

class DBBackup(object):
    def __init__(self):
        self.DB_HOST = input("Enter database hostname: ")
        self.DB_USER = input("Enter database username: ")
        self.DB_USER_PASSWORD = input("Enter database user password: ")
        self.DB_NAME = input("Enter backup database name: ")
        self.BACKUP_PATH = '/Users/macair/Desktop/backup/'

        # Getting current datetime to create seprate backup folder like "12012013-071334".
        self.DATETIME = time.strftime('%m%d%Y-%H%M%S')
        self.TODAYBACKUPPATH = self.BACKUP_PATH + self.DATETIME

    # Checking if backup folder already exists or not. If not exists will create it.
    def creating_backup_folder(self):
        print("creating backup folder")
        if not os.path.exists(self.TODAYBACKUPPATH):
            os.makedirs(self.TODAYBACKUPPATH)

    # Code for checking if you want to take single database backup or assinged multiple backups in DB_NAME.
    def checking_and_crate_db(self):
        if os.path.exists(self.DB_NAME):
            file1 = open(self.DB_NAME)
            multi = 1
            print("Databases file found...")
            print("Starting backup of all dbs listed in file " + self.DB_NAME)
        else:
            print("Starting backup of database " + self.DB_NAME)
            multi = 0

        # Starting actual database backup process.
        if multi:
            in_file = open(self.DB_NAME, "r")
            flength = len(in_file.readlines())
            in_file.close()
            p = 1
            dbfile = open(self.DB_NAME, "r")

            while p <= flength:
                db = dbfile.readline()  # reading database name from file
                db = db[:-1]  # deletes extra line
                dumpcmd = "mysqldump -u " + self.DB_USER + " -p" + self.DB_USER_PASSWORD + " " + db + " > " + \
                          self.TODAYBACKUPPATH + "/" + db + ".sql"
                os.system(dumpcmd)
                p = p + 1
            dbfile.close()
        else:
            db = self.DB_NAME
            dumpcmd = "mysqldump -u " + self.DB_USER + " -p" + self.DB_USER_PASSWORD + " " + db + " > " + self.TODAYBACKUPPATH + "/" + db + ".sql"
            os.system(dumpcmd)

        print("Backup script completed")
        print("Your backups has been created in '" + self.TODAYBACKUPPATH + "' directory")


if __name__ == "__main__":
    db_backup = DBBackup()
    db_backup.creating_backup_folder()
    db_backup.checking_and_crate_db()
```