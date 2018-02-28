#! python3

import sys, os, random

pick = [ sys.argv[x] for x in range(len(sys.argv)) if len(sys.argv) > 1 and x != 0 ]
notes = [
	[ 'C',
		[
			{ 'minor_second/major_seventh'  : 'C#/Db' },
			{ 'major_second/minor_seventh' : 'D' },
			{ 'minor_third/major_sixth' : 'D#/Eb' },
			{ 'major_third/minor_sixth' : 'E' },
			{ 'perfect_fourth/perfect_fifth' : 'F' },
			{ 'augmented_fourth/augmented_fourth' : 'F#/Gb' },
			{ 'perfect_fifth/perfect_fourth' : 'G' },
			{ 'minor_sixth/major_third' : 'G#/Ab' },
			{ 'major_sixth/minor_third' : 'A' },
			{ 'minor seventh/major_second' : 'A#/Bb' },
			{ 'major_seventh/minor_second' : 'B' },
			{ 'octave/octave' : 'C' }
		]
	],
	[ 'C#/Db',
		[
			{ 'minor_second/major_seventh'  : 'D' },
			{ 'major_second/minor_seventh' : 'D#/Eb' },
			{ 'minor_third/major_sixth' : 'E' },
			{ 'major_third/minor_sixth' : 'F' },
			{ 'perfect_fourth/perfect_fifth' : 'F#/Gb' },
			{ 'augmented_fourth/augmented_fourth' : 'G' },
			{ 'perfect_fifth/perfect_fourth' : 'G#/Ab' },
			{ 'minor_sixth/major_third' : 'A' },
			{ 'major_sixth/minor_third' : 'A#/Bb' },
			{ 'minor seventh/major_second' : 'B' },
			{ 'major_seventh/minor_second' : 'C' },
			{ 'octave/octave' : 'C#/Db' }
		]
	],
	[ 'D',
		[
			{ 'minor_second/major_seventh'  : 'D#/Eb' },
			{ 'major_second/minor_seventh' : 'E' },
			{ 'minor_third/major_sixth' : 'F' },
			{ 'major_third/minor_sixth' : 'F#/Gb' },
			{ 'perfect_fourth/perfect_fifth' : 'G' },
			{ 'augmented_fourth/augmented_fourth' : 'G#/Ab' },
			{ 'perfect_fifth/perfect_fourth' : 'A' },
			{ 'minor_sixth/major_third' : 'A#/Bb' },
			{ 'major_sixth/minor_third' : 'B' },
			{ 'minor seventh/major_second' : 'C' },
			{ 'major_seventh/minor_second' : 'C#/Db' },
			{ 'octave/octave' : 'D' }
		]
	],
	[ 'D#/Eb',
		[
			{ 'minor_second/major_seventh'  : 'E' },
			{ 'major_second/minor_seventh' : 'F' },
			{ 'minor_third/major_sixth' : 'F#/Gb' },
			{ 'major_third/minor_sixth' : 'G' },
			{ 'perfect_fourth/perfect_fifth' : 'G#/Ab' },
			{ 'augmented_fourth/augmented_fourth' : 'A' },
			{ 'perfect_fifth/perfect_fourth' : 'A#/Bb' },
			{ 'minor_sixth/major_third' : 'B' },
			{ 'major_sixth/minor_third' : 'C' },
			{ 'minor seventh/major_second' : 'C#/Db' },
			{ 'major_seventh/minor_second' : 'D' },
			{ 'octave/octave' : 'D#/Eb' }
		]
	],
	[ 'E',
		[
			{ 'minor_second/major_seventh'  : 'F' },
			{ 'major_second/minor_seventh' : 'F#/Gb' },
			{ 'minor_third/major_sixth' : 'G' },
			{ 'major_third/minor_sixth' : 'G#/Ab' },
			{ 'perfect_fourth/perfect_fifth' : 'A' },
			{ 'augmented_fourth/augmented_fourth' : 'A#/Bb' },
			{ 'perfect_fifth/perfect_fourth' : 'B' },
			{ 'minor_sixth/major_third' : 'C' },
			{ 'major_sixth/minor_third' : 'C#/Db' },
			{ 'minor seventh/major_second' : 'D' },
			{ 'major_seventh/minor_second' : 'D#/Eb' },
			{ 'octave/octave' : 'E' }
		]
	],
	[ 'F',
		[
			{ 'minor_second/major_seventh'  : 'F#/Gb' },
			{ 'major_second/minor_seventh' : 'G' },
			{ 'minor_third/major_sixth' : 'G#/Ab' },
			{ 'major_third/minor_sixth' : 'A' },
			{ 'perfect_fourth/perfect_fifth' : 'A#/Bb' },
			{ 'augmented_fourth/augmented_fourth' : 'B' },
			{ 'perfect_fifth/perfect_fourth' : 'C' },
			{ 'minor_sixth/major_third' : 'C#/Db' },
			{ 'major_sixth/minor_third' : 'D' },
			{ 'minor seventh/major_second' : 'D#/Eb' },
			{ 'major_seventh/minor_second' : 'E' },
			{ 'octave/octave' : 'F' }
		]
	],
	[ 'F#/Gb',
		[
			{ 'minor_second/major_seventh'  : 'G' },
			{ 'major_second/minor_seventh' : 'G#/Ab' },
			{ 'minor_third/major_sixth' : 'A' },
			{ 'major_third/minor_sixth' : 'A#/Bb' },
			{ 'perfect_fourth/perfect_fifth' : 'B' },
			{ 'augmented_fourth/augmented_fourth' : 'C' },
			{ 'perfect_fifth/perfect_fourth' : 'C#/Db' },
			{ 'minor_sixth/major_third' : 'D' },
			{ 'major_sixth/minor_third' : 'D#/Eb' },
			{ 'minor seventh/major_second' : 'E' },
			{ 'major_seventh/minor_second' : 'F' },
			{ 'octave/octave' : 'F#/Gb' }
		]
	],
	[ 'G',
		[
			{ 'minor_second/major_seventh'  : 'G#/Ab' },
			{ 'major_second/minor_seventh' : 'A' },
			{ 'minor_third/major_sixth' : 'A#/Bb' },
			{ 'major_third/minor_sixth' : 'B' },
			{ 'perfect_fourth/perfect_fifth' : 'C' },
			{ 'augmented_fourth/augmented_fourth' : 'C#/Db' },
			{ 'perfect_fifth/perfect_fourth' : 'D' },
			{ 'minor_sixth/major_third' : 'D#/Eb' },
			{ 'major_sixth/minor_third' : 'E' },
			{ 'minor seventh/major_second' : 'F' },
			{ 'major_seventh/minor_second' : 'F#/Gb' },
			{ 'octave/octave' : 'G' }
		]
	],
	[ 'G#/Ab',
		[
			{ 'minor_second/major_seventh'  : 'A' },
			{ 'major_second/minor_seventh' : 'A#/Bb' },
			{ 'minor_third/major_sixth' : 'B' },
			{ 'major_third/minor_sixth' : 'C' },
			{ 'perfect_fourth/perfect_fifth' : 'C#/Db' },
			{ 'augmented_fourth/augmented_fourth' : 'D' },
			{ 'perfect_fifth/perfect_fourth' : 'D#/Eb' },
			{ 'minor_sixth/major_third' : 'E' },
			{ 'major_sixth/minor_third' : 'F' },
			{ 'minor seventh/major_second' : 'F#/Gb' },
			{ 'major_seventh/minor_second' : 'G' },
			{ 'octave/octave' : 'G#/Ab' }
		]
	],
	[ 'A',
		[
			{ 'minor_second/major_seventh'  : 'A#/Bb' },
			{ 'major_second/minor_seventh' : 'B' },
			{ 'minor_third/major_sixth' : 'C' },
			{ 'major_third/minor_sixth' : 'C#/Db' },
			{ 'perfect_fourth/perfect_fifth' : 'D' },
			{ 'augmented_fourth/augmented_fourth' : 'D#/Eb' },
			{ 'perfect_fifth/perfect_fourth' : 'E' },
			{ 'minor_sixth/major_third' : 'F' },
			{ 'major_sixth/minor_third' : 'F#/Gb' },
			{ 'minor seventh/major_second' : 'G' },
			{ 'major_seventh/minor_second' : 'G#/Ab' },
			{ 'octave/octave' : 'A' }
		]
	],
	[ 'A#/Bb',
		[
			{ 'minor_second/major_seventh'  : 'B' },
			{ 'major_second/minor_seventh' : 'C' },
			{ 'minor_third/major_sixth' : 'C#/Db' },
			{ 'major_third/minor_sixth' : 'D' },
			{ 'perfect_fourth/perfect_fifth' : 'D#/Eb' },
			{ 'augmented_fourth/augmented_fourth' : 'E' },
			{ 'perfect_fifth/perfect_fourth' : 'F' },
			{ 'minor_sixth/major_third' : 'F#/Gb' },
			{ 'major_sixth/minor_third' : 'G' },
			{ 'minor seventh/major_second' : 'G#/Ab' },
			{ 'major_seventh/minor_second' : 'A' },
			{ 'octave/octave' : 'A#/Bb' }
		]
	],
	[ 'B',
		[
			{ 'minor_second/major_seventh'  : 'C' },
			{ 'major_second/minor_seventh' : 'C#/Db' },
			{ 'minor_third/major_sixth' : 'D' },
			{ 'major_third/minor_sixth' : 'D#/Eb' },
			{ 'perfect_fourth/perfect_fifth' : 'E' },
			{ 'augmented_fourth/augmented_fourth' : 'F' },
			{ 'perfect_fifth/perfect_fourth' : 'F#/Gb' },
			{ 'minor_sixth/major_third' : 'G' },
			{ 'major_sixth/minor_third' : 'G#/Ab' },
			{ 'minor seventh/major_second' : 'A' },
			{ 'major_seventh/minor_second' : 'A#/Bb' },
			{ 'octave/octave' : 'B' }
		]
	]
]

