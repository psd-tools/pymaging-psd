# -*- coding: utf-8 -*-
from __future__ import absolute_import

import psd_tools
from pymaging.formats import Format

def decode(fileobj):
    psd = psd_tools.PSDImage.from_stream(fileobj)
    return psd.as_pymaging()

def encode(image, fileobj):
    raise NotImplementedError("Saving to PSD is not supported")

PSD = Format(decode, encode, ['psd'])