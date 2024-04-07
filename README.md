# Setup and run nameserver (easy way - Debian/Ubuntu)

`chmod +x setup.sh`

`source setup.sh`

# Others

`pip install -r requirements.txt`

- Make directories ./source-folder and 
./mirror-folder

- Open nameserver
`pyro5-ns`

# All

- Populate ./source-folder with desired files for mirroring.

- Run server in another shell instance: `python3 server.py`

- Run client in another shell instance: `python3 client.py`