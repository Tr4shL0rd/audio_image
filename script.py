"""reads a list of audio frequencies and maps it to rgb values that outputs an image"""
from PIL import Image
import helper

WIDTH,HEIGHT = 1000,1000

def create_gray_scale_audio_image(audio_file_path:str):
    """
    takes an audio file and outputs a PNG image that visualizes the frequencies

    PARAMS:
    -------
    * audio_file_path `str`: path to the audio file
    """

    freq_list = helper.get_frequencies(audio_file_path)


    img = Image.new("L", (WIDTH,HEIGHT), color=255)
    samples_per_col = len(freq_list)//WIDTH

    for x in range(WIDTH):
        start_idx = x * samples_per_col
        end_idx = start_idx + samples_per_col

        avg_freq = sum(freq_list[start_idx:end_idx]) / samples_per_col
        gray_value = int((avg_freq / 32767) * 255)

        for y in range(HEIGHT):
            img.putpixel((x,y), gray_value)

    img.save(f"{audio_file_path.split('.')[0]}_gray_scale_image.png")

def create_rgb_audio_image(audio_file_path:str):
    """
    takes an audio file and outputs a PNG image that visualizes the frequencies

    PARAMS:
    -------
    * audio_file_path `str`: path to the audio file
    """

    freq_list = helper.get_frequencies(audio_file_path)

    img = Image.new("RGB", (WIDTH,HEIGHT), color=(0,0,0))
    samples_per_col = len(freq_list) // (WIDTH*3)

    for x in range(WIDTH):
        start_idx = x * samples_per_col*3
        end_idx = start_idx + samples_per_col*3
        freq_samples =  freq_list[start_idx:end_idx:3]

        red   = sum(freq_samples) / samples_per_col
        green = sum(freq_samples[start_idx+1:end_idx:3]) / samples_per_col
        blue  = sum(freq_samples[start_idx+2:end_idx:3]) / samples_per_col


        red_value = int((red / 32767) * 255)
        green_value = int((green / 32767) * 255)
        blue_value = int((blue / 32767) * 255)
        for y in range(HEIGHT):
            img.putpixel((x,y), (red_value,blue_value,green_value))
    img.save(f"{audio_file_path.split('.')[0]}_rgb_image.png")


def create_rgb_intense(audio_file_path:str):
    """
    takes an audio file and outputs a PNG image that visualizes the frequencies

    PARAMS:
    -------
    * audio_file_path `str`: path to the audio file
    """
    freq_list = helper.get_frequencies(audio_file_path)
    img = Image.new("RGB", (WIDTH, HEIGHT), color=(0, 0, 0))

    # Calculate the number of frequency samples per column
    samples_per_col = len(freq_list) // (3 * WIDTH)

    # Loop over each pixel column in the image
    for x in range(WIDTH):
        # Calculate the frequency sample indices for this column
        start_idx = 3 * x * samples_per_col
        end_idx = start_idx + 3 * samples_per_col
        
        # Get the average frequency values for this column
        avg_freq_r = sum(freq_list[start_idx:end_idx:3]) / samples_per_col
        avg_freq_g = sum(freq_list[start_idx+1:end_idx:3]) / samples_per_col
        avg_freq_b = sum(freq_list[start_idx+2:end_idx:3]) / samples_per_col
        
        # Scale the frequency values to increase intensity
        scale_factor = 2.5
        avg_freq_r *= scale_factor
        avg_freq_g *= scale_factor
        avg_freq_b *= scale_factor
        
        # Map the frequency values to RGB values between 0 and 255
        r = int((avg_freq_r / 32767) * 255)
        g = int((avg_freq_g / 32767) * 255)
        b = int((avg_freq_b / 32767) * 255)
        
        # Set the pixel value for each pixel in this column to the RGB value
        for y in range(HEIGHT):
            img.putpixel((x, y), (r, g, b))

    # Save the image to disk
    img.save(f"{audio_file_path.split('.')[0]}_intense_rgb_image.png")
    

print("gray scale")
create_gray_scale_audio_image("misa_misa.mp3")
create_gray_scale_audio_image("audio.mp3")
print("RGB")
create_rgb_audio_image("misa_misa.mp3")
create_rgb_audio_image("audio.mp3")
print("intense RGB")
create_rgb_intense("misa_misa.mp3")
create_rgb_intense("audio.mp3")
