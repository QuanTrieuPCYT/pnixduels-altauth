# pnixduels-altauth
Alternate authentication server for PhoenixDuels in case the API of them went down. All reponses are all valid, with the expiry date of 31th December 2099.

The script is designed to restart at the 30th minute of every hour. Pair this with a service manager, for example `systemd`, for 24/7 operation.

## Running the script
Assuming you're on Linux/macOS/Windows. Make sure you have latest `python3` with `python-pip` installed

```
cd pnixduels-altauth
pip install -r requirements.txt
python3 main.py

# The script will exit at the 30th of every hour. For continuous operation please kindly edit the source code or pair with a service manager.
```
