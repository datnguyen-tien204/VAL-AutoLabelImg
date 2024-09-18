# Ultralytics YOLO 🚀, AGPL-3.0 license

__version__ = "8.2.95"


import os

# Set ENV Variables (place before imports)
os.environ["OMP_NUM_THREADS"] = "1"  # reduce CPU utilization during training

from VAL_LabelImgs.ultralytics.data.explorer.explorer import Explorer
from VAL_LabelImgs.ultralytics.models import NAS, RTDETR, SAM, YOLO, FastSAM, YOLOWorld
from VAL_LabelImgs.ultralytics.utils import ASSETS, SETTINGS
from VAL_LabelImgs.ultralytics.utils.checks import check_yolo as checks
from VAL_LabelImgs.ultralytics.utils.downloads import download

settings = SETTINGS
__all__ = (
    "__version__",
    "ASSETS",
    "YOLO",
    "YOLOWorld",
    "NAS",
    "SAM",
    "FastSAM",
    "RTDETR",
    "checks",
    "download",
    "settings",
    "Explorer",
)
