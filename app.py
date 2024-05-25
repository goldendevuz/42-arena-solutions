import os
import re
import sys

from slugify import slugify

pattern = r'\]\(.*?\)'

# List to hold matching texts
matching_texts = []
data = {}


def slugify_path1(text):
    new_path = []
    new_name = text.replace("#", "-sharp")
    splitted_path = new_name.split('/')
    for item in splitted_path:
        item = item.split()
        for slice in item:
            if len(slice) == 32:
                item.remove(slice)
        item = slugify('-'.join(item))
        new_path.append(item)
    new_path = '/'.join(new_path)
    print(new_path)
    return new_path


def slugify_path2(text):
    new_path = []
    new_name = text[:-3] #.replace("#", "-sharp")
    new_name = new_name.replace("-md", "")
    splitted_path = new_name.split('/')
    for item in splitted_path:
        item = item.split('%20')
        for slice in item:
            if len(slice) == 32:
                item.remove(slice)
        item = slugify('-'.join(item))
        new_path.append(item)
    new_path = '/'.join(new_path) + '.md'
    print(new_path)
    return new_path


def find_content(file_name):
    with open(file_name) as f:
        file_content = f.read()
    # Find all matches in the file content
    matches = re.findall(pattern, file_content)
    if matches:
        matching_texts.extend(matches)
    for text in matching_texts:
        if 'http://' not in text and 'https://' not in text:
            if text.endswith('.md)'):
                value = text[2:-1]
                data[text] = slugify_path2(value)


def update_content(file_path):
    with open(file_path) as f:
        file_content = f.read()

    for key, value in data.items():
        file_content = file_content.replace(key[2:-1], value)

    with open(file_path, 'w') as f:
        f.write(file_content)


def rename_items(directory):
    next_directories = []
    for item in os.listdir(directory):
        old_name = item
        old_path = os.path.join(directory, item)
        new_name = old_path.replace(".md", "")
        new_name = slugify_path1(new_name)
        if item.endswith('.md'):
            new_name += '.md'
            find_content(old_path)
            update_content(old_path)
        new_path = new_name
        try:
            os.rename(old_path, new_path)
        except Exception as e:
            with open("issues.log", 'a') as f:
                f.write(f"{e}\n")
        if os.path.isdir(new_path):
            next_directories.append(new_name)
    for renamed_directory in next_directories:
        rename_items(renamed_directory)
        # print(f"Renamed to {renamed_directory}")
    return


if __name__ == "__main__":
    docs_directory = "docs"
    rename_items(docs_directory)
