from tkinter import *
from tkinter import messagebox
import theory.chords
import theory.theory_constants as tc 
import theory
import guitar.guitar as gg

def start_gui(): 
    root = Tk()
    w = Label(root, text='Chord Library')
    w.pack()
    root.title('Scale')
    a_scale = theory.chords.Scale("A")
    a_scale.major_scale()
    c_scale = theory.chords.Scale("C")
    c_scale.major_scale()

    a_chords = theory.chords.Chords(a_scale)
    c_chords = theory.chords.Chords(c_scale)

    midwest_tuning = "FACGCE"
    standard_tuning = "EADGBE"
    my_guitar = gg.Guitar(midwest_tuning)
    my_guitar.intitialize()
    
    text_widget = Text(root)
    text_widget.pack()
    button = Button(root, text="Print", command=c_chords.display_chords(text_widget))
    button.pack()
    chords = Button(root, text="Chords", command=my_guitar.find_chord(c_scale, "C Major", text_widget))
    chords.pack()
    root.mainloop()