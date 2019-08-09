import torch
import pickle
import glob

def load_pickle(path):
    with open(path, 'rb') as f:
        data = pickle.load(f)
    return data

def get_result_paths():
    return glob.glob('/Users/aaronlong/Projects/pytorch_hackathon/data/ssd300_inference/*.p')

if __name__ == '__main__':
    utils = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_ssd_processing_utils')
    classes_to_labels = utils.get_coco_object_dictionary()

    paths = get_result_paths()

    for p in paths:
        data = load_pickle(p)
        for frame_data in data:
            results = frame_data['results']
            boxes, classes, indices = results
            print(boxes, classes, indices)
            raise
