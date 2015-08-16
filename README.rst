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

Troubleshooting
---------------

* Make sure to turn on access for less secure apps in the
  `Google account security setting
  <https://www.google.com/settings/security/lesssecureapps>`_
  to send notification email using python.

  https://support.google.com/accounts/answer/6010255?hl=en
