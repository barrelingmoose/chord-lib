import guitar.guitar
import theory.chords
import theory.theory_constants as tc 
import theory
import guitar.guitar as gg


if __name__ == "__main__": 
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
    c_chords.display_chords()
    my_guitar.find_chord(c_scale, "C Major")