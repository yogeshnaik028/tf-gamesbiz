## Packaged Python Algorithm for Predicting Video Game Earnings

----

The aim of this project is to serve as a simple example of implementing a model in tensorflow.

### Prerequisites

1. Make sure to have setuptools library installed on python

2. Using version 3.6+ of python

3. Specify the "entry_point" in _setup.py_ which is the actual function SageMaker execute to run the container

````
setup(
   ...

     entry_point={
        "gamesbiz.train":"entry_point"
    }

   ...
)
````

### Description of Model

Its a simple fully connected neural network model (preceptron) with hyperparameters.json showing the hyperparameter values


**Note**:
Since this is a simple example, data is fed to the tensorflow model an array that was pre-loaded into memory.

----

### Built primarily With

* [Tensorflow](https://www.tensorflow.org/) - Open Source Machine Learning framework


### Authors

* **Mustafa Waheed** - *Data Scientist* 
