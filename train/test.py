import os
import sys
import argparse

import numpy as np

prj_path = os.path.join(os.path.dirname(__file__), '..')
if prj_path not in sys.path:
    sys.path.append(prj_path)

from lib.test.evaluation import get_dataset
from lib.test.evaluation.running import run_dataset
from lib.test.evaluation.tracker import Tracker


def run_tracker(tracker_name, tracker_param, run_id=None, dataset_name='otb', sequence=None, debug=0, threads=0,
                num_gpus=8, tag=0, trackerss={}):
    """Run tracker on sequence or dataset.
    args:
        tracker_name: Name of tracking method.
        tracker_param: Name of parameter file.
        run_id: The run id.
        dataset_name: Name of dataset (otb, nfs, uav, tpl, vot, tn, gott, gotv, lasot).
        sequence: Sequence number or name.
        debug: Debug level.
        threads: Number of threads.
    """

    dataset = get_dataset(dataset_name)

    if sequence is not None:
        dataset = [dataset[sequence]]

    trackers = [Tracker(tracker_name, tracker_param, dataset_name, run_id)]

    run_dataset(dataset, trackers, debug, threads, num_gpus=num_gpus, tag=tag, trackerss=trackerss)


def out_txt(tracker_dir):
    file_list = []  # 存储文件路径列表
    tracker_dict = {}
    # 获取文件夹中的所有txt文件路径
    for file_name in os.listdir(tracker_dir):
        content_list = []
        txt_name = None
        if file_name.endswith('.txt') and not file_name.endswith("_time.txt"):
            file_path = os.path.join(tracker_dir, file_name)
            txt_name = file_name.split('.')[0]
            with open(file_path, 'r') as file:
                for line in file:
                    num_list = [float(num) for num in line.split(',') or line.split('\t')]
                    content_list.append(np.array(num_list))
        tracker_dict[txt_name] = content_list
    return tracker_dict


def main():
    parser = argparse.ArgumentParser(description='Run tracker on sequence or dataset.')
    parser.add_argument('--tracker_name', default='DFDT', type=str, help='Name of tracking method.')
    parser.add_argument('--tracker_param', default='vitb_384_mae_ce_32x4_ep300', type=str, help='Name of config file.')
    parser.add_argument('--runid', type=int, default=None, help='The run id.')
    parser.add_argument('--dataset_name', type=str, default='ptbtir', help='Name of dataset (lsotbtir120, ptbtir).')
    parser.add_argument('--sequence', type=str, default=None, help='Sequence number or name.')
    parser.add_argument('--debug', type=int, default=0, help='Debug level.')
    parser.add_argument('--threads', type=int, default=20, help='Number of threads.')
    parser.add_argument('--num_gpus', type=int, default=4)

    args = parser.parse_args()

    try:
        seq_name = int(args.sequence)
    except:
        seq_name = args.sequence

    tag = 0
    trackerss = {}
    if tag:
        t = []
        t_n = ['/media/dell/xzj/dataset/test_result_txt/LSOTB_TIR_results/MDNet',
               '/media/dell/xzj/dataset/test_result_txt/LSOTB_TIR_results/VITAL',
               '/media/dell/xzj/dataset/test_result_txt/LSOTB_TIR_results/ECO_deep_TIR',
               '/media/dell/xzj/dataset/test_result_txt/LSOTB_TIR_results/ATOM',
               '/media/dell/xzj/dataset/test_result_txt/LSOTB_TIR_results/SiamRPN++'
               ]
        for i in range(len(t_n)):
            t.append(t_n[i])
        for idx in range(len(t)):
            tracker_name = t[idx].split('/')[-1]
            trackerss[tracker_name] = out_txt(t[idx])

    run_tracker(args.tracker_name, args.tracker_param, args.runid, args.dataset_name, seq_name, args.debug,
                args.threads, num_gpus=args.num_gpus, tag=tag, trackerss=trackerss)


if __name__ == '__main__':
    os.environ['CUDA_VISIBLE_DEVICES'] = '0,1,2,3'
    main()
