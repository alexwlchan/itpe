Release History
===============

2019.1 (release date: 2018-12-31)
---------------------------------

Now the `2018 masterlist <https://amplificathon.dreamwidth.org/3201231.html>`_
is posted, this release adds two bugfixes in anticipation of 2019, as requested
by the lovely mods:

-  You can now specify a Tumblr handle as ``tm/username``, in addition to the
   existing format.
-  Cover art won't overflow off the screen on narrow screens (i.e. phones).

2018.4 (release date: 2018-12-27)
---------------------------------

Another hotfix for Python 2 support.

2018.3 (release date: 2018-12-27)
---------------------------------

Another attempt to handle non-ASCII characters in Python 2.

2018.2 (release date: 2018-12-27)
---------------------------------

A failed release to fix a Python 2 Unicode bug.

2018.1 (release date: 2018-12-27)
---------------------------------

This is an attempt to release the code that *should* have been present
in the 2017.2 release.

2017.2 (release date: 2018-01-03)
---------------------------------

This releases fixes a bug that was found while building the 2017 masterpost:

-  Don't throw a UnicodeDecodeError if there are unusual characters in the
   input CSV.


2017.1 (release date: 2018-01-02)
---------------------------------

This releases fixes a bug that was found while building the 2017 masterpost:

-  Actually include the template ``podfic-template.html``.  This was present
   if you downloaded the repo and worked from that, but not if you installed
   through pip.

2016.0 (release date: 2017-01-01)
---------------------------------

- The first new release.  This contains a single change from 2015: the
  spreadsheets no longer include an AO3 link for the original fic, so we don't
  look for this when we generate the templates.

2015.0
------

- The last historical release, for ITPE 2015.  Smaller changes compared to 2014.

2014.0
------

- Another historical release, recording the state of the scripts used for
  ITPE 2014.  I don't remember much about these except that I rewrote the
  entire script in disgust at what I'd written for 2013.

2013.0
------

- First production release!  This is a historical release, recording the state
  of the scripts used for ITPE 2013.
