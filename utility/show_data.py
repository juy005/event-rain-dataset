import numpy as np
import argparse
import cv2
import os
import pandas as pd

# events visualization
def draw_img(input_folder, input_seq, imagesize):
    data_path = input_folder + '/data/' + str(input_seq) + '.csv' #event data path
    label_path = input_folder + '/data_label/' + str(input_seq) + '.csv' #label data path
    events = pd.read_csv(data_path,header=0,names=['t','x','y','p'])
    labels = pd.read_csv(label_path,header=0,names=['x1','y1','x2','y2'])
    img = np.ones((imagesize[0],imagesize[1],3),np.uint8)
    for num_event in range(len(events)):
        img[events['y'][num_event],events['x'][num_event]] = [255,255,255]
    if len(labels) > 0:
        for num_label in range(len(labels)):
            cv2.rectangle(img,(labels['x1'][num_label],labels['y1'][num_label]),(labels['x2'][num_label],labels['y2'][num_label]),(0,0,255),1)
    output_path = input_folder + '/img_label/' + str(input_seq) + '.png'
    cv2.imwrite(output_path, img)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('show_data')
    parser.add_argument('--input_folder', type=str, default='**/static') #input file
    parser.add_argument('--input_seq', type=int, default=1) #input data seqence
    parser.add_argument('--image_width', type=int, default=1280) #image width
    parser.add_argument('--image_height', type=int, default=720) #image height
    args = parser.parse_args()
    imagesize = [args.image_height, args.image_width]
    draw_img(args.input_folder, args.input_seq, imagesize) 