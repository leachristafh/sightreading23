import abjad
from PIL import Image

input_file = '../img/viola/piece2_wide_input.ly'
# Path to output PNG file
output_file = '../img/viola/piece2_wide.png'
# Compile LilyPond file using Abjad

parser = abjad.parser.LilyPondParser()

#read out lilypond file into string
with open(input_file, 'r') as file:
    string = file.read().replace('\n', '')

print(string)

staff = parser(string)

abjad.persist.as_png(staff, output_file)
