import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.guard_agent import GuardAgent  # noqa: E501
from swagger_server import util

from swagger_server.controllers.Store import Store
import json

store = Store()
agents=[]

def agents_get(page_size=None):  # noqa: E501
    """Gets the information of an Agent

    Gets a list of Agents and their security properites # noqa: E501

    :param page_size: Number of agents returned
    :type page_size: int

    :rtype: List[GuardAgent]
    """
    res=[]
    for e in agents:
        agent_data_str = store.get(e)
        agent_data_str=agent_data_str.replace("\'", "\"")
        agent_data_str=agent_data_str.replace(": None", ": {}")
        r=json.loads(agent_data_str)
        agent_data=GuardAgent.from_dict(r)
        res.append(agent_data)

    if len(res) > 0:
        return res, 200

    return None, 404


def agents_id_delete(id):  # noqa: E501
    """Deletes (unregisters) the Agent from the CB

    Unsets the agent Security Properties # noqa: E501

    :param id: The ID of an already registered agent
    :type id: str

    :rtype: None
    """
    if id in agents:
        store.delete(id)
        agents.remove(id)
        return None, 204
    return None, 404


def agents_id_get(id):  # noqa: E501
    """Gets the properties of an agent.

    Queries an agent # noqa: E501

    :param id: The ID of an already registered agent
    :type id: str

    :rtype: GuardAgent
    """
    if id in agents:
        agent_data_str = store.get(id)
        agent_data_str=agent_data_str.replace("\'", "\"")
        agent_data_str=agent_data_str.replace(": None", ": {}")
        r=json.loads(agent_data_str)
        agent_data=GuardAgent.from_dict(r)
        return agent_data, 200
    return None, 404


def agents_ping_id_put(id):  # noqa: E501
    """Puts a ping to GUARD Agent

    Sets a ping to the agent. # noqa: E501

    :param id: The ID of an already registered agent
    :type id: str

    :rtype: None
    """
    if id in agents:
        return None, 204
    return None, 204

def agents_register_post(agent=None):  # noqa: E501
    """Post a new GUARD Agent

    Sets the the agent Security Properties # noqa: E501

    :param agent: 
    :type agent: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        agent = GuardAgent.from_dict(connexion.request.get_json())  # noqa: E501
        if agent.id not in agents:
            agents.append(agent.id)
            store.set(agent.id, agent.to_str())
            return None, 204
        else:
            return None, 422
