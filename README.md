# Evaluating Energy Efficiency of AI Accelerators Using Two MLPerf Benchmarks

**Authors:** Farah Ferdaus, Xingfu Wu, Valerie Taylor, Zhiling Lan, Sanjif Shanmugavelu, Venkatram Vishwanath, Michael E. Papka

**Affliation:** Argonne National Laboratory, University of Illinois Chicago, Groq Inc.  

This repository is the official implementation of "Evaluating Energy Efficiency of AI Accelerators Using Two MLPerf Benchmarks" paper

## Table of Contents

- [About](#about)
- [Evaluated Models and Hardwares](#evaluated-models-and-hardwares)
- [Citation](#citation)
- [Acknowledgement](#acknowledgements)

## About
The significantly increasing use of artificial intelligence (AI) has led to the availability of specialized AI accelerators, aiming to enhance the performance and energy efficiency of AI workloads. In this work, we conduct an initial study to evaluate the energy requirements of four AI accelerators: Nvidia A100 GPUs, Intel Habana Gaudi Processing Units (HPUs), Graphcore Bow-Pod64 Intelligence Processing Units (IPUs), and GroqRack Language Processing Units (LPUs) using two popular MLPerf benchmarks: BERT-Large and ResNet50. We report the energy requirements for the two benchmarks to achieve a common MLPerf specified target accuracy. The benchmarks and AI accelerators were chosen based on the following criteria: publicly available tools or libraries from the vendors to monitor power consumption, publicly available optimized models from the vendors, and access to the AI accelerators. 

## Evaluated Models and Hardwares

| Framework/Hardware | Nvidia A100   | Graphcore      |  Habana Gaudi |  Groq         |  AMD         |
| :-------------:    | :-----------: | :------------: | :-----------: | :-----------: |:-----------: |
| ResNet50           | ✅           |  ✅            |  ✅          |  ✅           | WIP          |
| BERT-Large         | ✅           |  ✅            |  ✅          |  ✅           | WIP          |

## Instructions

Please navigate to the relevant directories and refer to the README.md there. 

```sh
cd Nvidia_A100
cd Graphcore
cd Habana
```

## Quick Guide 

| Hardware            | Framework      | Directory         |
| :--------------:    | :------------: | :-------:         |
| Nvidia A100 GPU     | ResNet50       | [Directory](Nvidia_A100/ResNet50/)         | 
|                     | BERT_Large     | [Directory](Nvidia_A100/Bert_Large/)       |
| Graphcore BowPod64  | ResNet50       | [Directory](Graphcore/ResNet50/)           |
|                     | BERT_Large     | [Directory](Graphcore/Bert_Large/)         |
| Habana Gaudi        | ResNet50       | [Directory](Habana/ResNet50/)              | 
|                     | BERT_Large     | [Directory](Habana/Bert_Large/)            |
| Groq                | ResNet50       | [Directory](Groq/ResNet50/)              | 
|                     | BERT_Large     | [Directory](Groq/Bert_Large/)            |
| AMD MI250 GPU       | Model          | [Directory](AMD_MI250/)                    |

## Citation
If you find this repository useful, please consider citing our paper:

```
@INPROCEEDINGS{11044796,
  author={Ferdaus, Farah and Wu, Xingfu and Taylor, Valerie and Lan, Zhiling and Shanmugavelu, Sanjif and Vishwanath, Venkatram and Papka, Michael E.},
  booktitle={2025 IEEE 25th International Symposium on Cluster, Cloud and Internet Computing (CCGrid)}, 
  title={Evaluating Energy Efficiency of Ai Accelerators Using Two Mlperf Benchmarks}, 
  year={2025},
  volume={},
  number={},
  pages={549-558},
  doi={10.1109/CCGRID64434.2025.00035}}
```


##### Acknowledgements
> This research was supported in part by DOE ASCR Base PIONEER (Program for Innovative Optimization of Next-gen Energy Efficient Resources) project and in part by DOE ASCR SciDAC RAPIDS. We gratefully acknowledge the Argonne Leadership Computing Facility for use of AI testbeds. This material is based upon work supported by the U.S. Department of Energy, Office of Science, under contract number DE-AC02-06CH11357, at Argonne National Laboratory.
