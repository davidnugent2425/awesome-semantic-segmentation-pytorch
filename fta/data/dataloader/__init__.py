"""
This module provides data loaders and transformers for popular vision datasets.
"""
from .ughent import UGhentSegmentation
from .danish import DanishSegmentation
from .mscoco import COCOSegmentation
from .cityscapes import CitySegmentation
from .ade import ADE20KSegmentation
from .pascal_voc import VOCSegmentation
from .pascal_aug import VOCAugSegmentation
from .sbu_shadow import SBUSegmentation
from .overfit import OverfitSegmentation

datasets = {
    'ade20k': ADE20KSegmentation,
    'pascal_voc': VOCSegmentation,
    'pascal_aug': VOCAugSegmentation,
    'coco': COCOSegmentation,
    'citys': CitySegmentation,
    'sbu': SBUSegmentation,
    'ughent':UGhentSegmentation,
    'danish':DanishSegmentation,
    'overfit':OverfitSegmentation
}

def get_segmentation_dataset_names():
    return list(datasets.keys())

def get_segmentation_dataset(name, **kwargs):
    """Segmentation Datasets"""
    return datasets[name.lower()](**kwargs)
