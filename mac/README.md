# OSx

## Package requirements for Mac

* [Cryptography](https://pypi.org/project/cryptography/)
* [Selenium](https://pypi.org/project/selenium/)

## Macintosh Specific Instructions and Troubleshooting

### Enable safari automation

Safari’s [WebDriver](https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari) support for developers is turned off by default. How you enable it depends on your operating system.

High Sierra and later:

Run `safaridriver --enable` once. (If you’re upgrading from a previous macOS release, you may need to use sudo.)

Sierra and earlier:

If you haven’t already done so, make the Develop menu available. Choose Safari > Preferences, and on the Advanced tab, select “Show Develop menu in menu bar.” For details, see Safari Help.

Choose Develop > Allow Remote Automation.

Authorize safaridriver to launch the XPC service that hosts the local web server. To permit this, manually run /usr/bin/safaridriver once and follow the authentication prompt.

> Note: Python 3.10.3 is the latest version of Python 3 that is supported by Selenium. If you have a newer version of Python 3 installed, you will need to install Python 3.7.3.

### Tips and further improvments:

* Optimize the wait login wait time according to your specific needs.

* We will roll out a feature to automatically optimise the wait time for relogin based on logs.

* 
