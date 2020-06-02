import os
import re

images = set()
images_without_version = set()


def search_image(line, pattern):
    if '$' not in line:
        m = re.search(pattern, line)
        if m is not None:
            return m.group(1)
    return None


def read_yaml(file_path):
    if file_path[-4:] != "yaml":
        return

    with open(file_path) as file:

        for line in file:
            image_address = search_image(line, '(gcr.io[a-zA-Z0-9/\-:\._]*)')
            if image_address is not None:
                # print("This file has image: {} ".format(file_path))
                # print("The image is : {}".format(image_address))
                if ':' in image_address:
                    images.add(image_address)
                else:
                    images_without_version.add(image_address)


def scan_folder(folder):
    g = os.walk(folder)

    for path, dir_list, file_list in g:
        for file_name in file_list:
            read_yaml(os.path.join(path, file_name))

    #  just print
    for address in images:
        print(address)
    print("==================")
    for address in images_without_version:
        print(address)


scan_folder("/opt/my-kubeflow")
