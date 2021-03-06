# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RGB(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, r: int=None, g: int=None, b: int=None):  # noqa: E501
        """RGB - a model defined in Swagger

        :param r: The r of this RGB.  # noqa: E501
        :type r: int
        :param g: The g of this RGB.  # noqa: E501
        :type g: int
        :param b: The b of this RGB.  # noqa: E501
        :type b: int
        """
        self.swagger_types = {
            'r': int,
            'g': int,
            'b': int
        }

        self.attribute_map = {
            'r': 'r',
            'g': 'g',
            'b': 'b'
        }
        self._r = r
        self._g = g
        self._b = b

    @classmethod
    def from_dict(cls, dikt) -> 'RGB':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RGB of this RGB.  # noqa: E501
        :rtype: RGB
        """
        return util.deserialize_model(dikt, cls)

    @property
    def r(self) -> int:
        """Gets the r of this RGB.


        :return: The r of this RGB.
        :rtype: int
        """
        return self._r

    @r.setter
    def r(self, r: int):
        """Sets the r of this RGB.


        :param r: The r of this RGB.
        :type r: int
        """

        self._r = r

    @property
    def g(self) -> int:
        """Gets the g of this RGB.


        :return: The g of this RGB.
        :rtype: int
        """
        return self._g

    @g.setter
    def g(self, g: int):
        """Sets the g of this RGB.


        :param g: The g of this RGB.
        :type g: int
        """

        self._g = g

    @property
    def b(self) -> int:
        """Gets the b of this RGB.


        :return: The b of this RGB.
        :rtype: int
        """
        return self._b

    @b.setter
    def b(self, b: int):
        """Sets the b of this RGB.


        :param b: The b of this RGB.
        :type b: int
        """

        self._b = b
