import Pyro5.api
import os
import base64


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
                with open(full_path, 'rb') as f:
                    files_dict[rel_path] = base64.b64encode(
                        f.read()).decode('utf-8')

        return files_dict

    def get_all_files(self):
        return self._get_files_recursively(self.root_folder)


daemon = Pyro5.server.Daemon()
ns = Pyro5.api.locate_ns()
uri = daemon.register(ServeFile)
ns.register("example.file", uri)

print("Ready.")
daemon.requestLoop()
