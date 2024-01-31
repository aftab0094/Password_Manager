import random
import secrets
import string
import time
from useful_func import countdown, clear_screen
import os
from password import Password


def write_master_key():
    if os.path.isfile('master_key.txt'):
        pass
    else:
        create_file = open('master_key.txt', 'w')
        create_file.close()
    master_key_file = open('master_key.txt', 'r+')
    method = master_key_file.read
    mk_check = method()
    if mk_check == '':
        master_key_file.seek(0)
        master_key = password_ultimate(30) + password_normal() + password_ultimate(30)
        master_key_file.write(master_key)
        print(f'Your master key is (you will need this after, so save it somewhere else, you have 2 minutes): "{master_key}"')
        try:    
            countdown(120)
            clear_screen()
        except KeyboardInterrupt:
            master_key_file.close()
            os.remove('master_key.txt')
            clear_screen()
    else:
        pass
    master_key_file.close()

def password_normal():
    words = ['haha', 'wow', 'amazing', 'rabbit', 'lion', 'lala', 'done', 'one', 'hello', 'world', 'python', 'java', 'csharp', 'javascript']

    Password.random_numbers = str(random.randint(1000, 10000))
    Password.random_words = ''.join(random.choices(words, k=2, weights=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]))
    final_password = (Password.random_numbers + Password.random_words)
    return final_password

def password_ultimate(lenth_of_pass):
    password = []
    password.extend(string.punctuation)
    password.extend(string.ascii_letters)
    password.extend(string.digits)
    password = ''.join(random.choices(password, k=lenth_of_pass))
    return password

def save_pass(platform, password):
    saved_pass_file = open('saved_passwords.txt', 'a')
    saved_pass_file.write(f"{platform}:{password}\n")
    saved_pass_file.close()

def user_input():
    def pass_gen_menu():
        choose_option = input(" 1. Generate normal strenth password\n 2. Generate Ultimate strenth password\n 3. Go back to the main menu\n Choose a option: ")
        if choose_option.isdigit:
            if choose_option == '1':
                platform = input("Enter the platform name that you are gonna use the password for Security: ")
                password = password_normal()
                print(f'your Generated Password is: {password}')
                save_pass(platform=platform, password=password)
                countdown(30)
                clear_screen()
                main_menu()
            if choose_option == '2':
                platform = input("Enter the platform name that you are gonna use the password for Security: ")
                MAX_LEN = 30
                MIN_LEN = 8
                while True:
                    try:
                        password_lenth = int(input('Enter the lenth that your password should be: '))
                        if password_lenth <= MAX_LEN and password_lenth >= MIN_LEN:
                            break
                        elif password_lenth > MAX_LEN:
                            print("Password lenth cannot exceed the lenth of 30")
                            time.sleep(3)
                            clear_screen()
                        elif password_lenth < MIN_LEN:
                            print("Password lenth cannot be lower than the lenth of 8")
                            time.sleep(3)
                            clear_screen()
                    except ValueError:
                        clear_screen()
                        print("Please enter a whole number only")
                        time.sleep(3)
                if password_lenth <= MAX_LEN and password_lenth >= MIN_LEN:
                    password = password_ultimate(password_lenth)
                    print(f'your Generated Password is: {password}')
                    save_pass(platform=platform, password=password)
                    countdown(30)
                clear_screen()
                main_menu()
            if choose_option == '3':
                clear_screen()
                main_menu()
        else:
            print("Please enter a number.")
    def saved_pass_menu():
        saved_pass_file = open('saved_passwords.txt', 'r')
        method = saved_pass_file.read
        spm_read = method()
        print(spm_read)
        print("'Ctrl + c' to go to main menu")
        try:
            countdown(300)
        except KeyboardInterrupt:
            clear_screen()
            main_menu()

    def del_saved_pass_menu():
        def del_saved_pass(file, line_num):
            with open(file, 'r') as f:
                lines = f.readlines()
            with open(file, "w") as f:
                for i in range(len(lines)):
                    if i != line_num:
                        f.write(lines[i])
            time.sleep(2)
            f.close()

        def convert_txt_file_to_list(file):
            with open(file, 'r') as f:
                data = f.read()
                data_into_list = data.replace('\n', '').split('.')
            return data_into_list

        def get_total_lines_from_a_file(file):
            with open(file, 'r') as f:
                count = sum(1 for line in f)
            return count

        def delete_line(filename, line_number):
            with open(filename, "r") as f:
                lines = f.readlines()

            with open(filename, "w") as f:
                for i, line in enumerate(lines):
                    if i != line_number:
                        f.write(line)

        file = 'saved_passwords.txt'
        lines = convert_txt_file_to_list(file)

        for i, line in enumerate(lines):
            print(f"{i}. {line}")

        line_num = input("Choose the index of the password to delete: ")
        if line_num.isdigit():
            delete_line(file, int(line_num))
            print('The line has been deleted.')
        else:
            print('Invalid input. Please enter a valid line number.')



    def main_menu():
        choose_option = input(" 1. Password Generator\n 2. See saved Passwords\n 3. Delete saved passwords\n 4. Master key options\n 5. Change configuration\n 6. Quit\n Choose a option: ")
        if choose_option.isdigit:
            if choose_option == '1':
                clear_screen()
                pass_gen_menu()
            elif choose_option == '2':
                clear_screen()
                try:
                    saved_pass_menu()
                except FileNotFoundError:
                    print("you need to create passwords to see saved passwords.")
                    time.sleep(5)
                    clear_screen()
                    main_menu()
            elif choose_option == '3':
                clear_screen()
                try:
                    del_saved_pass_menu()
                except FileNotFoundError:
                    print("you need to create passwords to delete saved passwords.")
                    time.sleep(5)
                clear_screen()
                main_menu()
            elif choose_option == '4':
                clear_screen()
                master_key_menu()
            elif choose_option == '5':
                clear_screen()
                config_menu()
            elif choose_option == '6':
                clear_screen()
                print("See you again!")
                exit()
        else:
            ("Enter a digit")
    main_menu()

def run_pass_gen():
    clear_screen()
    write_master_key()
    if os.path.isfile('master_key.txt'):
        master_key_file = open('master_key.txt', 'r+')
        method = master_key_file.read
        mk_check = method()
        if mk_check != '':
            master_key_file.close()
            user_input()
    else:
        print("Master key is must to continue.")
        exit()
try:
    master_key_file = open('master_key.txt', 'r+')
    method = master_key_file.read
    mk_check = method()
    total_try = 0
    emergency_vanish = False
    while not(emergency_vanish) and total_try <= 5 :
        check_master_key = input("Enter the master key:\n\n")
        if secrets.compare_digest(check_master_key, mk_check):
            master_key_file.close()
            try:
                run_pass_gen()
                break
            except KeyboardInterrupt and TypeError:
                clear_screen()
                print("See you again!")
            except NameError:
                clear_screen()
                print("This menu is under construction")
                run_pass_gen()
        elif total_try > 5:
            emergency_vanish = True
            master_key_file.close()
            if os.name == "nt":
                os.system("del /f saved_passwords.txt && del /f master_key.txt")
                print("FILE DELETED!")
            else:
                os.system("rm saved_passwords.txt && rm master_key.txt")
                print("FILE DELETED!")
        else:
            print("the master key is wrong")
            total_try += 1
except FileNotFoundError:
    try:
        run_pass_gen()
    except ValueError or TypeError:
        clear_screen()
        print("See you again!")