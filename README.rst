JAL Ticket Price Checker
========================

This script checks the availability of low price one-way JAL tickets
from Taipei to Boston.
An email notification is sent out once the price falls below
the specified threshold.

Requirement
-----------

* `Python 2.7 <http://www.python.org/download/>`_
* `Google Chrome <http://www.google.com/chrome/>`_
* `Selenium Python bindings <https://pypi.python.org/pypi/selenium>`_
* `ChromeDriver <https://code.google.com/p/selenium/wiki/ChromeDriver>`_

Command-line Options
--------------------

Several options are available using the command line::

   usage: jal_price.py [-h] [-m GMAIL_ACCOUNT] [-t TO_ADDR]

   optional arguments:
     -h, --help        show this help message and exit
     -m GMAIL_ACCOUNT  gmail account
                       (won't send notification if not specified)
     -t TO_ADDR        comma separated email addresses to send notification to
                       (send to GMAIL_ACCOUNT if not specified)

Troubleshooting
---------------

* Make sure to turn on access for less secure apps in the
  `Google account security setting
  <https://www.google.com/settings/security/lesssecureapps>`_
  to send notification email using python.

  https://support.google.com/accounts/answer/6010255?hl=en
