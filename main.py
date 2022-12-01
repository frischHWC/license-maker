
import logging
import os
import argparse
import shutil


def main():
    parser = argparse.ArgumentParser(description='Set up an Apache LICENSE project for a non-licensed project',
                                     epilog="This program is intent to help developer's life." +
                                            "It comes with no warranty, always SAVE & BACKUP your files before")
    # Required arguments
    parser.add_argument('--folder', required=True, type=str,
                        help="Absolute path of the folder where to apply license")

    args = parser.parse_args()

    folder = args.__dict__.get("folder")

    logger.info("Starting to apply license to %s" % folder)

    need_to_set_license_file = True
    for file in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, file)) and file == 'LICENSE':
            need_to_set_license_file = False

    if need_to_set_license_file:
        shutil.copy("LICENSE", folder)

    all_full_path_files = [os.path.join(dirpath, f) for (dirpath, dirnames, filenames)
                           in os.walk(folder) for f in filenames]

    for file in all_full_path_files:
        logger.debug("Treating file: %s" % file)
        extension = file.split('.')[-1]
        input_file = "license-shell"

        if extension == 'java' or extension == 'scala':
            input_file = "license-java"
        elif extension == 'xml':
            input_file = "license-xml"
        elif extension != 'sh' and extension != 'properties' and extension != 'yml' and extension != 'py':
            continue

        logger.info("File matches required extension to be treated: %s" % file)

        with open(input_file, 'r') as header:
            with open(file, 'r') as content:
                with open(file+'.lm_tmp_XXXX', 'w') as output_file:
                    output_file.write(header.read())
                    output_file.write(content.read())

        shutil.move(file+'.lm_tmp_XXXX', file)

        logger.info("Finished to treat file: %s" % file)

    logger.info("Finished to apply license to %s" %  folder)


if __name__ == "__main__":
    # Prepare logger
    logger = logging.getLogger("license_maker")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    main()
