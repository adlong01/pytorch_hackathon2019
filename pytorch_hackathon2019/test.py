import cv2
import numpy as np
import matplotlib.pyplot as plt
import torch


def get_image(cam):
    ret, frame = cam.read()
    frame = np.array(frame)
    frame = frame[:,:,::-1]
    frame = cv2.resize(frame, (300, 300)) / 255.
    return frame

def get_ssd():
    return torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_ssd', model_math='fp32', force_reload=False)

def run_ssd(ssd, image):
    image = np.transpose(image, (2, 0, 1))[np.newaxis, ...].astype(np.float32)
    image = torch.as_tensor(image)
    print(image.shape)
    output = ssd(image)
    return output

def process_output(output, utils):
    results_per_input = utils.decode_results(outputs)
    best_results_per_input = [utils.pick_best(results, 0.05) for results in results_per_input]
    return best_results_per_input

if __name__ == '__main__':
    utils = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_ssd_processing_utils')
    ssd = get_ssd()
    ssd.eval()
    cam = cv2.VideoCapture(0)
    
    fig = plt.figure(figsize=[10,10])
    ax = plt.gca()
    
    try:
        while True:
            pic = get_image(cam)
            outputs = run_ssd(ssd, pic)
            outputs = process_output(outputs, utils)
            boxes, cid, conf = outputs[0]

            ax.cla()
            ax.imshow(pic)
            for box in boxes:
                box = box * 300
                x0,y0,x1,y1 = box
                ax.add_patch(plt.Rectangle((x0, y0), x1-x0, y1-y0, fill=False, edgecolor='g', linestyle='--', linewidth=1.5))
            plt.pause(0.01)
    finally:
        cam.release()

