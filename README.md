# Umami Uploader

Scripts for uploading visit info to umami extracted from haproxy logs.

## Configuration

Create `config.json` based on `config.json.example`.

The logfile should be a tsv file in the following format:
```
url user-agent  timestamp   ip-address
```
To create this logfile from a haproxy log, you can run
```bash
gawk -v OFS='\t' \
  'match($0, \
  /\{((https:\/\/mores-horizon\.eu\/)|(https:\/\/mores-horizon\.github\.io\/)|(https:\/\/morespulsedemo\.poltextlab\.com\/))\|(umami\.dsd\.sztaki\.hu)\|(.*)\}/, headers) \
  {print headers[1], headers[6], $1, $4}' \
  path/to/haproxy/log \
  > path/to/output/logfile
```
Modify the regex according to your needs.
This example matches the part of a haproxy log that looks like this:
```
{referrer|host|user-agent}
```
In the example, the referrer can be one of multiple different URLs and host is the domain name of the umami instance

## Running

```
python3 main.py
```