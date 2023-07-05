import moviepy.editor as mp
import numpy as np
import cv2
from playsound import playsound

#Path to the input video file
video_path = 'bad_apple_fps60.mp4'

#Path to the audio file (MP3 format)
audio_path = 'bad_apple.mp3'

#Extract the width and height values
#Cannot go full screen :(
WIDTH = 80
HEIGHT = 40

#ASCII characters for the animation (customize as desired) but not recommended!!
ASCII_CHARS = '@#S%?*+;:, '

#intensity levels
num_levels = len(ASCII_CHARS)

#Load the video file
video = mp.VideoFileClip(video_path)

#fit the terminal dimensions (this is not working but breaks on run so I kept it here :))
video_resized = video.resize((WIDTH, HEIGHT))

#audio file
playsound(audio_path, block=False)
for frame in video_resized.iter_frames(fps=video.fps):
    #Convert the frame to grayscale EZ 
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    #Resize the frame to fit the terminal dimensions
    resized_frame = cv2.resize(gray_frame, (WIDTH, HEIGHT))

    #ASCII mapping (restrict bounds to just the ASCII chars we have) 
    #TODO: can this be more good?
    ascii_frame = ''
    for row in resized_frame:
        for pixel in row:
            #Calculate the intensity level
            intensity = int(pixel / 255 * num_levels)

            #Ensure the intensity is within the valid range
            if intensity >= num_levels:
                intensity = num_levels - 1

            #Append the corresponding ASCII character
            ascii_frame += ASCII_CHARS[intensity]

        ascii_frame += '\n'

    #Clear the terminal and print the ASCII frame
    #(\033[H\033[J) is escape code in ANSI to clear terminal
    print('\033[H\033[J' + ascii_frame)

