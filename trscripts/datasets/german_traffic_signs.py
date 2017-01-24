## some code for downloading files
from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import os, struct
import array
import sys
import zipfile
from IPython.display import display, Image
from scipy import ndimage
from sklearn.linear_model import LogisticRegression
from six.moves.urllib.request import urlretrieve
from six.moves import cPickle as pickle
import scipy.io as sio

class GermanTrafficSigns:
    GERMAN_TRAFFIC_SIGNS_DOWNLOAD_URL = "https://d17h27t6h515a5.cloudfront.net/topher/2016/November/581faac4_traffic-signs-data/traffic-signs-data.zip"
    GERMAN_TRAFFIC_SIGNS_DOWNLOAD_PATH = ["..", "data"]
    GERMAN_TRAFFIC_SIGNS_DOWNLOAD_FILENAME = "german_traffic_signs.zip"

    def __init__(self):
        basepath = os.path.dirname(__file__)
        self.basepath = os.path.abspath(os.path.join(basepath, self.GERMAN_TRAFFIC_SIGNS_DOWNLOAD_PATH[0],
                                                     self.GERMAN_TRAFFIC_SIGNS_DOWNLOAD_PATH[1]))

    def download(self, force=False):
        """Download a file if not present, and make sure it's the right size."""
        path = str(os.path.abspath(os.path.join(self.basepath, self.GERMAN_TRAFFIC_SIGNS_DOWNLOAD_FILENAME)))
        if force or not os.path.exists(path):
            print('Attempting to download: %s' % str(self.GERMAN_TRAFFIC_SIGNS_DOWNLOAD_FILENAME))
            filename, _ = urlretrieve(self.GERMAN_TRAFFIC_SIGNS_DOWNLOAD_URL, os.path.abspath(os.path.join(self.basepath, self.GERMAN_TRAFFIC_SIGNS_DOWNLOAD_FILENAME)))
            print('\nDownload Complete! File saved in: %s' % str(path))
        else:
            print('File was already downloaded')

    def extract(self, force=False):
        folder = os.path.abspath(os.path.join(self.basepath, os.path.splitext(self.GERMAN_TRAFFIC_SIGNS_DOWNLOAD_FILENAME)[0]))
        zip_file = os.path.abspath(os.path.join(self.basepath, self.GERMAN_TRAFFIC_SIGNS_DOWNLOAD_FILENAME))
        if os.path.isdir(folder) and not force:
            # You may override by setting force=True.
            print('%s already present - Skipping extraction of downloaded zip.' % (folder))
        else:
            print('Extracting data for %s. This may take a while. Please wait.' % folder)
            os.makedirs(folder)

            with zipfile.ZipFile(zip_file, "r") as z:
                z.extractall(folder)
                print('Successfully extracted dataset')
        if not os.path.exists(zip_file):
            print('The dataset is missing')

    def get_data(self):
        training_filename = 'train.p'
        testing_filename = 'test.p'

        german_taffic_signs_folder = os.path.splitext(self.GERMAN_TRAFFIC_SIGNS_DOWNLOAD_FILENAME)[0]
        training_path = os.path.abspath(os.path.join(self.basepath, german_taffic_signs_folder, training_filename))
        testing_path = os.path.abspath(os.path.join(self.basepath, german_taffic_signs_folder, testing_filename))

        with open(training_path, mode='rb') as f:
            train = pickle.load(f)
        with open(testing_path, mode='rb') as f:
            test = pickle.load(f)

        X_train, y_train = train['features'], train['labels']
        X_test, y_test = test['features'], test['labels']
        return X_train, y_train, X_test, y_test