# coding: utf-8

"""
    KAMONOHASHI API

    A platform for deep learning  # noqa: E501

    OpenAPI spec version: v1
    Contact: kamonohashi-support@jp.nssol.nipponsteel.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from kamonohashi.op.rest.models.data_set_api_models_index_output_model import DataSetApiModelsIndexOutputModel  # noqa: F401,E501


class InferenceApiModelsInferenceIndexOutputModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'created_at': 'str',
        'created_by': 'str',
        'data_set': 'DataSetApiModelsIndexOutputModel',
        'display_id': 'int',
        'entry_point': 'str',
        'favorite': 'bool',
        'full_name': 'str',
        'id': 'int',
        'memo': 'str',
        'modified_at': 'str',
        'modified_by': 'str',
        'name': 'str',
        'output_value': 'str',
        'parent_name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'data_set': 'dataSet',
        'display_id': 'displayId',
        'entry_point': 'entryPoint',
        'favorite': 'favorite',
        'full_name': 'fullName',
        'id': 'id',
        'memo': 'memo',
        'modified_at': 'modifiedAt',
        'modified_by': 'modifiedBy',
        'name': 'name',
        'output_value': 'outputValue',
        'parent_name': 'parentName',
        'status': 'status'
    }

    def __init__(self, created_at=None, created_by=None, data_set=None, display_id=None, entry_point=None, favorite=None, full_name=None, id=None, memo=None, modified_at=None, modified_by=None, name=None, output_value=None, parent_name=None, status=None):  # noqa: E501
        """InferenceApiModelsInferenceIndexOutputModel - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._created_by = None
        self._data_set = None
        self._display_id = None
        self._entry_point = None
        self._favorite = None
        self._full_name = None
        self._id = None
        self._memo = None
        self._modified_at = None
        self._modified_by = None
        self._name = None
        self._output_value = None
        self._parent_name = None
        self._status = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if data_set is not None:
            self.data_set = data_set
        if display_id is not None:
            self.display_id = display_id
        if entry_point is not None:
            self.entry_point = entry_point
        if favorite is not None:
            self.favorite = favorite
        if full_name is not None:
            self.full_name = full_name
        if id is not None:
            self.id = id
        if memo is not None:
            self.memo = memo
        if modified_at is not None:
            self.modified_at = modified_at
        if modified_by is not None:
            self.modified_by = modified_by
        if name is not None:
            self.name = name
        if output_value is not None:
            self.output_value = output_value
        if parent_name is not None:
            self.parent_name = parent_name
        if status is not None:
            self.status = status

    @property
    def created_at(self):
        """Gets the created_at of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501


        :return: The created_at of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InferenceApiModelsInferenceIndexOutputModel.


        :param created_at: The created_at of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501


        :return: The created_by of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this InferenceApiModelsInferenceIndexOutputModel.


        :param created_by: The created_by of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def data_set(self):
        """Gets the data_set of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501


        :return: The data_set of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :rtype: DataSetApiModelsIndexOutputModel
        """
        return self._data_set

    @data_set.setter
    def data_set(self, data_set):
        """Sets the data_set of this InferenceApiModelsInferenceIndexOutputModel.


        :param data_set: The data_set of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :type: DataSetApiModelsIndexOutputModel
        """

        self._data_set = data_set

    @property
    def display_id(self):
        """Gets the display_id of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501


        :return: The display_id of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :rtype: int
        """
        return self._display_id

    @display_id.setter
    def display_id(self, display_id):
        """Sets the display_id of this InferenceApiModelsInferenceIndexOutputModel.


        :param display_id: The display_id of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :type: int
        """

        self._display_id = display_id

    @property
    def entry_point(self):
        """Gets the entry_point of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501


        :return: The entry_point of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._entry_point

    @entry_point.setter
    def entry_point(self, entry_point):
        """Sets the entry_point of this InferenceApiModelsInferenceIndexOutputModel.


        :param entry_point: The entry_point of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :type: str
        """

        self._entry_point = entry_point

    @property
    def favorite(self):
        """Gets the favorite of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501


        :return: The favorite of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this InferenceApiModelsInferenceIndexOutputModel.


        :param favorite: The favorite of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :type: bool
        """

        self._favorite = favorite

    @property
    def full_name(self):
        """Gets the full_name of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501


        :return: The full_name of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this InferenceApiModelsInferenceIndexOutputModel.


        :param full_name: The full_name of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def id(self):
        """Gets the id of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501


        :return: The id of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InferenceApiModelsInferenceIndexOutputModel.


        :param id: The id of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def memo(self):
        """Gets the memo of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501


        :return: The memo of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this InferenceApiModelsInferenceIndexOutputModel.


        :param memo: The memo of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :type: str
        """

        self._memo = memo

    @property
    def modified_at(self):
        """Gets the modified_at of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501


        :return: The modified_at of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this InferenceApiModelsInferenceIndexOutputModel.


        :param modified_at: The modified_at of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :type: str
        """

        self._modified_at = modified_at

    @property
    def modified_by(self):
        """Gets the modified_by of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501


        :return: The modified_by of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this InferenceApiModelsInferenceIndexOutputModel.


        :param modified_by: The modified_by of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def name(self):
        """Gets the name of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501


        :return: The name of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InferenceApiModelsInferenceIndexOutputModel.


        :param name: The name of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def output_value(self):
        """Gets the output_value of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501


        :return: The output_value of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._output_value

    @output_value.setter
    def output_value(self, output_value):
        """Sets the output_value of this InferenceApiModelsInferenceIndexOutputModel.


        :param output_value: The output_value of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :type: str
        """

        self._output_value = output_value

    @property
    def parent_name(self):
        """Gets the parent_name of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501


        :return: The parent_name of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        """Sets the parent_name of this InferenceApiModelsInferenceIndexOutputModel.


        :param parent_name: The parent_name of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :type: str
        """

        self._parent_name = parent_name

    @property
    def status(self):
        """Gets the status of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501


        :return: The status of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InferenceApiModelsInferenceIndexOutputModel.


        :param status: The status of this InferenceApiModelsInferenceIndexOutputModel.  # noqa: E501
        :type: str
        """

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InferenceApiModelsInferenceIndexOutputModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InferenceApiModelsInferenceIndexOutputModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
