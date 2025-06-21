# BERT-large on NVIDIA A100

The BERT-large benchmark is sourced from the NVIDIA Deep Learning Examples Github Repo. https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/LanguageModeling/README.md

We used A100 GPU systems on Sophia at ALCF.

## Setup

Follow the instructions from the NVIDIA Deep Learning Examples GitHub repo for setup.

## Running BERT-large Benchmark

1. Use `launch.py` script provided here to collect throughput measurements. 
2. Use `launch_power.py` script provided here to collect power measurements. 
    > You will need `power_script.py` file for power metric collectring in the same direcotry as the `launch_power.py`

## Run Benchmarks 

* Running for automatic Mixed Precision

```bash
python3 ./launch.py --model resnet50 --precision AMP --mode convergence_no_ckpts --platform DGXA100 /local/scratch/ImageNet/ --raport-file sophia_amp_epoch50.json --epochs 50 
```
