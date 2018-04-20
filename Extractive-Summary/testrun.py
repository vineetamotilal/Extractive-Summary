#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 01:29:32 2018

@author: vineeta
"""

import testrun
from glob import glob

paths = glob('test/*.testrun')

for file in paths:
	testrun.testfile(file)