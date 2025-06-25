# ResNet50 on Graphcore

The ResNet50 benchmark is sourced from the Graphcore Examples Github Repo. https://github.com/graphcore/examples/blob/master/vision/cnns/pytorch/README.md

We utilized Graphcore systems (https://www.alcf.anl.gov/alcf-ai-testbed) at AI testbeds within ALCF.

## Setup

Follow the instructions from the Graphcore Examples GitHub repo for setup.

## Running ResNet50 Benchmark

* Use `train.py` script provided here to collect throughput and power measurements. 
    > You will need `power_script.py` file for power metric collectring in the same direcotry as the `train.py`

## Run Benchmarks 

* Running for 4 IPUs

```bash
poprun -vv --vipu-partition=slurm_${SLURM_JOBID} --num-instances=2 --num-replicas=4 --executable-cache-path=$PYTORCH_CACHE_DIR python3 /projects/EE-ECP/fferdaus/examples/vision/cnns/pytorch/train/train.py --config resnet50-pod4 --imagenet-data-path /mnt/localdata/datasets/imagenet-raw-dataset --epoch 100 --validation-mode during --dataloader-worker 14 --dataloader-rebatch-size 256 
```

* Running for 16 IPUs

```bash
poprun -vv --vipu-partition=slurm_${SLURM_JOBID} --num-instances=4 --num-replicas=16 --executable-cache-path=$PYTORCH_CACHE_DIR python3 /projects/EE-ECP/fferdaus/examples/vision/cnns/pytorch/train/train.py --config resnet50 --imagenet-data-path /mnt/localdata/datasets/imagenet-raw-dataset --epoch 100 --validation-mode during --dataloader-worker 14 --dataloader-rebatch-size 256
```
