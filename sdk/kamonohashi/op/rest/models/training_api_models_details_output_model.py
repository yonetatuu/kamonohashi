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

from kamonohashi.op.rest.models.components_container_image_output_model import ComponentsContainerImageOutputModel  # noqa: F401,E501
from kamonohashi.op.rest.models.components_git_commit_output_model import ComponentsGitCommitOutputModel  # noqa: F401,E501
from kamonohashi.op.rest.models.data_set_api_models_index_output_model import DataSetApiModelsIndexOutputModel  # noqa: F401,E501
from kamonohashi.op.rest.models.system_collections_generic_key_value_pair import SystemCollectionsGenericKeyValuePair  # noqa: F401,E501
from kamonohashi.op.rest.models.training_api_models_simple_output_model import TrainingApiModelsSimpleOutputModel  # noqa: F401,E501


class TrainingApiModelsDetailsOutputModel(object):
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
        'completed_at': 'str',
        'condition_note': 'str',
        'container_image': 'ComponentsContainerImageOutputModel',
        'cpu': 'int',
        'created_at': 'str',
        'created_by': 'str',
        'data_set': 'DataSetApiModelsIndexOutputModel',
        'display_id': 'int',
        'entry_point': 'str',
        'execution_time': 'str',
        'favorite': 'bool',
        'full_name': 'str',
        'git_model': 'ComponentsGitCommitOutputModel',
        'gpu': 'int',
        'id': 'int',
        'key': 'str',
        'log_summary': 'str',
        'memo': 'str',
        'memory': 'int',
        'modified_at': 'str',
        'modified_by': 'str',
        'name': 'str',
        'node': 'str',
        'options': 'list[SystemCollectionsGenericKeyValuePair]',
        'parent': 'TrainingApiModelsSimpleOutputModel',
        'partition': 'str',
        'started_at': 'str',
        'status': 'str',
        'status_type': 'str',
        'waiting_time': 'str'
    }

    attribute_map = {
        'completed_at': 'completedAt',
        'condition_note': 'conditionNote',
        'container_image': 'containerImage',
        'cpu': 'cpu',
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'data_set': 'dataSet',
        'display_id': 'displayId',
        'entry_point': 'entryPoint',
        'execution_time': 'executionTime',
        'favorite': 'favorite',
        'full_name': 'fullName',
        'git_model': 'gitModel',
        'gpu': 'gpu',
        'id': 'id',
        'key': 'key',
        'log_summary': 'logSummary',
        'memo': 'memo',
        'memory': 'memory',
        'modified_at': 'modifiedAt',
        'modified_by': 'modifiedBy',
        'name': 'name',
        'node': 'node',
        'options': 'options',
        'parent': 'parent',
        'partition': 'partition',
        'started_at': 'startedAt',
        'status': 'status',
        'status_type': 'statusType',
        'waiting_time': 'waitingTime'
    }

    def __init__(self, completed_at=None, condition_note=None, container_image=None, cpu=None, created_at=None, created_by=None, data_set=None, display_id=None, entry_point=None, execution_time=None, favorite=None, full_name=None, git_model=None, gpu=None, id=None, key=None, log_summary=None, memo=None, memory=None, modified_at=None, modified_by=None, name=None, node=None, options=None, parent=None, partition=None, started_at=None, status=None, status_type=None, waiting_time=None):  # noqa: E501
        """TrainingApiModelsDetailsOutputModel - a model defined in Swagger"""  # noqa: E501

        self._completed_at = None
        self._condition_note = None
        self._container_image = None
        self._cpu = None
        self._created_at = None
        self._created_by = None
        self._data_set = None
        self._display_id = None
        self._entry_point = None
        self._execution_time = None
        self._favorite = None
        self._full_name = None
        self._git_model = None
        self._gpu = None
        self._id = None
        self._key = None
        self._log_summary = None
        self._memo = None
        self._memory = None
        self._modified_at = None
        self._modified_by = None
        self._name = None
        self._node = None
        self._options = None
        self._parent = None
        self._partition = None
        self._started_at = None
        self._status = None
        self._status_type = None
        self._waiting_time = None
        self.discriminator = None

        if completed_at is not None:
            self.completed_at = completed_at
        if condition_note is not None:
            self.condition_note = condition_note
        if container_image is not None:
            self.container_image = container_image
        if cpu is not None:
            self.cpu = cpu
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
        if execution_time is not None:
            self.execution_time = execution_time
        if favorite is not None:
            self.favorite = favorite
        if full_name is not None:
            self.full_name = full_name
        if git_model is not None:
            self.git_model = git_model
        if gpu is not None:
            self.gpu = gpu
        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if log_summary is not None:
            self.log_summary = log_summary
        if memo is not None:
            self.memo = memo
        if memory is not None:
            self.memory = memory
        if modified_at is not None:
            self.modified_at = modified_at
        if modified_by is not None:
            self.modified_by = modified_by
        if name is not None:
            self.name = name
        if node is not None:
            self.node = node
        if options is not None:
            self.options = options
        if parent is not None:
            self.parent = parent
        if partition is not None:
            self.partition = partition
        if started_at is not None:
            self.started_at = started_at
        if status is not None:
            self.status = status
        if status_type is not None:
            self.status_type = status_type
        if waiting_time is not None:
            self.waiting_time = waiting_time

    @property
    def completed_at(self):
        """Gets the completed_at of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The completed_at of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """Sets the completed_at of this TrainingApiModelsDetailsOutputModel.


        :param completed_at: The completed_at of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._completed_at = completed_at

    @property
    def condition_note(self):
        """Gets the condition_note of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The condition_note of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._condition_note

    @condition_note.setter
    def condition_note(self, condition_note):
        """Sets the condition_note of this TrainingApiModelsDetailsOutputModel.


        :param condition_note: The condition_note of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._condition_note = condition_note

    @property
    def container_image(self):
        """Gets the container_image of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The container_image of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: ComponentsContainerImageOutputModel
        """
        return self._container_image

    @container_image.setter
    def container_image(self, container_image):
        """Sets the container_image of this TrainingApiModelsDetailsOutputModel.


        :param container_image: The container_image of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: ComponentsContainerImageOutputModel
        """

        self._container_image = container_image

    @property
    def cpu(self):
        """Gets the cpu of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The cpu of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this TrainingApiModelsDetailsOutputModel.


        :param cpu: The cpu of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: int
        """

        self._cpu = cpu

    @property
    def created_at(self):
        """Gets the created_at of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The created_at of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TrainingApiModelsDetailsOutputModel.


        :param created_at: The created_at of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The created_by of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this TrainingApiModelsDetailsOutputModel.


        :param created_by: The created_by of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def data_set(self):
        """Gets the data_set of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The data_set of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: DataSetApiModelsIndexOutputModel
        """
        return self._data_set

    @data_set.setter
    def data_set(self, data_set):
        """Sets the data_set of this TrainingApiModelsDetailsOutputModel.


        :param data_set: The data_set of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: DataSetApiModelsIndexOutputModel
        """

        self._data_set = data_set

    @property
    def display_id(self):
        """Gets the display_id of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The display_id of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: int
        """
        return self._display_id

    @display_id.setter
    def display_id(self, display_id):
        """Sets the display_id of this TrainingApiModelsDetailsOutputModel.


        :param display_id: The display_id of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: int
        """

        self._display_id = display_id

    @property
    def entry_point(self):
        """Gets the entry_point of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The entry_point of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._entry_point

    @entry_point.setter
    def entry_point(self, entry_point):
        """Sets the entry_point of this TrainingApiModelsDetailsOutputModel.


        :param entry_point: The entry_point of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._entry_point = entry_point

    @property
    def execution_time(self):
        """Gets the execution_time of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The execution_time of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        """Sets the execution_time of this TrainingApiModelsDetailsOutputModel.


        :param execution_time: The execution_time of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._execution_time = execution_time

    @property
    def favorite(self):
        """Gets the favorite of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The favorite of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this TrainingApiModelsDetailsOutputModel.


        :param favorite: The favorite of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: bool
        """

        self._favorite = favorite

    @property
    def full_name(self):
        """Gets the full_name of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The full_name of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this TrainingApiModelsDetailsOutputModel.


        :param full_name: The full_name of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def git_model(self):
        """Gets the git_model of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The git_model of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: ComponentsGitCommitOutputModel
        """
        return self._git_model

    @git_model.setter
    def git_model(self, git_model):
        """Sets the git_model of this TrainingApiModelsDetailsOutputModel.


        :param git_model: The git_model of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: ComponentsGitCommitOutputModel
        """

        self._git_model = git_model

    @property
    def gpu(self):
        """Gets the gpu of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The gpu of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: int
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        """Sets the gpu of this TrainingApiModelsDetailsOutputModel.


        :param gpu: The gpu of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: int
        """

        self._gpu = gpu

    @property
    def id(self):
        """Gets the id of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The id of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrainingApiModelsDetailsOutputModel.


        :param id: The id of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The key of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TrainingApiModelsDetailsOutputModel.


        :param key: The key of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def log_summary(self):
        """Gets the log_summary of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The log_summary of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._log_summary

    @log_summary.setter
    def log_summary(self, log_summary):
        """Sets the log_summary of this TrainingApiModelsDetailsOutputModel.


        :param log_summary: The log_summary of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._log_summary = log_summary

    @property
    def memo(self):
        """Gets the memo of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The memo of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this TrainingApiModelsDetailsOutputModel.


        :param memo: The memo of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._memo = memo

    @property
    def memory(self):
        """Gets the memory of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The memory of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this TrainingApiModelsDetailsOutputModel.


        :param memory: The memory of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: int
        """

        self._memory = memory

    @property
    def modified_at(self):
        """Gets the modified_at of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The modified_at of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this TrainingApiModelsDetailsOutputModel.


        :param modified_at: The modified_at of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._modified_at = modified_at

    @property
    def modified_by(self):
        """Gets the modified_by of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The modified_by of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this TrainingApiModelsDetailsOutputModel.


        :param modified_by: The modified_by of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def name(self):
        """Gets the name of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The name of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrainingApiModelsDetailsOutputModel.


        :param name: The name of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def node(self):
        """Gets the node of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The node of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this TrainingApiModelsDetailsOutputModel.


        :param node: The node of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._node = node

    @property
    def options(self):
        """Gets the options of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The options of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: list[SystemCollectionsGenericKeyValuePair]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this TrainingApiModelsDetailsOutputModel.


        :param options: The options of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: list[SystemCollectionsGenericKeyValuePair]
        """

        self._options = options

    @property
    def parent(self):
        """Gets the parent of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The parent of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: TrainingApiModelsSimpleOutputModel
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this TrainingApiModelsDetailsOutputModel.


        :param parent: The parent of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: TrainingApiModelsSimpleOutputModel
        """

        self._parent = parent

    @property
    def partition(self):
        """Gets the partition of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The partition of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this TrainingApiModelsDetailsOutputModel.


        :param partition: The partition of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._partition = partition

    @property
    def started_at(self):
        """Gets the started_at of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The started_at of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this TrainingApiModelsDetailsOutputModel.


        :param started_at: The started_at of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._started_at = started_at

    @property
    def status(self):
        """Gets the status of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The status of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TrainingApiModelsDetailsOutputModel.


        :param status: The status of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_type(self):
        """Gets the status_type of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The status_type of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._status_type

    @status_type.setter
    def status_type(self, status_type):
        """Sets the status_type of this TrainingApiModelsDetailsOutputModel.


        :param status_type: The status_type of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._status_type = status_type

    @property
    def waiting_time(self):
        """Gets the waiting_time of this TrainingApiModelsDetailsOutputModel.  # noqa: E501


        :return: The waiting_time of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._waiting_time

    @waiting_time.setter
    def waiting_time(self, waiting_time):
        """Sets the waiting_time of this TrainingApiModelsDetailsOutputModel.


        :param waiting_time: The waiting_time of this TrainingApiModelsDetailsOutputModel.  # noqa: E501
        :type: str
        """

        self._waiting_time = waiting_time

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
        if issubclass(TrainingApiModelsDetailsOutputModel, dict):
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
        if not isinstance(other, TrainingApiModelsDetailsOutputModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
