from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *
import file_menu
import edit_menu
import format_menu
import help_menu
import time
import sys 
from threading import Thread


class App(Tk):

    def __init__(self, file):
        super().__init__()

        self.title("Text Editor-Untiltled")
        self.geometry("300x250+300+300")
        self.minsize(width=400, height=400) 
        self.text = ScrolledText(self, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True)
        self.text.pack(fill=Y, expand=1)
        self.text.focus_set()
        menu = Menu(self)
        file_menu.main(self, self.text, menu)
        edit_menu.main(self, self.text, menu)
        format_menu.main(self, self.text, menu)
        help_menu.main(self, self.text, menu) 

        self.file = file 
        Thread(target=self.run, daemon=True).start()

    def get_text_object(self):
        return self.text 

    def run(self):
        last_len_text = 1
        while True:
            text = self.text.get("1.0", "end-1c")
            text_split = text.split(" ")
            n = len(text_split)

            if last_len_text > n:
                last_len_text = 1

            if len(text) > 0 and last_len_text != n and text[-1] == " ":

                word = text_split[-2]
                if n > last_len_text:
                    self.is_palindrome(word)
                    self.in_file(word)
                    self.reverse_in_file(word)
                    self.is_two_palindrome(word)
                    print()


                last_len_text = n


    def is_palindrome(self, word):
        if word.lower() == word[::-1].lower():
            print(f"the {word} is palindrome")
        else:
            print(f"the {word} is not palindrome")

    def in_file(self, word):
        if word in self.file:
            print(f"the {word} is meaningful")
        else:
            print(f"the {word} is not meaningful")

    def reverse_in_file(self, word):
        if word[::-1] in self.file:
            print(f"reverse of {word} is meaningful")
        else:
            print(f"reverse of {word} is not meaningful")

    def is_two_palindrome(self, word):
        p = True 

        
        for i in range(len(word)//2):
            if word[i] != word[len(word)-1-i]:
                p = False 

        if p:
            print(f"the {word} is two word palindrome")
        else:
            print(f"the {word} is not two word palindrome")


if __name__ == "__main__":

    with open("words.txt", "r") as f:
        file = f.readlines()

    file = list(file)
    file = list(map(lambda w: w.strip(), file))

    app = App(file)
    app.mainloop()


