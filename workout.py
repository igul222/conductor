from conductor import *

prepare('bike', 60)
tone(HIGH) # cue to start
advance(2 * 60)
say('10 minutes remaining', no_advance=True)
advance(5 * 60)
say('5 minutes remaining', no_advance=True)
advance((5 * 60) - 10)
countdown(10)
tone(HIGH) # cue to stop

prepare('ankle exercises', 30)
say('Dorsiflexion plantarflexion')
basic_set(20, 2)
say('Inversion eversion')
basic_set(20, 2)
say('Clockwise circles')
basic_set(20, 1)
say('Counter-clockwise circles')
basic_set(20, 1)

prepare('heel raises', 30)
basic_set(20, 2)

prepare('toe raises', 30)
basic_set(20, 1)

prepare('toe curls', 30)
advance(3*60 - 10)
countdown(10)

prepare('bridges', 30)
isometric_set(10, 10)

prepare('wall push', 30)
isometric_set(10, 10)

prepare(f'left leg forward raise', 30)
isometric_set(15, 5)

prepare(f'right leg forward raise', 10)
isometric_set(15, 5)

prepare(f'left leg sideways raise', 10)
isometric_set(15, 5)

prepare(f'right leg sideways raise', 10)
isometric_set(15, 5)

prepare(f'left leg backward raise', 10)
isometric_set(15, 5)

prepare(f'right leg backward raise', 10)
isometric_set(15, 5)

prepare('towel stretch', 30)
isometric_set(3, 30)

say('Workout finished, good job.')

write_output('workout')