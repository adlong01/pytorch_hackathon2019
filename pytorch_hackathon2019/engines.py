import cv2
import torch
import numpy as np
import matplotlib.pyplot as plt
import time
from tqdm import tqdm


class SSDEngine():
    def __init__(self, confidence_threshold = 0.01):
        self.ssd = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub',
                                'nvidia_ssd',
                                model_math='fp32',
                                force_reload=False).eval()

        self.utils = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub',
                                'nvidia_ssd_processing_utils')
        self.conf_thresh = confidence_threshold
        self.classes_to_labels = self.utils.get_coco_object_dictionary()


    def run(self, video_sequence, video_name):
        """gets outputs for the whole sequence

        Args:
            video_sequence (np.ndarray): (N, H, W, C) numpy array

        Return:
            list of proposals, a set for every item
        """
        results = []
        ff = 8
        video_sequence = self.prepare_tensor(video_sequence[::ff, ...])
        with tqdm(total=video_sequence.shape[0]) as pbar:
            batch = []
            for idx, frame in enumerate(video_sequence):
                indices = [idx*ff]
                frame = cv2.resize(frame, (300, 300))
                frame = np.transpose(frame, (2, 0, 1))
                batch = torch.tensor(frame[np.newaxis,...])
                bs = batch.size(0)
                loc_preds, cls_preds = self.ssd(batch)
                outputs = (loc_preds, cls_preds)
                # boxes, cid, conf = self.process_output(outputs)[0]
                try:
                    processed_outputs = self.process_output(outputs)
                    for i, x in zip(indices, processed_outputs):
                        boxes, cls_id, confidences = x
                        m = confidences > 0.3
                        if m.sum() > 0:
                            boxes = boxes[m]
                            cls_id = cls_id[m]
                            cls_id = [self.classes_to_labels[x-1] for x in cls_id]
                            confidences = confidences[m]
                            results.append({'video': video_name, 'frame': i, 'results': (boxes, cls_id, confidences)})
                        else:
                            results.append({'video': video_name, 'frame': i, 'results': ([],[],[])})

                except Exception as e:
                    print(f'warning, skipping frames {indices}')
                    for i in indices:
                        results.append({'video': video_name, 'frame': i, 'results': ([],[],[])})
                finally:
                    pbar.update(bs)

        return results

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
    def prepare_tensor(batch_tensor):
        # channel first, add batch dimension, convert to single prec
        # image = image[:, :, ::-1] # bgr -> rgb
        # image = cv2.resize(image, (300, 300))
        batch_tensor = batch_tensor.astype(np.float32)
        # [0,1]
        batch_tensor /= 255.
        # mean
        batch_tensor[:,:,0] -= 0.485
        batch_tensor[:,:,1] -= 0.456
        batch_tensor[:,:,2] -= 0.406
        # std
        batch_tensor[:,:,0] /= 0.229
        batch_tensor[:,:,1] /= 0.224
        batch_tensor[:,:,2] /= 0.225
        return batch_tensor

    def process_output(self, output):
        try:
            results_per_input = self.utils.decode_results(output)
        except Exception as e:
            print(output)
            raise e
        best_results_per_input = [self.utils.pick_best(results, self.conf_thresh)
                                        for results in results_per_input]
        return best_results_per_input

if __name__ == '__main__':
    engine = SSDEngine()
    engine.run()
