# MS MARCO LLM Distillation

This repository contains the code and data for the paper `A Systematic Investigation of Distilling Large Language Models into Cross-Encoders for Passage Re-ranking`.

## Usage

We use the [`lightning-ir`](https://github.com/webis-de/lightning-ir) library for fine-tuning and running experiments. Follow the installation instructions from the repository to install the library.

### Data

We will release the full run files for MS MARCO training queries upon acceptance. Sample run files can be found in the supplementary material.

### Fine-tuning

To fine-tune a model using ColBERTv2 hard negatives, update the `train_dataset` argument in `configs/monoelectra-fine-tune-colbert.yaml` to point to the downloaded ColBERTv2 run file.

Then run the following command to fine-tune the model:

```bash
lightning-ir fit --config configs/monoelectra-fine-tune-colbert.yaml
```

To fine-tune a model using our proposed distillation method, update the `train_dataset` argument in `configs/monoelectra-fine-tune-distillation.yaml` to point to the downloaded distillation run file.

Then run the following command to fine-tune the model:

```bash
lightning-ir fit --config configs/monoelectra-fine-tune-distillation.yaml
```

### Inference

We provide an example configuration file for running inference on TREC Deep Learning 2019 and 2020 in `configs/predict-trec-dl.yaml`. Replace the `model_path` argument with the path to the fine-tuned model.

To re-rank passages, run the following command (this will download the MS MARCO passage corpus using [`ir_datasets`](https://ir-datasets.com/)):

```bash
lightning-ir re_rank --config configs/predict-trec-dl.yaml
```
