from tkinter import *
from random import choice
from random import shuffle

root = Tk()
root.title('Word-Jumble')
root.geometry("600x400")

my_label = Label(root, text="", font=("Helbetica", 48))
my_label.pack()

def shuffler():
    global word
    #Clear Hint Label
    hint_label.config(text='')
    
    #Clear Hint Count
    global hint_count
    hint_count = 0 

    #Clear Entry Box
    entry_answer.delete(0, END)

    #Clear Answer Label
    answer_label.config(text='')

    #List of Words
    with open("10000 words.txt") as f:
        words = [word for line in f for word in line.split()]

    #Pick random worde
    word = choice(words)
    my_label.config(text=word)

    #Break Apart the Word
    break_apart_word = list(word)
    shuffle(break_apart_word)

    #Turn Shuffled List into a word
    global shuffled_word
    shuffled_word = ''
    for letter in break_apart_word:
        shuffled_word += letter

    #Print Shuffled word to the screen
    my_label.config(text=shuffled_word)

def answer():
    if word == entry_answer.get():
        answer_label.config(text='Correct!')
    else:
        answer_label.config(text='Incorrect!')

global hint_count
hint_count = 0

def hint(count):
    global hint_count
    hint_count = count
    
    word_length = len(word)

    if count < word_length:
        hint_label.config(text=f'{hint_label["text"]} {word[count]}')
        hint_count +=1


entry_answer = Entry(root, font=('Helvetica', 24))
entry_answer.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

my_button = Button(button_frame, text="Pick Another Word", command=shuffler)
my_button.grid(row=0, column=0, padx=10)

Answer_button = Button(button_frame, text="Answer", command=answer)
Answer_button.grid(row=0, column=1, padx=10)

hint_button = Button(button_frame, text='Hint', command=lambda: hint(hint_count))
hint_button.grid(row=0, column=2, padx=10)

answer_label = Label(root, text='', font=("Helvetica", 18))
answer_label.pack(pady=20)

hint_label = Label(root, text='', font=("Helvetica", 18))
hint_label.pack(pady=20)

root.mainloop()