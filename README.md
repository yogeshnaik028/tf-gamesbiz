## Packaged Python Algorithm for Predicting Video Games Earnings

----

The aim of this project is to serve as a simple example of implementing tensorflow model to be used with the [sagemaker-pipeline]() project .

### Prerequisites

1. Make sure to have setuptools library installed on python

2. Using version 3.6+ of python

3. Specify the "entry_point" in _setup.py_ which is the actual function SageMaker execute to run the container where as "gamesbiz.train" should refer to the

```
setup(
   ...

     entry_point={
        "gamesbiz.train":"entry_point"
    }

   ...
)
```
**Note**: As you can see above we assume that the setup() function requires the additional *entry_point={...}* argument which allows the
pipeline to abstract out all the information needed to build a SageMaker compatible docker image.

### Description of Model

Its a simple fully connected neural network model (multilayer preceptron)
The training and testing data set are mounted to the SageMaker managed docker container in "/opt/ml/input/data/training"
The Trained model artifact can be saved to "/opt/ml/output/model" within the container and this gets zipped and pushed to S3 location

**Note**:
Since this is a simple example, data is fed to the tensorflow model an array that was pre-loaded into memory.

----

### Built primarily With

* [Tensorflow](https://www.tensorflow.org/) - Open Source Machine Learning framework


### Authors

* **Mustafa Waheed** - *Data Scientist* 