modes = {
	'dorian' : [ 1, 2, 4, 6, 7, 9 ]
}

def main(options) :
	random_note = random.randint(0, 11)
	random_interval = int(round(random.uniform(-12, 11)))
	mode = False

	if options :
		if len(options) == 2 :
			if options[1].lower() in modes :
				mode = { "index" : 0, "intervals" : modes[options[1].lower()] }
		for n in range(len(notes)) :
			if notes[n][0] == options[0] :
				random_note = n
				break

	choose_note(random_note, random_interval, mode)


def choose_note(rnote, rinterval, mode) :
	if mode :
		if mode['index'] == len(mode['intervals']) :
			mode['index'] = 0

		rinterval = mode['intervals'][mode['index']]
		mode['index'] = mode['index'] + 1

	interval_quality = "DOWN A(N) " if rinterval < 0 else "UP A(N) "
	interval = list(notes[rnote][1][rinterval].keys())[0].split('/')[1 if rinterval < 0 else 0 ].upper().replace('_', ' ')
	correct_note = list(notes[rnote][1][rinterval].values())[0].split('/')

	guess = input('Current note : ' + notes[rnote][0] + '\n' + interval_quality + interval + ' : ')

	if guess == correct_note[0] :
		print('Correct\n')
	else :
		try :
			if guess == correct_note[1] :
				print('Correct\n')
			else :
				print('Wrong. Correct is : {note} \n'.format(note=correct_note))
		except IndexError :
			print('Wrong. Correct is : {note} \n'.format(note=correct_note))

	choose_note(rnote, rinterval, mode)

main(pick)
# choose_note(pick, 0)
