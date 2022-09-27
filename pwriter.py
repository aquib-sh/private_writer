#!/usr/bin/python3

import sys
import os

class PWriter:
    def __init__(self, filename):
        f_fullpath = os.path.join(os.getcwd(), filename)
        f_mode = "w"
        if os.path.exists(f_fullpath):
            f_mode = "a"

        self.__fp = open(f_fullpath, f_mode)                    # file pointer
        self.quit_trigger = "CLOSE_FILE"                        # word which triggers program to quit

        self.clear_screen_fn = lambda: os.system("clear")       # fn to clear console
        if sys.platform == "win32":                             # Windows specific clear console fn
            self.__clear_screen_fn = lambda: os.system("cls")

        
    def write(self, line):
        self.__fp.writelines(line + "\n")


    def quit(self):
        self.__fp.close()


    def start(self):
        print("""
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$ PRIVATE WRITER $$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n

        ** Write 'CLOSE_FILE' to save text file and quit program. **\n"""
        )
        while ((line := input("$> ")) != self.quit_trigger):
            self.write(line)
            self.clear_screen_fn()
        self.quit()


if __name__ == "__main__":
    filename = sys.argv[1]
    PWriter(filename).start()

