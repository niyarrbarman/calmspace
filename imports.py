import tensorflow as tf
import speech_recognition as sr
import numpy as np
from tensorflow import keras
from tensorflow.python.keras.engine import data_adapter
from tensorflow.python.eager import backprop
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras import models
from flask import Flask,render_template, request, redirect, url_for, flash
from pred_utils import *
import seaborn as sns
import matplotlib.pyplot as plt
import os
import shutil
from PIL import Image
import moviepy.editor as moviepy

def main():
    pass
