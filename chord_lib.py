import theory.chords
import theory.theory_constants as tc 
import theory


if __name__ == "__main__": 
    a_scale = theory.chords.Scale("A")
    a_scale.major_scale()
    c_scale = theory.chords.Scale("C")
    c_scale.major_scale()

    a_chords = theory.chords.Chords(a_scale)
    c_chords = theory.chords.Chords(c_scale)