# inport the system from the opersting system.
from os import system, name;
# for use of a timer import the sleep function
from time import sleep;
# import webbrowser to open a specific page
import webbrowser as webbrowser;

def openPage(url):
  webbrowser.open(url, new = 2);

# clear the screen function this is made to clear the console depending on the os that is being used.  
def cls():
  
  if(name == "nt"): # if windows then use cls
        system("cls");
  elif(name == "posix"): #if replicat use clear --same as unix/linux
         system("clear");

#used to close the console    
def close():
    print("okay, we will now close the window");
    #sleep(10);
    countDown(10);
    if(name == "nt"): # if windows then use cls
      system("exit");
    elif(name == "posix"): #if replicat use exit --same as unix/linux      
      system("exit 0");

def splash():
  nhsLogo = """,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,@@@@(,,,,,,@@@@@,,,,@@,,,,@@@@@%,,,,@@*,,,,,,,,,,@@,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,@@@@,,,,,,,%@@@*,,,/@,,,,,@@@@@,,,,%@,,,,&@@@@@@@@@,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,@@@*,,,#,,,,@@@,,,,@@,,,,@@@@@(,,,,@@,,,,,,@@@@@@@@,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,@@@,,,,@@,,,,@*,,,#@,,,,,,,,,,,,,,%@@@@,,,,,,,,@@@@,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,@@*,,,#@@@,,,*,,,,@@,,,,@@@@@(,,,,@@@@@@@@@,,,,*@@@,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,@@,,,,@@@@*,,,,,,&@,,,,*@@@@@,,,,@@,,,,,,,,,,,,@@@@,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,@,,,,%@@@@@,,,,,,@@,,,,@@@@@*,,,,@@*,,,,,,,*@@@@@@@,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,***************************************************,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,@@(,,,,,@@@,,,@@@,*@@,,,/@%,@@*,#@%,,(@@/,,,,*@@@@*,,@@,,%@#,,,,,,,,,
,,,,,,,,,,@@,,,,,,/@@,,,,,@@*,#@&,,@@,,@@*,#@%,,,,@@,****,,@@*,,@@#,@@@,,,,,,,,,
,,,,,,,,,,@@@,,,,,,@@,,,,,@@,,,@@/@@,,,@@*,#@%,,,@@@,,,,,,,@@*,,,,,,%@#,,,,,,,,,
,,,,,,,,,,,,,@@@@@,,,@@@@@,,,,,,@@@,,,,@@*,#@@@@@*,,,,,,,,,@@*,,#@@@@,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""";
  print(nhsLogo);
  #sleep(10);
  print("Loading..")
  countDown(10);
  #loadingPercent();
  cls();

def countDown(secs):
  while(secs > 0):
    print(secs);
    sleep(1);
    secs = secs -1;
    print ("\033[A                             \033[A"); # source stackoverflow https://stackoverflow.com/questions/44565704/how-to-clear-only-last-one-line-in-python-output-console

def loadingPercent():
  print("test ");
  for i in range(1,100):
   print("\r", end="");
   print(i);
   sleep(1);
    