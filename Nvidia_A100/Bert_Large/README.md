# BERT-large on NVIDIA A100

The BERT-large benchmark is sourced from the NVIDIA Deep Learning Examples Github Repo. https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/LanguageModeling/BERT/README.md

We used A100 80GB GPU systems on Sophia (https://www.alcf.anl.gov/sophia) at ALCF.

## Setup

Follow the instructions from the NVIDIA Deep Learning Examples GitHub repo for setup.

## Running BERT-large Benchmark

* Use `run_pretraining.py` script provided here to collect throughput and power measurements. 
    > You will need `power_script.py` file for power metric collectring in the same directory as the `run_pretraining.py`

## Run Benchmarks 

* Running for pretraining

```bash
singularity shell --nv --fakeroot --sharens -B /raid,/lus,/soft,/eagle,/raid/scratch/workspace:/workspace bert.sif
```
