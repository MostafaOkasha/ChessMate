#!/usr/local/bin/python3

import cv2
import numpy as np
import math
import time
import boto3
import os
import PIL
import glob
import subprocess
from IPython import embed
import sys
from pprint import pprint
import botocore
from shutil import copyfile


img = cv2.imread('/Desktop/CAPSTONE_R/chess-irs/pictures/processed_states/2019-03-25-01:34:12.041180:raw_state.jpg')


fgbg = cv2.createBackgroundSubtractorMOG(128,cv2.THRESH_BINARY,1)
masked_image = fgbg.apply(img)
masked_image[masked_image==127]=0
cv2.imShow(masked_image)




