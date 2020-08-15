import os  # os module is imported

print("Menu")
print("Press 1 to open Notepad")
print("Press 2 to open Chrome")
print("Press 3 to open media player")
print("\nEnter your choice(1-3) :")

choice = input()

if(choice == str(1)):

	os.system("notepad")

elif(choice == str(2)):

	os.system("chrome")

elif(choice == str(3)):

	os.system("wmplayer")

# the above mentioned are windows programs.
# the path must be set for the above programs.
