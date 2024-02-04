from controller.chat_session import start_chat_session
from view.ascii_art import print_header, print_headerTower

def main():
    print_headerTower()
    print_header()
    start_chat_session()

if __name__ == "__main__":
    main()