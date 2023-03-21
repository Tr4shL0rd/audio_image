"""Helper module"""
from pydub import AudioSegment
from typing import List

def remove_items(lst:list, items:list=None) -> List:
    """
    removes all occurences of item

    PARAMS:
    -------
    * lst `list`: list to operate on
    * item `any`: items to remove
    """
    if not isinstance(items, list):
        items = []
    # using list comprehension to perform the task
    res = [i for i in lst if i not in items]
    return res

def get_frequencies(audio_file_path) -> List:
    """
    returns a list of frequencies

    PARAMS:
    * audio_file_path `str`: path to audio file
    """

    audio_file = AudioSegment.from_file(audio_file_path)
    freqs = list(audio_file.get_array_of_samples())

    freq_list = remove_items(freqs, [-1,0,1])
    return freq_list