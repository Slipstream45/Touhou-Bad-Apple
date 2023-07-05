#This is just the rendering with no sound. Go to bad_apple.py for both!
#TODO: experiment with other methods
import moviepy.editor as mp
import numpy as np
import cv2

#Path to the input video file
video_path = 'bad_apple_fps60.mp4'

#Resize dimensions for the ASCII animation
#Size down when running sound cause of sync issues
WIDTH = 120
HEIGHT = 80

#ASCII characters for the animation (customize as desired) but not recommended!
ASCII_CHARS = '@#S%?*+;:, '

#Calculate the number of intensity levels
num_levels = len(ASCII_CHARS)

#Load the video file
video = mp.VideoFileClip(video_path)

#Resize the video to fit the terminal dimensions
video_resized = video.resize((WIDTH, HEIGHT))

for frame in video_resized.iter_frames(fps=video.fps):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    resized_frame = cv2.resize(gray_frame, (WIDTH, HEIGHT))

    ascii_frame = ''
    for row in resized_frame:
        for pixel in row:
            # Calculate the intensity level
            intensity = int(pixel / 255 * num_levels)

            # Ensure the intensity is within the valid range
            if intensity >= num_levels:
                intensity = num_levels - 1

            # Append the corresponding ASCII character
            ascii_frame += ASCII_CHARS[intensity]

        ascii_frame += '\n'
    #ANSI for clearing terminal
    print('\033[H\033[J' + ascii_frame)
