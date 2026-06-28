import math
import numpy as np
from scipy.io import wavfile

# --- MY AP PRECALC MATH EXPERIMENT ---
# This script turns sine wave equations into an actual playable audio file.
# Equation from class: y = Amplitude * sin(2 * pi * frequency * time)

sampling_rate = 44100  # Standard CD quality (44100 data points per second)

def make_sine_wave(frequency, duration, volume=0.5):
    """Generates a list of numbers representing a single note using sine math."""
    total_samples = int(sampling_rate * duration)
    
    # Standard python list to hold our math points
    wave_data = []
    
    for i in range(total_samples):
        # Calculate time (t) for this specific data point
        t = i / sampling_rate
        
        # This is the exact sine wave equation from my precalc textbook!
        y = volume * math.sin(2 * math.pi * frequency * t)
        wave_data.append(y)
        
    return wave_data

def add_fade(wave):
    """Fades the note in and out so it doesn't make a loud clicking noise."""
    total_samples = len(wave)
    fade_size = int(0.1 * sampling_rate) # Fade for 0.1 seconds
    
    # If the note is too short, skip the fade
    if total_samples < (fade_size * 2):
        return wave
        
    # Apply linear multiplier to smooth the audio signal
    for i in range(fade_size):
        # Fade in at the start
        wave[i] = wave[i] * (i / fade_size)
        # Fade out at the end
        end_index = total_samples - 1 - i
        wave[end_index] = wave[end_index] * (i / fade_size)
        
    return wave

def make_chord(frequencies, duration):
    """Combines multiple notes together to make a chord chord harmony."""
    total_samples = int(sampling_rate * duration)
    chord_data = [0.0] * total_samples
    
    # Loop through each note frequency in the chord
    for freq in frequencies:
        note_wave = make_sine_wave(freq, duration, volume=0.3)
        note_wave = add_fade(note_wave)
        
        # Add the waves together point by point
        for i in range(total_samples):
            chord_data[i] = chord_data[i] + note_wave[i]
            
    # Divide by number of notes so the audio doesn't distort/clip
    for i in range(total_samples):
        chord_data[i] = chord_data[i] / len(frequencies)
        
    return chord_data

# --- RUNNING THE SYNTH ---
# Musical note frequencies in Hz (A minor going to F major)
aminor_chord = [220.00, 261.63, 329.63]  # A, C, E notes
fmajor_chord = [174.61, 220.00, 261.63]  # F, A, C notes

print("Calculating chord matrices using sine equations...")
chord_1 = make_chord(aminor_chord, duration=2.0)
chord_2 = make_chord(fmajor_chord, duration=2.0)

# Combine the two chords into one song list
full_song = chord_1 + chord_2

# Convert our python list into a standard 16-bit audio format
audio_array = np.array(full_song, dtype=np.float32)
audio_data = np.int16(audio_array * 32767)

# Export the file so we can play it
output_file = "my_precalc_synth.wav"
wavfile.write(output_file, sampling_rate, audio_data)
print(f"Done! Created audio file: {output_file}")
