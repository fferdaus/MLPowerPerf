# ResNet50 on NVIDIA A100

The ResNet50 benchmark is sourced from the NVIDIA Deep Learning Examples Github Repo. https://github.com/NVIDIA/DeepLearningExamples/blob/master/PyTorch/Classification/ConvNets/resnet50v1.5/README.md

We used A100 GPU systems on Sophia at ALCF.

## Setup

Follow the instructions from the NVIDIA Deep Learning Examples GitHub repo for setup.

## Running ResNet50 Benchmark

```bash
git clone https://github.com/vllm-project/vllm.git
cd vllm/benchmarks/

python benchmark_latency.py --batch-size=32 --tensor-parallel-size=1 --input-len=32--output-len=32 --model="meta-llama/Llama-2-7b-hf" --dtype="float16" --trust-remote-code
```

## Run Benchmarks 

1. Use `launch.py` script provided here to collect throughput measurements. 
2. Use `launch_power.py` script provided here to collect power measurements. 
    > You will need `power_utils.py` file for power metric collectring in the same direcotry as the `launch_power.py`

