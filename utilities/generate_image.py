import abjad
from PIL import Image

string = "c'4 d'4 e'4 f'4 g'2 g'2 a'4 a'4 a'4 a'4 g'1 a'4 a'4 a'4 a'4 g'1"
output_image = 'output_image.png'

voice_1 = abjad.Voice(string, name="Voice_1")
staff_1 = abjad.Staff([voice_1], name="Staff_1")
score_1 = abjad.Score([staff_1], name="Score")

abjad.setting(score_1).proportional_notation_duration = "#(ly:make-moment 1 8)"

# Render the staff as an image

abjad.persist.as_png(score_1, '../img/viola/piece1.png')

# Open the image using PIL
image = Image.open('../img/viola/piece1.png')

# Crop the image to remove the empty space above the staff
cropped_image = image.crop((90, 20, 1000, 90))

# Save the cropped image
cropped_image.save('../img/cropped_piece1.png')



