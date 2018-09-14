import pkgutil
import sys
import os
import types

import gamesbiz.data as location


class resource(object):
    @staticmethod
    def filename(package, filename):

        if isinstance(package, types.ModuleType):
            mod = package
        else:
            loader = pkgutil.get_loader(package)
            if loader is None or not hasattr(loader, 'get_data'):
                return None
            mod = sys.modules.get(package) or loader.load_module(package)
            if mod is None or not hasattr(mod, '__file__'):
                return None

        parts = filename.split('/')
        parts.insert(0, os.path.dirname(mod.__file__))
        return os.path.join(*parts)

    @staticmethod
    def exists(package, filename):
        return os.path.exists(resource.filename(package, filename))

    @staticmethod
    def stream(package, filename):
        return open(resource.filename(package, filename), 'r')

    @staticmethod
    def isdir(package, filename):
        os.path.isdir(resource.filename(package, filename))

    @staticmethod
    def listdir(package, filename):
        os.listdir(resource.filename(package, filename))

    @staticmethod
    def string(package, filename):
        with open(resource.filename(package, filename), 'r') as handle:
            return handle.read()


# ------------------------------------------------------------------------------
# SageMaker Paths
# ------------------------------------------------------------------------------

class sagemaker(object):

    @staticmethod
    def check():
        """
        Checks if we are running in a SageMaker context

        Returns:
            result (bool): Whether or not standard SageMaker paths exist
        """
        path = os.path.join(*[os.sep, 'opt', 'ml'])
        return os.path.exists(path)

    @staticmethod
    def model(filename):
        """
        The path to model artifacts.

        Your algorithm should write all final model artifacts to this directory.
        Amazon SageMaker copies this data as a single object in compressed tar
        format to the S3 location that you specified in the CreateTrainingJob
        request. If multiple containers in a single training job write to this
        directory they should ensure no file/directory names clash. Amazon
        SageMaker aggregates the result in a tar file and uploads to S3.

        Arguments:
            filename (str): The name of the file which will be written to S3
        Returns:
            path (str): The absolute path to the model output directory
        """
        return os.path.join(*[os.sep, 'opt', 'ml', 'model', filename])

    @staticmethod
    def input(channel, filename):
        """
        The path to input artifacts.

        Amazon SageMaker allows you to specify "channels" for your docker container.
        The purpose of a channel is to copy data from S3 to a specified directory.
        Amazon SageMaker makes the data for the channel available in the
        /opt/ml/input/data/channel_name directory in the Docker container.
        For example, if you have three channels named training, validation, and
        testing, Amazon SageMaker makes three directories in the Docker container:

            /opt/ml/input/data/training
            /opt/ml/input/data/validation
            /opt/ml/input/data/testing

        Arguments:
            channel (str): The name of the channel which contains the filename
            filename (str): The name of the file within a specific channel
        Returns:
            path (str): The absolute path to the specified channel file
        """
        return os.path.join(*[os.sep, 'opt', 'ml', 'input', 'data', channel, filename])

    @staticmethod
    def failure():
        """
        The path to the failure file.

        If training fails, after all algorithm output (for example, logging)
        completes, your algorithm should write the failure description to this
        file.

        Returns:
            path (str): The absolute path to the failure file
        """
        return os.path.join(*[os.sep, 'opt', 'ml', 'output', 'failure'])

    @staticmethod
    def output(filename):
        """
        The path to the output artifacts.
        Your algorithm should write all final model artifacts to this directory.
        Amazon SageMaker copies this data as a single object in compressed tar
        format to the S3 location that you specified in the CreateTrainingJob
        request. If multiple containers in a single training job write to this
        directory they should ensure no file/directory names clash. Amazon SageMaker
        aggregates the result in a tar file and uploads to S3.
        Arguments:
            filename (str): The name of the file which will be written back to S3
        Returns:
            path (str): The absolute path to the model output directory
        """
        return os.path.join(*[os.sep, 'opt', 'ml', 'model', filename])


# ------------------------------------------------------------------------------
# Local Paths
# ------------------------------------------------------------------------------

class local(object):

    @staticmethod
    def model(filename):
        return resource.filename(location, filename)

    @staticmethod
    def input(channel, filename):
        return resource.filename(location, filename)

    @staticmethod
    def failure():
        return resource.filename(location, 'failure')

    @staticmethod
    def output(filename):
        return resource.filename(location, filename)


# ------------------------------------------------------------------------------
# Path Selector
# ------------------------------------------------------------------------------

class paths(object):

    @staticmethod
    def base():
        if sagemaker.check():
            return sagemaker
        return local

    @staticmethod
    def model(filename):
        return paths.base().model(filename)

    @staticmethod
    def input(channel, filename):
        return paths.base().input(channel, filename)

    @staticmethod
    def failure():
        return paths.base().failure()

    @staticmethod
    def output(filename):
        return paths.base().output(filename)