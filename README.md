# dircbot
A simple Python IRC bot

## Features
* Greet when an user joins chat
  
  ![](http://i.imgur.com/hdC1X9g.png)

* Reply "pong" to "ping"

  ![](http://i.imgur.com/yiAQTVb.png)

* Randomly send out quotes from a quote database

  ![](http://i.imgur.com/Sx5EgXc.png)

	* Support Unicode for ultimate international quoting experience

    ![](http://i.imgur.com/Q7H59ez.png)

## Requirement
* Python 3.4.x

## Getting Started
* Set up necessary parameters such as nickname, chat server and channel in the configuration part of dircbot.py. dircbot's source code, and particularly the configuration section, is carefully commented to assist user. (screenshot)

  ![](http://i.imgur.com/EiXsQPA.png)

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

	* Change the variable `filename` to `utf8_test.txt` (bundled globalization test database) to test the bot's Unicode support.

## Limitations
* Naive chat parsing that can cause glitches with some functions (see known issues).
* Does not support secure connection to IRC server.
* Does not support Simple Authentication and Security Layer (SASL) for authentication with server.

## Revision to original design
* Refactorized subroutine code into modules.
* Added multithreading.

## Known issues
* Ctrl+C does not work on Windows command prompt, but fine on UNIX systems. This is a Windows issue as it is not compliant with UNIX interrupt signals, which Python uses.
* Interrupts are not gracefully handled due to the use of multithreading.
* Naive chat parsing causing bot to send a welcome message when it joins the channel.
* Right-to-left languages are currently written as left-to-right.

## License
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>

## Author
dircbot was created by Duy Nguyen as a final project for CS128 class by Dr. Victor Lee, John Carroll University.
