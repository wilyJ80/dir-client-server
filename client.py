import Pyro5.api
import os
import base64

file_server = Pyro5.api.Proxy("PYRONAME:example.file")

files_dict = file_server.get_all_files()

destination_dir = './mirror-folder/'

for rel_path, content in files_dict.items():
    destination_file = os.path.join(destination_dir, rel_path)

    os.makedirs(os.path.dirname(destination_file), exist_ok=True)
    with open(destination_file, 'wb') as file:
        file.write(base64.b64decode(content))

print(f'All files saved in: {destination_dir}')
