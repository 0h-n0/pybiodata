import requests

from .base import AbstractDatabase
from .database_urls import PDB_REST_URL, PDB_DOWNLOAD_URL


class PDB(AbstractDatabase):
    def __init__(self, parser):
        self.args = vars(parser.parse_args())

    def run(self):
        pdb_id = self.args['id']
        filename = f'{pdb_id}.pdb'
        with requests.get(PDB_DOWNLOAD_URL + f'/{filename}', stream=True) as r:
            r.raise_for_status()
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        return filename

    @classmethod
    def set_command_arguments(cls):
        parser = super().set_command_arguments()
        parser.add_argument('--id', help='set PDBID')
        return parser
