import speech_recognition as speech_recog
from flask import Flask, render_template, request, redirect

def TranscriptionIA():
    recog = speech_recog.Recognizer()
    with speech_recog.Microphone() as source:
        recog.adjust_for_ambient_noise(source)
        audio = recog.listen(source)
    return recog.recognize_google(audio, language="es-ES")
