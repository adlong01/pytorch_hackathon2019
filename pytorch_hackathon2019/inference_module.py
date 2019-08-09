from engines import SSDEngine
import pickle
import skvideo
from skvideo.io import vread
import glob

class InferenceModule:
    def __init__(self, video_paths):
        self.ssd = SSDEngine()
        self.videos = video_paths if isinstance(video_paths, list) else [video_paths]

    def run(self):
        for path in self.videos:
            save_path = path[:-4] + '_results_testrun.p'
            print(f'Saving results to path: {save_path}')
            video = vread(path)
            print(video.shape)
            results = self.ssd.run(video, path)
            print(f'Saving {len(results)} results to path: {save_path}')
            self.write(results, save_path)

    @staticmethod
    def write(results, path):
        with open(path, 'wb') as f:
            pickle.dump(results, f)

    @staticmethod
    def load(path):
        with open(path, 'rb') as f:
            data = pickle.load(path)
        return data

if __name__ == '__main__':
    paths = glob.glob('/Users/aaronlong/Projects/pytorch_hackathon/data/videos_640x480/*.mp4')
    InferenceModule(paths).run()
