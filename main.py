import sqlite3

intro = """
      ,----..            ,----,          .---. 
     /   /   \         ,/   .`|         /. ./|
    /   .     :      ,`   .'  :     .--'.  ' ;
   .   /   ;.  \   ;    ;     /    /__./ \ : |
  .   ;   /  ` ; .'___,/    ,' .--'.  '   \' .
  ;   |  ; \ ; | |    :     | /___/ \ |    ' ' 
  |   :  | ; | ' ;    |.';  ; ;   \  \;      : 
  .   |  ' ' ' : `----'  |  |  \   ;  `      |
  '   ;  \; /  |     '   :  ;   .   \    .\  ; 
   \   \  ',  /      |   |  '    \   \   ' \ |
    ;   :    /       '   :  |     :   '  |--"  
     \   \ .'        ;   |.'       \   \ ;     
  www. `---` ver     '---' he       '---" ire.org 

Welcome to the OTW wargames database. Please make sure that your details.db file is in the same directory as this runnable.
Enter a command below. Enter 'help' for information about available commands.
"""

help = """
The following commands are available:
    addwargame -- This will add space for a new wargame to the database.
    addpassword -- This will add a password for a given challenge.
    addsolution -- This will add a description for a given challenge.
    getdetails -- This can be used to retrieve the password and the solution for a challenge.
    exit -- Close the application.
    help -- Display this menu
"""
conn = sqlite3.connect('details.db').cursor()

def main():
    conn = sqlite3.connect('details.db')
    running = True        
    print intro
    
    while(running):
        userIn = raw_input('DDB: ')
        if userIn == "addwargame":
            addWargame()
        elif userIn == "addpassword":
            addPassword()
        elif userIn == "addsolution":
            addSolution()
        elif userIn == "getdetails":
            getDetails()
        elif userIn == "help":
            print help
        elif userIn == "exit":
            running = False;
        else:
            print("Invalid command. Please try again.")
    conn.close()


def addWargame():
    name = (raw_input('Please enter the name of the wargame: '),)
    conn.execute("CREATE TABLE %s (ID INTEGER PRIMARY KEY AUTOINCREMENT, PASSWORD TEXT, SOLUTION TEXT)" % name)
    print(name[0] + ' created succesfully!');
    return
    

def addPassword():
    wg = str(raw_input('Which wargame? '))
    ch = str(raw_input('Which challenge? '))
    pw = str(raw_input('Password: '))

    conn.execute("INSERT INTO "+wg+" VALUES (NULL, '"+pw+"', NULL)") #TODO
    return

def addSolution():
    print("adding sol")

def getDetails():
    print("getting details")

 

if __name__ == "__main__":
    main()
