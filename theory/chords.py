import theory.theory_constants as tc

class Note: 
    def __init__(self, name):
        self.name = name

class Scale(Note): 
    def __init__(self, root):
        self.root = root
        self.positions = []
        self.pos = 0
        self.scale = []
        self.scale_name = ""

    def copy_constructor(self, other):
        self.root = other.root
        self.positions = other.positions
        self.pos = other.pos 
        self.scale = other.scale
        self.scale_name = other.scale_name
        return self

    def append_root(self): 
        self.positions.append(self.pos)

    def append_whole(self): 
        self.pos += 2 
        if self.pos > 12: 
            self.pos = self.pos - 12
        self.positions.append(self.pos)

    def append_half(self): 
        self.pos += 1 
        if self.pos > 12: 
            self.pos = self.pos - 12
        self.positions.append(self.pos) 

    # Major R-W-W-H-W-W-W-H(R) 
    # Ex: C D E F G A B 
    def major_scale(self):
        self.positions.clear()
        self.scale.clear()
        self.scale_name = tc.pos_to_scale_modes.get(1)
        if self.root in tc.notes_to_pos.keys(): 
            self.pos = tc.notes_to_pos.get(self.root) # root position
            self.append_root() # root position 
            self.append_whole() # second position 
            self.append_whole() # third position  
            self.append_half() # fourth position 
            self.append_whole() # fifth position  
            self.append_whole() # sixth posion 
            self.append_whole() # seventh position 

        for items in self.positions: 
            self.scale.append(tc.pos_to_notes.get(items))
    
    # Minor R-W-H-W-W-H-W-W(R) 
    # Ex: A B C D E F G 
    def minor_scale(self): 
        self.positions.clear()
        self.scale.clear()
        self.scale_name = tc.pos_to_scale_modes.get(6)
        if self.root in tc.notes_to_pos.keys(): 
            self.pos = tc.notes_to_pos.get(self.root) # root position
            self.append_root() # root position 
            self.append_whole() # second position 
            self.append_half() # third position 
            self.append_whole() # fourth position  
            self.append_whole() # fifth position  
            self.append_half() # sixth posion 
            self.append_whole() # seventh position 
        
        for items in self.positions: 
            self.scale.append(tc.pos_to_notes.get(items))

class Chords(Scale):
    def chords(self, scale): 
        scale_chords = {}
        # I ii iii IV V vi vii* if major(Ionian)
        if self.scale_name == tc.pos_to_scale_modes.get(1): 
            for i in range(len(self.scale)): 
                root_note = i
                chord_root = self.scale[root_note]
                if i == 0 or i == 3 or i == 4: 
                    self.chord_name = chord_root + " Major"
                elif i == 6:
                    self.chord_name = chord_root + " Diminished"
                else: 
                    self.chord_name = chord_root + " Minor"
                if i + self.third_note> (len(self.scale)-1): 
                    major_third = (i + self.third_note) - len(self.scale)
                else:
                    major_third = i + self.third_note
                chord_third = self.scale[major_third]
                if i + self.fifth_note > (len(self.scale)-1):
                    major_fifth = (i + self.fifth_note) - len(self.scale)
                else: 
                    major_fifth = i + self.fifth_note
                chord_fifth = self.scale[major_fifth]
                chord = chord_root + chord_third + chord_fifth
                scale_chords[self.chord_name] = chord 
        if self.scale_name == tc.pos_to_scale_modes.get(2): 
            pass
        if self.scale_name == tc.pos_to_scale_modes.get(3): 
            pass
        if self.scale_name == tc.pos_to_scale_modes.get(4): 
            pass
        if self.scale_name == tc.pos_to_scale_modes.get(5): 
            pass
        if self.scale_name == tc.pos_to_scale_modes.get(6): 
            pass
        # i ii* III iv v VI VII if minor 
        if self.scale_name == tc.pos_to_scale_modes.get(7): 
            pass
        return scale_chords
        

    def __init__(self, scale):
        self.root = scale.root
        self.positions = scale.positions
        self.pos = scale.pos 
        self.scale = scale.scale
        self.scale_name = scale.scale_name
        self.first_position = 0
        self.third_note= 2
        self.fifth_note = 4
        self.chord_name = ""
        self.scale_chords = self.chords(scale)

    def display_chords(self):
        for chords in self.scale_chords.keys():
            print(chords)

    
        



