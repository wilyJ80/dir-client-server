# Setup and run nameserver (easy way - Debian/Ubuntu)

`chmod +x setup.sh`

`source setup.sh`

# Others

`python3 -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

- Make directories ./source-folder and 
./mirror-folder

- Open nameserver
`pyro5-ns`

# All

- Populate ./source-folder with desired files for mirroring.

- Run server in another shell instance with venv activated: `python3 server.py`

- Run client in another shell instance with venv activated: `python3 client.py`

- Mirrored files will be on ./mirror-folder