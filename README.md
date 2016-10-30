## bart-parking
Automate downloading BART parking permits.

### Requirements

* Install `requests` [package](http://docs.python-requests.org/en/master/user/install). Usually, it is `pip install requests`.

### Background

Before having the Monthly Parking Permit, you usually have no choice but Daily Parking Permits (DPP).
You will often end up having to download multiple PDF files for the DPPs and print them to put on the dashboard.
The BART website offers no easy way to do so (see the screenshot).

{% img center BART.jpg %}

The BART commute itself is not that bad, especially when you usually find a seat. 
But it is painful to download every ... single ... PDF ... permit and print it.

### How to run

Run the `main.py` script and input username and password as shown below.

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