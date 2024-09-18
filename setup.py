from setuptools import setup, find_packages

setup(
    name='VAL_LabelImgs',
    version='0.1.6rc3',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'requests',
        'psutil',
        'tqdm',
        'matplotlib',
        'pyyaml',
        'pandas',
        'numpy',
        'torch',
        'thop',
        'torchvision',
        'ultralytics-thop',
        'urllib3',
        'Werkzeug',
        'yolov6',
        'pycocotools',
        'PyQt5',
        'lxml'
    ],
    package_data={
        'VAL_LabelImgs': ['ultralytics/cfg/default.yaml','data/coco.yaml','data/default_imgs.yaml','data/predefined_classes.txt','default_imgs.yaml'],
        # Bao gồm file YAML trong gói
    },
    entry_points={
        'console_scripts': [
            'VAL_LabelImgs=VAL_LabelImgs.mainapp:main_app'
        ]
    }
)
