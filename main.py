import os


if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Swastik")
    while True:
        x = input("Enter what you want me to say: ")
        if x == "q":
            os.system("say 'Bye bye my friend'")
            break
        command = f"say {x}"
        os.system(command)


