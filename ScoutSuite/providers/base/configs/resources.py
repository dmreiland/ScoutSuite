# -*- coding: utf-8 -*-

import abc


class Resources(dict, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    async def fetch_all(self, **kwargs):
        raise NotImplementedError()


class SimpleResources(Resources, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def parse_resource(self, resource):
        raise NotImplementedError

    @abc.abstractmethod
    async def get_resources_from_api(self, **kwargs):
        raise NotImplementedError


class CompositeResources(Resources, metaclass=abc.ABCMeta):

    # The following enforces that classes which inherits from CompositeResources define a `children` attribute:
    @property
    @abc.abstractmethod
    def children(self):
        raise NotImplementedError

    @abc.abstractmethod
    async def fetch_children(self, **kwargs):
        raise NotImplementedError
