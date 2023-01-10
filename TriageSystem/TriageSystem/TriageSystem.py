
## This application runs though a series of questions to determin if a person needs to see a GP

# inport the system from the opersting system.
from os import system, name;
# for use of a timer inport the sleep function
from time import sleep;


# clear the screen function this is made to clear the console depending on the os that is being used.
def cls():
    # if windows then use 
    #if(name == 'NT'):
        system("cls");


print("Welcome to the self triage COVID-19 application");
print("We will ask a few questions to determin weather you should see your GP.")
print("Are you happy to conintue? y/n:")

happy = input();
if (happy.capitalize() == 'Y' or happy.capitalize() == "YES"):
    cls();
    print("Do you have a regular cough? y/n:");
    cough = input();
    if (cough.capitalize() == 'Y' or cough.capitalize() == "YES"):
        cls();
        print("Please go see your GP.");
    elif (cough.capitalize() == 'N' or cough.capitalize() == "NO"):
        #procced to next question.
        cls();
        print("Do you have a high tempature?");
        highTemp = input();
        if(highTemp.capitalize == 'Y' or highTemp.capitalize == "YES"):
            cls();
            print("Please go see your GP.");
        elif(highTemp.capitalize == 'N' or highTemp.capitalize == "NO"):
            cls();
            print("You should be fine.")
        else: 
            cls();
            print("An incorrect option has been selected.");
    else:
        cls();
        print("An incorrect option has been selected.");
elif (happy.capitalize() == 'N' or happy.capitalize() == "NO"):
    print("okay, we will now close the window");
    sleep(2);
    system("exit");
else: 
    print("An incorrect option has been selected.");