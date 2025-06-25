# BERT-large on Graphcore

The BERT-large benchmark is sourced from the Graphcore Examples Github Repo. https://github.com/graphcore/examples/blob/master/nlp/bert/pytorch/README.md

We utilized Graphcore systems (https://docs.alcf.anl.gov/ai-testbed/graphcore/getting-started/) at AI testbeds within ALCF.

## Setup

Follow the instructions from the Graphcore Examples GitHub repo for setup.

## Running BERT-large Benchmark

* Use `run_pretraining.py` script provided here to collect throughput and power measurements. 
    > You will need `power_script.py` file for power metric collectring in the same direcotry as the `run_pretraining.py`

## Run Benchmarks 

* Running for pre-training with checkpointing

```bash
python3 run_pretraining.py --config pretrain_large_128 --input-files /mnt/localdata/torch_bert/packed_128/*.tfrecord --disable-progress-bar --packed-data --checkpoint-output-dir /projects/EE-ECP/fferdaus/bert_checkpoint/checkpoint_128/
```

* Running for SQuAD application 

```bash
python3 run_squad.py --squad-do-validation True --config squad_large_384 --checkpoint-input-dir /projects/EE-ECP/fferdaus/bert_checkpoint/checkpoint_512/step_2136
```
