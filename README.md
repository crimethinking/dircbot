# dircbot
A simple Python IRC bot

## Features
* Greet when an user joins chat. (screenshot)
* Reply "pong" to "ping". (screenshot)
* Randomly send out quotes from a quote database. (screenshot)
	* Support Unicode for ultimate international quoting experience. (screenshot)

## Requirement
* Python 3.4.x

## Getting Started
* Set up necessary parameters such as nickname, chat server and channel in the configuration part of dircbot.py. dircbot's source code, and particularly the configuration section, is carefully commented to assist user. (screenshot)
* Run straight from Python CLI REPL: `python dircbot.py` or from inside IDLE.

## Design Architecture
* **Modular:** subroutines are written as modules to be imported. When needed, new modules can be written, imported, and triggered through conditional statements.
* **Multithreaded:** allow bot to be responsive to multiple I/O requests.

## Testing
* All functions OK on personal workstations with Python 3.4.3:
	* Windows XP x86
	* Windows 7 x64
	* Debian 8
	* Fedora 21

* Currently running 24/7 from inside a Docker container on a CoreOS Microsoft Azure instance, servicing my private IRC channel.

* **Test parameters:**
  * `!about` in chat to test the about function.
	* Send a message with content `ping` or `PING` to see the bot reply `pong` or `PONG` accordingly.
	* Change the Boolean variable `debug` in `dircbot.py` to turn on/off debug mode, which prints out buffer content for debugging purpose.
	* Change the variable `min_interval` and `max_interval` in `dircbot.py` to set the interval time between quotes.
	+ Change the variable `filename` to `utf8_test.txt` (bundled globalization test database) to test the bot's Unicode support.

## Limitations:
* Naive chat parsing that can cause glitches with some functions (see known issues).
* Does not support secure connection to IRC server.
* Does not support Simple Authentication and Security Layer (SASL) for authentication with server.


## Revision to original design
* Refactorized subroutine code into modules.
* Added multithreading.

## Known issues:
* Ctrl+C does not work on Windows command prompt, but fine on UNIX systems. This is a Windows issue as it is not compliant with UNIX interrupt signals, which Python uses.
* Interrupts are not gracefully handled due to the use of multithreading.
* Naive chat parsing causing bot to send a welcome message when it joins the channel.
* Right-to-left languages are currently written as left-to-right.

## License
dircbot is released under The Unlicense. See [UNLICENSE](UNLICENSE) for the full license text.


## Author
dircbot was created by Duy Nguyen as a final project for CS128 class by Dr. Victor Lee, John Carroll University.
