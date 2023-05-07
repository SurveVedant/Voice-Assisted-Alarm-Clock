# Voice-Assisted-Alarm-Clock

This Python script sets an alarm clock using voice commands. 
The script uses the speech_recognition library to capture the user’s voice input for the hour, minute, and am/pm of the alarm. 
The script first prompts the user to speak the hour of the alarm and captures their voice input using a microphone. 
The script then prompts the user to speak the minute of the alarm and captures their voice input. 
Finally, the script prompts the user to speak whether they want the alarm to ring at am or pm and captures their voice input.

The script then waits until the specified time and plays an alarm sound using the playsound library. 
The alarm sound is specified as an mp3 file in the code. Once the alarm goes off, the script stops running.
