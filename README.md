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

| Framework/Hardware | Nvidia A100   | Graphcore      |  Habana Gaudi |  Groq         |
| :-------------:    | :-----------: | :------------: | :-----------: | :-----------: |
| ResNet50           | ✅           |  ✅            |  ✅          |  ✅           |
| BERT-Large         | ✅           |  ✅            |  ✅          |  ✅           |

## Instructions

Please navigate to the relevant directories and refer to the README.md there. 

```sh
cd Nvidia_A100
cd Graphcore
cd Habana
```

## Citation
If you find this repository useful, please consider citing our paper:

```
@INPROCEEDINGS{farah2025mlperf,
  title={Evaluating Energy Efficiency of AI Accelerators Using Two MLPerf Benchmarks},
  author={Ferdaus, Farah and Wu, Xingfu and Taylor, Valerie and Lan, Zhiling and Shanmugavelu, Sanjif and Vishwanath, Venkatram and Papka, Michael E.},
  booktitle={25th IEEE International Symposium on Cluster, Cloud, and Internet Computing, 2025},
  year={2025}
}
```


##### Acknowledgements
> This research was supported in part by DOE ASCR Base PIONEER (Program for Innovative Optimization of Next-gen Energy Efficient Resources) project and in part by DOE ASCR SciDAC RAPIDS. We gratefully acknowledge the Argonne Leadership Computing Facility for use of AI testbeds. This material is based upon work supported by the U.S. Department of Energy, Office of Science, under contract number DE-AC02-06CH11357, at Argonne National Laboratory.
