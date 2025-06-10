# EdgeFucker
Bring user's rights back
if you are annoyed by this unwanted default browser and want to switch to chrome instead, this is your last shelter.

## Usage
- download the release.
- extract into a folder.
- copy the msedge.exe from dist/ folder and put it inside "C:\Program Files (x86)\Microsoft\Edge\Application"  
- enjoy your lovely chrome.
-ps. add the binary to your antivirus exceptions, if you have problems disable windows defender before extraction.

## Build
- clone the repo
- `cd EdgeFucker`
- `pip install pywin32 pyinstaller`
- `pyinstaller --onefile --noconsole --name msedge edge_fucker.py`
- copy the msedge.exe from dist/ folder and put it inside "C:\Program Files (x86)\Microsoft\Edge\Application"  

## todo:
- ability to change chrome path
- ability to use firefox, etc.