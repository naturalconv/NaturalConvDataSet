
# NaturalConv

PLEASE READ THIS BEFORE USE THE SCRIPT.
This repository provides examplar code for researchers to download the documents from the provided URLs of NaturalConv for non-commerical research purpose only.
If you feel it costs too much time to download, please refer to Third Party Work below.

## Dataset Download

Please locate and download the offical NaturalConv Dataset from [here](https://ai.tencent.com/ailab/nlp/dialogue/#datasets). It contains all the dialogues, and the urls of the grounding documents.

NaturalConv is released for non-commerical usage only. By downloading, you agree to the terms and conditions in the license that is included in the dataset zip file.

## How to Use

You can download a large part of the grounding documents using the python code through the given urls.

```
python download_document.py --doc_url_json document_url_release.json --output_dir ./
```

document_url_release.json can be found [here](https://ai.tencent.com/ailab/nlp/dialogue/#datasets).

## Citation

Please kindly cite the following paper if you find NaturalConv useful:

```
@inproceedings{aaai-2021-naturalconv,
    title={NaturalConv: A Chinese Dialogue Dataset Towards Multi-turn Topic-driven Conversation},
    author={Wang, Xiaoyang and Li, Chen and Zhao, Jianqiao and Yu, Dong},
    booktitle={Proceedings of the 35th AAAI Conference on Artificial Intelligence (AAAI-21)},
    year={2021}
}
```

## Third Party Work

Third party researchers have downloaded the documents and shared them on [Google Drive](https://drive.google.com/file/d/1uxMwiKMxgfKPuz0EnUxDHioUxeRJwPiZ), and [Baidu Pan](https://pan.baidu.com/s/1ztVj2l9yoQjXwCUmPYf2YQ) with passcode "wgta", for non-commercial usage only.

## Disclaimers

The code and data is provided as is, without warranty of any kind, express or implied.
