# I had a directory with thousands of images to move and separate according to their IDs
# I also had a .csv with the file names and IDs, so I build this to facilitate

# It moves and separate files according to a category or ID, it uses a .csv containing the file name with extension
# and the respective ID for each file.

import os.path
import shutil
import csv

IMAGES_PATH = '/img'
OUTPUT_PATH = 'C:/projectX/training_images'
CSV = 'train.csv'

with open(CSV) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        src = IMAGES_PATH + row[0]
        dst = OUTPUT_PATH + row[1] + '/' + row[0]
        newDir = OUTPUT_PATH + row[1]
        if not os.path.exists(newDir):
            os.makedirs(newDir)
            print('directory created: ' + newDir)
        shutil.copy2(src, dst, follow_symlinks=True)
        print(f'\t{row[0]} id {row[1]}' + ' was saved')


