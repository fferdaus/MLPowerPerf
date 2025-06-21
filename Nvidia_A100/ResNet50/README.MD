# ResNet50 on NVIDIA A100

The ResNet50 benchmark is sourced from the NVIDIA Deep Learning Examples Github Repo. https://github.com/NVIDIA/DeepLearningExamples/blob/master/PyTorch/Classification/ConvNets/resnet50v1.5/README.md

We used A100 GPU systems on Sophia at ALCF.

## Setup

Follow the instructions from the NVIDIA Deep Learning Examples GitHub repo for setup.

## Running ResNet50 Benchmark

1. Use `launch.py` script provided here to collect throughput measurements. 
2. Use `launch_power.py` script provided here to collect power measurements. 
    > You will need `power_script.py` file for power metric collectring in the same direcotry as the `launch_power.py`

## Run Benchmarks 

* Running for automatic Mixed Precision

```bash
python3 ./launch.py --model resnet50 --precision AMP --mode convergence_no_ckpts --platform DGXA100 /local/scratch/ImageNet/ --raport-file sophia_amp_epoch50.json --epochs 50 
```

* Running for FP32 Precision

```bash
python3 ./launch.py --model resnet50 --precision FP32 --mode convergence_no_ckpts --platform DGXA100 /local/scratch/ImageNet/ --raport-file sophia_fp32_epoch50.json --epochs 50 
```

