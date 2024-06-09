import os
import regex

def separate_files(files: list[str], regex_pattern: str) -> dict[str, list[str]]:
    batches = {}
    for file in files:
        directory = regex.search(pattern=regex.compile(pattern=regex_pattern), string=file).group(1)
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
    return json_files