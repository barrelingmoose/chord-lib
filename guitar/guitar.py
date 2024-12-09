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
    
    def find_notes(self, lst, value): 
        return [i for i, x in enumerate(lst) if x == value]
    
    def sixth_string_as_root(): 
        return True

    def fifth_string_as_root():
        return True

    def fourth_string_as_root(): 
        return True

    def find_chord(self, scale, search):
        note_count = 0
        chords = theory.chords.Chords(scale)
        note_list = list(chords.scale_chords.get(search))
        for notes in note_list: 
            string_pos = 0
            for guitar_string in self.tuning_list: 
                cur_string = self.fretboard.get(guitar_string)
                note_positions = self.find_notes(cur_string, notes)
                if string_pos == 1 and note_count == 0:
                    print(f"{guitar_string}:{notes}:{self.find_notes(cur_string, notes)}")
                    root_note = note_positions[0]
                if string_pos != 1 and note_count != 0:
                    note_options = self.find_notes(cur_string, notes)
                    for options in note_options: 
                        if abs(options - root_note) < 4:
                            print(f"{guitar_string}:{notes}:{options}")
                string_pos += 1
            note_count += 1
        

    def intitialize(self):
        self.get_notes(self.tuning)
        print(self.fretboard)


        
