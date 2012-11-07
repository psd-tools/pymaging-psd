# -*- coding: utf-8 -*-
from __future__ import absolute_import

import psd_tools
from pymaging.formats import Format
from pymaging.exceptions import FormatNotSupported

def decode(fileobj):
    psd = psd_tools.PSDImage.from_stream(fileobj)
    return psd.as_pymaging()

def encode(image, fileobj):
    raise FormatNotSupported('psd')

PSD = Format(decode, encode, ['psd'])