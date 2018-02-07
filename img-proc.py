import os
import sys

# Imports the GCP lib
from google.cloud import vision

# Instantiates a client
client = vision.ImageAnnotatorClient()


def processfile(dir, filename):
    print(' loading ' + dir + '/' + filename)
    with open(dir + '/' + filename, 'rb') as image_file:
        response = client.annotate_image({
            'image': {'content': image_file.read()},
            'features': [
                {'type': 'TEXT_DETECTION'},
                {'type': 'LABEL_DETECTION'}
            ]
        })

        if not os.path.exists(dir + '/out/'):
            os.makedirs(dir + '/out/')

        with open(dir + '/out/' + filename + '.txt', "w") as content:
            for label in response.label_annotations:
                content.write(label.description)
                content.write('\n')

            for text in response.text_annotations:
                content.write(text.description)


def process(dir):
    print('Processing ', dir)

    if not os.path.exists(dir):
        print('dir does not exists')
        return

    for entry in os.listdir(dir):
        processfile(dir, entry)


def main(argv):
    if len(argv) != 1:
        print('dir not provided')
    else:
        process(argv[0])


if __name__ == "__main__":
    main(sys.argv[1:])
