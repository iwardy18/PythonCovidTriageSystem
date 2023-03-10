## This application runs though a series of questions to determin 
## if a person needs to see a GP

# import utilities
from Utilities import cls, close, splash, countDown;


#start the splash screen
splash();

#start the program.
print("Welcome to the self triage COVID-19 application!");
print("\n");
print("We will ask a few questions to determin if you should see your GP.");
print("\n");

happy = input("Are you happy to continue? y/n: ");
if (happy.capitalize() == 'Y' or happy.capitalize() == "YES"):
  #question1:  
    cls();
    name = input("What is your name? ");
    cls();
    cough = input("Hi " + name + ", Do you have a regular cough? y/n: ");
    if (cough.capitalize() == 'Y' or cough.capitalize() == "YES"):
        cls();
        print("Please go see your GP.");
    elif (cough.capitalize() == 'N' or cough.capitalize() == "NO"):
        #procced to next question.
        cls();
        highTemp = input(name + ", Do you have a high temperature? y/n: ");
        if(highTemp.capitalize() == 'Y' or highTemp.capitalize() == "YES"):
            cls();
            print("Please go see your GP.");
        elif(highTemp.capitalize() == 'N' or highTemp.capitalize() == "NO"):
            cls();
            print("You should be fine.")
        else: 
            cls();
            print("An incorrect option has been selected.");
    else:
        cls();
        print("An incorrect option has been selected.");
        
elif (happy.capitalize() == 'N' or happy.capitalize() == "NO"):
  cls();
  close();
else: 
    print("An incorrect option has been selected.");

    