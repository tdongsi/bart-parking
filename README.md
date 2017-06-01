## bart-parking
Automated downloading [BART](https://www.bart.gov/) parking permits.

### Requirements

* Install `requests` [package](http://docs.python-requests.org/en/master/user/install). Usually, it is simply `pip install requests`.

### Background

Before having the Monthly Parking Permit, we usually have no choice but Daily Parking Permits for BART commutes.
We will often end up having to download multiple PDF files for the daily permits and print them to put on our vehicle's dashboard.
The [BART reservation website](https://www.select-a-spot.com/bart/) offers no easy way to download all of PDF files in one click (see the screenshot).
We will have to click "Print Permit" button one by one, each opens up a dialog to navigate through with quite a few clicks, before we can download the PDF file.

![BART Screenshot](BART.jpg?raw=true "Screenshot")

Personally, the BART commute itself is not that bad. 
But it is really painful to download every ... single ... PDF ... permit manually before printing them.

### How to run

Run the `main.py` script and input your username and password, as shown below.

```
C:\Github\bart-parking\bart>python main.py
bart-view   : INFO     Please input your username and password.
Username:YOUR_USERNAME
Password:
bart-view   : INFO     Done reading username and password
requests.packages.urllib3.connectionpool: INFO     Starting new HTTPS connection (1): www.select-a-spot.com
bart        : INFO     Login Response: https://www.select-a-spot.com/bart/users/login/ 302
bart        : INFO     Created folder to save permit PDF files.
bart        : INFO     Finished downloading permit 1183167.
bart        : INFO     Finished downloading permit 1183161.
bart        : INFO     Finished downloading permit 1183136.
bart        : INFO     Finished downloading permit 1180762.
bart        : INFO     Finished downloading permit 1177938.
bart        : INFO     Finished downloading permit 1177937.
bart        : INFO     Finished downloading permit 1177935.
bart        : INFO     Finished downloading permit 1177929.

C:\Github\bart-parking\bart>
```
