# dsp-waveform-synthesizer

# AP Precalc Sine Wave Audio Synthesizer

A simple Python script I built during my junior year to turn the trigonometry equations from my AP Precalculus class into real music.

## Why I Built This
In AP Precalc, we spend a lot of time graphing periodic sine waves on calculators using formulas like $y = A \sin(B(x-C))$. I realized that these squiggly textbook lines are actually the exact physical math behind sound waves and audio frequencies. 

I wanted to see if I could write a program to bring these equations to life. This script calculates raw data points along a sine wave mathematical curve and converts them directly into a playable `.wav` audio track.

## How It Works
1. **Sine Wave Generation**: The program uses a standard `for` loop to calculate time increments and plugs them directly into `math.sin()`.
2. **Volume Envelope / Fading**: If an audio wave stops suddenly, it makes an annoying popping sound. I wrote a function that loops through the first and last 10% of the audio points to manually blend the volume down to zero.
3. **Chord Layering**: To make chords, the script loops through an array of musical notes, calculates their individual sine values, adds them together, and averages them out so it doesn't get too loud.

## How to Test It
Make sure you have `numpy` and `scipy` installed, then run:
```bash
python waveform_synth.py
```
