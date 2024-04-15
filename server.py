import Pyro5.api
import os
import base64
import hashlib


@Pyro5.api.expose
class ServeFile(object):
    def __init__(self, root_folder='./source-folder/'):
        self.root_folder = root_folder

    def _get_files_recursively(self, path):
        files_dict = {}
        for root, _, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, self.root_folder)
                try:
                    with open(full_path, 'rb') as f:
                        file_content = f.read()
                except Exception as e:
                    print(f"Error reading file {rel_path}: {e}")
                    continue

                files_dict[rel_path] = {
                    'content': base64.b64encode(file_content).decode('utf-8'),
                    'checksum': hashlib.md5(file_content).hexdigest()
                }
        return files_dict

    def get_all_files(self):
        try:
            return self._get_files_recursively(self.root_folder)
        except Exception as e:
            print(f"Error retrieving files: {e}")
            return {}


daemon = Pyro5.server.Daemon()
ns = Pyro5.api.locate_ns()
uri = daemon.register(ServeFile)
ns.register("example.file", uri)

print("Ready.")
daemon.requestLoop()
