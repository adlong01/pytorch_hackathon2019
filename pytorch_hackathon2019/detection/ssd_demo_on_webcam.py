import cv2
import torch
import numpy as np
import matplotlib.pyplot as plt

class SSDEngine:
    def __init__(self):
        self.ssd = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub',
                                'nvidia_ssd',
                                model_math='fp32',
                                force_reload=False).eval()

        self.utils = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub',
                                'nvidia_ssd_processing_utils')
        self.conf_thresh = 0.05

    def run(self):
        # get the camera
        cam = cv2.VideoCapture(0)

        # make the matplotlib figure for visualization
        fig = plt.figure(figsize=[10,10])
        ax = plt.gca()

        try:
            while True:
                ax.cla()
                pic = self.get_image(cam)
                outputs = self.ssd(self.prepare_image(pic))
                boxes, cid, conf = self.process_output(outputs)[0]
                ax.imshow(pic)
                self.draw_boxes(ax, boxes)
                plt.pause(0.01)

        finally:
            cam.release()

    @staticmethod
    def get_image(cam):
        ret, frame = cam.read()
        frame = np.array(frame)
        frame = frame[:,:,::-1]
        frame = cv2.resize(frame, (300, 300)) / 255.
        return frame

    @staticmethod
    def draw_boxes(ax, boxes):
        for box in boxes:
            box = box * 300
            x0,y0,x1,y1 = box
            ax.add_patch(plt.Rectangle((x0, y0),
                                        x1-x0,
                                        y1-y0,
                                        fill=False,
                                        edgecolor='g',
                                        linestyle='--',
                                        linewidth=1.5))

    @staticmethod
    def prepare_image(image):
        # channel first, add batch dimension, convert to single prec
        return torch.as_tensor(np.transpose(image, (2, 0, 1))[np.newaxis, ...].astype(np.float32))

    def process_output(self, output):
        results_per_input = self.utils.decode_results(output)
        best_results_per_input = [self.utils.pick_best(results, self.conf_thresh)
                                        for results in results_per_input]
        return best_results_per_input

if __name__ == '__main__':
    engine = SSDEngine()
    engine.run()
