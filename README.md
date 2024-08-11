# NLP_Distilbert_Review_Consument
<p align="left">
<a  href= "https://github.com/psf/black">
  <img src="https://img.shields.io/badge/code%20style-black-000000.svg" 
  alt="Code style: black"
  ></a>
  <img src="https://img.shields.io/github/repo-size/ackermanjayjay/DS_Student-Perfomance" 
  alt="Size">
</p>

## Tools
<p align="left">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" 
  alt="FastApi">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" 
  alt="Python">
  <img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue" 
  alt="ML">
  </p>


## Objective

- Make model with data text review cloth with transfer learning distilbert/distilbert-base-uncased
- Make a API with FastAPI
- Hyperparameter Reference using with this paper [Journal Distilber](https://arxiv.org/pdf/1910.01108) and this [Journal bert](https://arxiv.org/pdf/1810.04805)



## Evaluation 
- 0 Negative review
- 1 Neutral review
- 2 Positive review

![eval](Eval.PNG)


## Api (deployment)
```
http://127.0.0.1:8000/prediction/text?query={your text}
```


```
{
  "data": {
    "input_text": "i love pretty soft shirt falls well want wear everyday",
    "result": "Positve"
  }
}
```




## Citation
```
@article{Sanh2019DistilBERTAD,
  title={DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter},
  author={Victor Sanh and Lysandre Debut and Julien Chaumond and Thomas Wolf},
  journal={ArXiv},
  year={2019},
  volume={abs/1910.01108}
}
```
