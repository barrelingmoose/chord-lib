import theory.chords
import theory.theory_constants as tc

class Guitar:
    def __init__(self, tuning="EADGBE"): 
        self.string_count = 6
        self.frets = 24
        self.half_frets = 12 
        self.tuning = tuning.upper()
        self.fretboard = {}
        self.tuning_list = list(tuning)

    def fretboard_display(self, note_list, filter=[]): 
        fret_note = "|"
        for note in note_list:
            if not filter: 
                fret_note += "---{}---|".format(note)
            elif note in filter: 
                fret_note += "---{}---|".format(note)
            else:
                fret_note += "-------|"
        print(fret_note)

    def get_notes(self, tuning):
        for note in self.tuning_list: 
            string_notes = []
            root_position = tc.notes_to_pos.get(note)
            for fret in range(self.half_frets): 
                if fret + root_position < self.half_frets + 1:
                    next_note = tc.pos_to_notes.get(fret+root_position)
                    string_notes.append(next_note)
                else:
                    next_note = tc.pos_to_notes.get((fret+root_position)-12)
                    string_notes.append(next_note)
            string_notes += string_notes
            self.fretboard[note] = string_notes
        
            self.fretboard_display(string_notes)
    
    def find_notes(self, lst, value): 
        return [i for i, x in enumerate(lst) if x == value]
    
    def sixth_string_as_root(): 
        return True

    def fifth_string_as_root():
        return True

    def fourth_string_as_root(): 
        return True

    def find_chord(self, scale, search):
        chords = theory.chords.Chords(scale)
        note_list = list(chords.scale_chords.get(search))
        print("***{} Voicings***".format(search))
        for items in self.tuning_list:
            self.fretboard_display(self.fretboard.get(items), note_list)
        

    def intitialize(self):
        self.get_notes(self.tuning)


        
