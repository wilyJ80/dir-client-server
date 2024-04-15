import Pyro5.api
import os
import base64
import hashlib

file_server = Pyro5.api.Proxy("PYRONAME:example.file")

files_dict = file_server.get_all_files()

destination_dir = './mirror-folder/'

for rel_path, file_info in files_dict.items():
    destination_file = os.path.join(destination_dir, rel_path)

    os.makedirs(os.path.dirname(destination_file), exist_ok=True)
    file_content = base64.b64decode(file_info['content'])

    with open(destination_file, 'wb') as file:
        file.write(file_content)

    received_checksum = hashlib.md5(file_content).hexdigest()

    if received_checksum == file_info['checksum']:
        print(f'{rel_path}: File transfer successful. MD5 checksum matched.')
    else:
        print(f'{rel_path}: File transfer failed. MD5 checksums do not match.')

print(f'All files saved in: {destination_dir}')
