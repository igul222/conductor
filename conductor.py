import numpy as np
import soundfile
import os
import librosa

SAMPLE_RATE = 22050

TRACK = np.zeros((SAMPLE_RATE * 60 * 60 * 24,))
CURSOR = 0

# Core framework

def insert_audio(wav, sample_rate, no_advance=False):
    global CURSOR
    wav = librosa.resample(wav, sample_rate, SAMPLE_RATE)
    TRACK[CURSOR : (CURSOR + wav.shape[0])] += wav
    if not no_advance:
        CURSOR += wav.shape[0]

def advance(seconds):
    global CURSOR
    CURSOR += int(SAMPLE_RATE * seconds)

def write_output(name):
    soundfile.write(f'{name}.wav', TRACK[:CURSOR], SAMPLE_RATE)

# Primitives

_tts_cache = {}
def say(text, no_advance=False):
    print(text)
    if text not in _tts_cache:
        path = '/tmp/conductor_tts_audio.aiff'
        os.system(f'say -o {path} {text}')
        wav, sample_rate = soundfile.read(path)
        os.system(f'rm {path}')
        _tts_cache[text] = (wav, sample_rate)
    wav, sample_rate = _tts_cache[text]
    insert_audio(wav, sample_rate, no_advance)
    if not no_advance:
        advance(0.25)

MID = 440
HIGH = 880
def tone(freq, no_advance=False):
    """0.5-second tone, then 0.5-second silence."""
    x = np.arange(0.5 * SAMPLE_RATE, dtype='float32')
    wav = np.sin(x * (2 * np.pi * freq / SAMPLE_RATE)) * 0.25
    insert_audio(wav, SAMPLE_RATE, no_advance)
    if not no_advance:
        advance(0.5)

# Higher-level functions

def prepare(description, seconds):
    say(f'Prepare for {description}')
    countdown(seconds)

def countdown(seconds):
    for i in range(seconds, 0, -1):
        say(i, no_advance=True)
        advance(1)

def basic_set(reps, seconds):
    for i in range(1, reps+1):
        tone(HIGH, no_advance=True)
        advance(seconds)
        say(i)

def isometric_set(reps, seconds):
    for i in range(1, reps+1):
        tone(HIGH) # enter position
        for i in range(seconds):
            tone(MID, 0.5) # hold
        tone(HIGH) # exit position
        say(str(i), no_advance=True)
        advance(1) # rest