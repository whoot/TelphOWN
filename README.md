TelphOWN
========

TelphOWN is a proof-of-concept/penetration testing tool that exploits some vulnerabilities in [Telpho10](http://www.telpho.de).

Telpho10 is a german "Hybrid ISDN / VoIP Telefonanlage" (telephone system) which I hacked for fun.

And seriously, Telpho10 (v2.6.31) is absolutely broken and one of the finest examples of how NOT to code applications.

Tipp:
	Hack it yourself to test/train your skills or just for fun and you will find a lot of vulnerabilities which are easy to exploit.

Since MITRE/CVE decided to cover only [software used most by enterprises](https://cve.mitre.org/cve/data_sources_product_coverage.html),
no CVE number could be assigned for the vulnerabilities found by me.

However, I have notified the team of Telpho10 about the vulnerabilities and they will fix them (hopefully) in the next release.

Exploits
----

TelphOWN can exploit following vulnerabilties:

	* Dumping all kind of Credentials
	* Reboot/Shutdown Server
	* Restart Apache
	* Upload a Webshell

For the upload of a webshell, valid credentials are needed, so you first need to dump the credentials.
If no credentials are provided, TelphOWN will try the default credentails.

Installation
----

You can download the latest tarball by clicking [here](https://github.com/whoot/TelphOWN/tarball/master) or latest zipball by clicking [here](https://github.com/whoot/TelphOWN/zipball/master).

Preferably, you can download TelphOWN by cloning the [Git](https://github.com/whoot/TelphOWN) repository:

    git clone https://github.com/whoot/TelphOWN.git

TelphOWN works with [Python](http://www.python.org/download/) version **3.x** on Debian/Ubuntu, RedHat and Windows platforms.

You might need to install following packages:

* [Requests](https://pypi.python.org/pypi/requests/)
* [Requests-toolbelt](https://pypi.python.org/pypi/requests-toolbelt)

On Debian/Ubuntu you can install the packages with apt-get:

	apt-get install python3-requests python3-requests-toolbelt

On Redhat you can install all needed packages with easy_install:

	easy_install argparse
	easy_install requests
	easy_install requests-toolbelt

Usage
----

To get a list of all options use:

    python3 TelphOWN.py -h

Example:
Dump credentials from Telpho10 system on 192.168.0.139:

	python3 TelphOWN.py -d 192.168.0.139 --dump

Bug Reporting
----
Bug reports are welcome! Please report all bugs on the [issue tracker](https://github.com/whoot/TelphOWN/issues).

Links
----

* Download: [.tar.gz](https://github.com/whoot/TelphOWN/tarball/master) or [.zip](https://github.com/whoot/TelphOWN/archive/master.zip)
* Changelog: [Here](https://github.com/whoot/TelphOWN/blob/master/doc/CHANGELOG.md)
* TODO: [Here](https://github.com/whoot/TelphOWN/blob/master/doc/TODO.md)
* Issue tracker: [Here](https://github.com/whoot/TelphOWN/issues)

# License

TelphOWN - Telpho10 Ownage Tool

Copyright (c) 2016 Jan Rude

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see [http://www.gnu.org/licenses/](http://www.gnu.org/licenses/)