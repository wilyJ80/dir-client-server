import Pyro5.api
import os
import base64
import hashlib
import time

file_server = Pyro5.api.Proxy("PYRONAME:example.file")

destination_dir = './mirror-folder/'


def sync_files():
    try:
        files_dict = file_server.get_all_files()
    except Exception as e:
        print(f"Error retrieving files: {e}")
        files_dict = {}

    for rel_path, file_info in files_dict.items():
        destination_file = os.path.join(destination_dir, rel_path)

        os.makedirs(os.path.dirname(destination_file), exist_ok=True)
        file_content = base64.b64decode(file_info['content'])

        try:
            with open(destination_file, 'wb') as file:
                file.write(file_content)
        except Exception as e:
            print(f"Error writing file {rel_path}: {e}")
            continue

        received_checksum = hashlib.md5(file_content).hexdigest()

        if received_checksum == file_info['checksum']:
            print(f'{rel_path}: File sync successful. MD5 checksums match.')
        else:
            print(f'{rel_path}: File sync failed. MD5 checksums do not match.')

    print(f'All files saved in: {destination_dir}')


# Run the synchronization loop
try:
    while True:
        sync_files()
        # Add a delay before syncing again (e.g., every 5 seconds)
        time.sleep(5)
except KeyboardInterrupt:
    print("Ctrl+C detected. Exiting gracefully...")
