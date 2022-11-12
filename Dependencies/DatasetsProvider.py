from git import Repo, RemoteProgress
import logging
from urlextract import URLExtract




class Progress(RemoteProgress):
    def line_dropped(self, line):
        print(line)

    def update(self, *args):
        print(self._cur_line)


class DataSetsProvider:

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.__extractor = URLExtract()
        self.__gitUrlList = self.__extractor.find_urls(open(file="Resources/urls_dataset.txt").read())

    def get_datasets(self):
        print(self.__gitUrlList)
        for item in self.__gitUrlList:
            print(item)
            Repo.clone_from(
                url=item,
                to_path="../Resources",
                progress=Progress(),
            )
