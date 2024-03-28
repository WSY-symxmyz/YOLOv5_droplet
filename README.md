# YOLOv5 for droplet detection
## Install codes modified from original YOLOv5
```linux
$ git clone https://github.com/WSY-symxmyz/YOLOv5_droplet.git
$ cd YOLOv5_droplet
$ pip install -r requirements.txt
```

## Train on own dataset
First arrange the dataset in the required way.

```linux
$ python3 train.py --data selftxtfile --epochs 50 --weights 'customized_name' --cfg yolov5s.yaml --batch-size 16
```

Then the weight file will be stored in the dir `runs/train/your_dir_name/weights` as a `.pt` file.

## Detect

the `detect.py`, `dataloader.py`, etc. files have been modified for detecting using the camera.

See annotations in relevant codes.
