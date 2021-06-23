
from os import error


class File:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_file_ext(file: str) -> str:
        """ get file extension """
        
        if not '.' in file:
            return file
        
        parts = file.split('.')
        return parts[len(parts) - 1]

    @staticmethod
    def read_file_content(path: str) -> str:
        """ read file content """
        return open(path, errors='ignore', encoding='utf-8').read()
