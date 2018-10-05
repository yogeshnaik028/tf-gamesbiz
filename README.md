## Packaged Python Algorithm for Predicting Video Games Earnings

----

The aim of this project is to serve as a simple example of implementing tensorflow model to be used with the [sagemaker-pipeline](https://github.com/MustafaWaheed91/sagemaker-pipeline) project.

### Prerequisites

1. Make sure to have setuptools library installed on python

2. Using version 3.6+ of python

3. Specify the "entry_point" in setup.py which is the actual function SageMaker execute to run the container where as "gamesbiz.train" should refer to the module or sub-module path (depending on the contents of the __init__.py at the top level of the module)

### Running Model locally

```

git clone https://github.com/MustafaWaheed91/tf-gamesbiz.git

cd tf-gamesbiz

pip3 install -e .

python3 gamesbiz/train.py

```


----

### Built primarily with

* [Tensorflow](https://www.tensorflow.org/) - Open Source Machine Learning framework


### Authors

* **Mustafa Waheed** - *Data Scientist* 
