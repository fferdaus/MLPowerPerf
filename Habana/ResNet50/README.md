# ResNet50 on Habana Gaudi

The ResNet50 benchmark is sourced from the [HabanaAI Model References Github Repo](https://github.com/HabanaAI/Model-References/blob/master/README.md)

We utilized Gaudi1 systems at [AI testbeds](https://www.alcf.anl.gov/alcf-ai-testbed) within ALCF.

For Gaudi2, we had limited access to Intel's Habana Gaudi2 systems and conducted the experiments on their platform.

HabanaAI published optimized ResNet50 and BERT_large models for MLPERF3.1, which we have used in our paper; however, those models were not available on MLPERF4.0. Currently, they only have this [ResNet50](https://github.com/HabanaAI/Model-References/blob/master/PyTorch/computer_vision/classification/torchvision/README.md) model available.
