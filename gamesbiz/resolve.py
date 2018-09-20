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


class sagemaker(object):

    @staticmethod
    def check():
        path = os.path.join(*[os.sep, 'opt', 'ml'])
        return os.path.exists(path)

    @staticmethod
    def model(filename):
        return os.path.join(*[os.sep, 'opt', 'ml', 'model', filename])

    @staticmethod
    def input(channel, filename):
        return os.path.join(*[os.sep, 'opt', 'ml', 'input', 'data', channel, filename])

    @staticmethod
    def failure():
        return os.path.join(*[os.sep, 'opt', 'ml', 'output', 'failure'])

    @staticmethod
    def output(filename):
        return os.path.join(*[os.sep, 'opt', 'ml', 'model', filename])


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