import pickle
import glob


if __name__ == '__main__':
    write_file = 'group_results.p'
    file_dir = '/Users/aaronlong/Projects/pytorch_hackathon/data/ssd_inference_32/'
    paths = glob.glob(file_dir + '*.p')

    if len(glob.glob(file_dir + write_file)):
        print('already done!')
    else:
        new_data = list()
        for p in paths:
            with open(p, 'rb') as f:
                new_data.extend(pickle.load(f))

        with open(file_dir + write_file, 'wb') as f:
            pickle.dump(new_data, f)
