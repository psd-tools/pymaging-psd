PSD support for Pymaging
========================

This module provides basic PSD support for Pymaging_.
The license is MIT.

Installation
------------

::

    pip install pymaging-psd

This module requires `psd-tools`_, packbits_ and distribute_.

.. _Pymaging: https://github.com/ojii/pymaging
.. _psd-tools: https://github.com/kmike/psd-tools
.. _packbits: http://pypi.python.org/pypi/packbits/
.. _distribute: http://pypi.python.org/pypi/distribute

Contributing
------------

Development happens at github and bitbucket:

* https://github.com/kmike/pymaging-psd
* https://bitbucket.org/kmike/pymaging-psd

The main issue tracker is at github: https://github.com/kmike/pymaging-psd/issues

Feel free to submit ideas, bugs, pull requests (git or hg) or regular patches.

Please note that pymaging-psd is a simple wrapper for `psd-tools`_ and
does almost nothing: it just registers the image format and provides
a distribute entry point. If something doesn't work, this is likely a bug in
`psd-tools`_ (or maybe in Pymaging_) and should be reported to the
appropriate bug tracker.