#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on November 9 2018
@author: Juliette MILLET
Example of script to create csv file with numpy arrays in it to stock 
mfccs if you do not want to use kaldi and if you do not want to apply vtln
Note: the numpy array produced are of the form: feature Time x dim
"""
import numpy as np
import librosa
import os
import scipy.io.wavfile as wav
import sys
#from mfccs import mfcc

def extract_features(path_to_wavs, feat_func, path_to_save):
    """
    Function to extract features from wavs in path_to_wavs
    :param path_to_wavs: path to find the wav files
    :param feat_func: feat spectral function
    :param path_to_save: path to save the .csv files with features in it
    :return: None
    """
    for root, dirs, files in os.walk(path_to_wavs):
        len_total = len(files)
        count = 0
        for filename in files:
            #print filename
            count += 1
            if count%100 == 0:
                print(count, "files done on", len_total)
            if not filename.endswith('.wav'):
                continue
            #print(filename)
            full_name = '/' + os.path.join(root.lstrip('./'), filename)
            fs, waveform = wav.read(full_name)
            print(fs)
            waveform = waveform.astype(float)
            print(filename, waveform.shape)
            if feat_func == 'mfccs':
                feat = librosa.feature.mfcc(y=waveform, sr=fs, S=None, n_mfcc=13, fmin = 0, fmax = 8000) 
                feat = np.swapaxes(feat, 0, 1)

            np.savetxt( path_to_save + '/' + filename[:len(filename) - 3] + 'csv', feat, delimiter=',')

if __name__ == "__main__":
    feature_wanted = sys.argv[1]
    path_wav = sys.argv[2]
    path_save = sys.argv[3]
    if feature_wanted == 'mfccs':
        feature_func = "mfccs"
    else:
        print('features unavailable')

    extract_features(path_wav, feature_func, path_save)




