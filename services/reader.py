from models.object import *


def get_object_from_file(self, filename):
    vertex, faces = [], []

    with open(filename) as f:
        for line in f:
            if line.startswith('v '):
                vertex.append([float(i) for i in line.split()[1:]] + [1])
            elif line.startswith('f'):
                tmp_faces = line.split()[1:]
                faces.append([int(tmp_face.split('/')[0]) - 1 for tmp_face in tmp_faces])

    return Object(self, vertex, faces)