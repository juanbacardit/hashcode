import os
import sys
import array

class picture:
    def __init__(self, orientation, tags):
        self.orientation = orientation
        self.tags = tags

    def get_interest_factor(self, picture):
        c3 = [filter(lambda x: x in picture.tags, sublist) for sublist in self.tags]
        print c3

    def __str__(self):
        return self.tags


base_set = {}
tag_tree = {}
orientation = {}
picts = []

def execute(filename):
    f = open(filename,'r')

    num_of_photos = int(f.readline())
    print num_of_photos

    for x in range(num_of_photos):
        line = f.readline()[:-1].split(" ")
        orientation = line[0]
        tags = line[2:]
        base_set[x] = {'o':orientation,'tags':tags}
        picts.append(picture(orientation,tags))
        print picts

if __name__ == "__main__":
    execute('a_example.txt')




