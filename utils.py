#!/usr/bin/python
#coding:utf-8

import logging, sys, argparse

def str2bool(v):
    # copy from StackOverflow
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def get_entity(tag_seq, char_seq):
    LOC = get_post_entity(tag_seq, char_seq, start_post='B-LOC', in_post='I-LOC')
    PER = get_post_entity(tag_seq, char_seq, start_post='B-PER', in_post='I-PER')
    ORG = get_post_entity(tag_seq, char_seq, start_post='I-ORG', in_post='I-ORG')
    return PER, LOC, ORG


def get_post_entity(tag_seq, char_seq, start_post='B-LOC', in_post='I-LOC'):
    LOC = []
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == start_post:
            LOC.append(char_seq[i])
        elif tag == in_post and len(LOC)>0:
            LOC[-1] += char_seq[i]
    return LOC


def get_logger(filename):
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
    logging.getLogger().addHandler(handler)
    return logger


if __name__ == '__main__':
    tag = ['B-LOC', 'I-LOC', 0, 0, 0, 0, 0]
    demo_sent = ['无', '锡', '是', '个', '好', '地', '方']

    tag = ['B-LOC', 'I-LOC', 0, 'B-LOC', 'I-LOC', 0, 0, 0, 0, 0]
    demo_sent = ['苏', '州', '到', '上', '海', '有', '多', '少', '巨', '鹿']

    print(get_entity(tag, demo_sent))