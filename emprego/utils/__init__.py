import os
import regex

sorting_regex = regex.compile(pattern=r'_(\d+)\.')

def separate_files(files: list[str], compiled_regex: str) -> dict[str, list[str]]:
    batches = {}
    for file in files:
        directory = regex.search(pattern=compiled_regex, string=file).group(1)
        if directory not in batches:
            batches[directory] = [file]
        else:
            batches[directory].append(file)
    return batches

def find_files(root_dir: str, file_extension: str) -> list[str]:
    json_files = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(file_extension):
                json_files.append(os.path.join(root, file))
    json_files.sort(key=lambda x: int(regex.search(pattern=sorting_regex, string=x).group(1)))
    return json_files