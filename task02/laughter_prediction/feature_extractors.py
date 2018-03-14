import librosa
import numpy as np
import pandas as pd


class FeatureExtractor:
    def extract_features(self, frames, rate):
        """
        Extracts features for classification ny frames for audio frames

        :param frames
        :return: pandas.DataFrame with features of shape (n_chunks, n_features)
        """

        df = pd.DataFrame([self._extract_features(frame, rate) for frame in frames], dtype=np.float)
        df.columns = [f'FBANK{i}' for i in range(1, df.shape[1] - 12)] + [f'MFCC{i}' for i in range(1, 14)]
        return df

    @staticmethod
    def _extract_features(frame, rate):
        S = librosa.feature.melspectrogram(frame, rate).mean(axis=1)
        log_S = librosa.power_to_db(S, ref=np.max)
        mfcc = librosa.feature.mfcc(S=log_S, n_mfcc=13)
        return np.concatenate((log_S, mfcc))
