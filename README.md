# Umami Uploader

Scripts for uploading visit info to umami based on haproxy logs.

## Configuration

Create `config.json` based on `config.json.example`.
The logfile should be a tsv in the following format:
```
url user-agent  timestamp   ip-address
```
## Running
 
```
python3 main.py
```