import numpy as np
import pandas as pd
import scipy.io.wavfile as wav


def sample_by_frames(values, frame_size, shift):
    last = (len(values) - frame_size + shift) // shift * shift
    return np.array([np.array(values[i: i + frame_size]) for i in range(0, last, shift)])


def sample_audio_by_frames(audio, frame_size):
    """
    Samples audio by chunks of fixed size

    :param audio: array-like, representation of raw audio
    :param frame_size: int, number of frames per chunk
    :return: Pandas DataFrame, each chunk represented by row
    """

    return pd.DataFrame(sample_by_frames(audio, frame_size, 3 * frame_size // 4), dtype=np.float)


def sample_wav_by_time(wav_path, frame_sec):
    """
    Samples audio by chunks of fixed time

    :param wav_path: path to wav file to sample
    :param frame_sec: int, length of each chunk in seconds
    :return: Pandas DataFrame, each chunk represented by row
    """

    rate, audio = wav.read(wav_path)
    frame_size = int(rate * frame_sec)
    return sample_audio_by_frames(audio, frame_size)
