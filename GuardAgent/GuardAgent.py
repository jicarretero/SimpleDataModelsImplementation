#!/usr/bin/env python3

# from __future__ import print_function
import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.guard_agent import GuardAgent

import threading
from swagger_client.GuardAgentSecurityContext import GuardAgentSecurityContext
from swagger_client.models.security_properties import SecurityProperties
from swagger_client.models.security_properties_value import SecurityPropertiesValue
from swagger_client.models.configuration_properties import ConfigurationProperties
from swagger_client.models.configuration_properties_value import ConfigurationPropertiesValue
from swagger_client.models.data_schema import DataSchema
from swagger_client.api.default_api import DefaultApi
from swagger_client.api.orion_api_client import OrionApi

from typing import List

configuration = swagger_client.Configuration()
api_instance = DefaultApi(swagger_client.ApiClient(configuration))
# api_instance = OrionApi(swagger_client.ApiClient(configuration))

id = "urn:guard:agent:openstack:00000001"

def server_thread():
    import connexion
    # from swagger_server import encoder

    #app = connexion.App(__name__, specification_dir='./swagger_server/swagger/')
    #app.app.json_encoder = encoder.JSONEncoder
    #app.add_api('swagger.yaml', arguments={'title': 'First Approach to an GUARD Programmability API'})
    #app.run(port=3036)
    pass


def ping_thread():
    import time
    time.sleep(2)
    security_context=GuardAgentSecurityContext()
    while True:
        time.sleep(security_context.time_between_pings())
        api_response = api_instance.agents_ping_agent_urn_put(id)
        print("Ping:",api_response.status)

def get_guard_security_agent_data():
    type = "GuardAgent"
    name=id
    vendor="FIWARE Foundation e.V."
    patch=""
    version="0.0.2"
    callback_url="http://localhost:3033/guard-agent"
    sp_value = SecurityPropertiesValue(name, version, vendor, patch, callback_url)
    sp = SecurityProperties(type, sp_value)

    cp_time_between_probes = ConfigurationPropertiesValue("time_between_probes", "ConfigurationProperty", "", "60")
    cp_time_between_pings  = ConfigurationPropertiesValue("time_between_pings", "ConfigurationProperty", "", "60")
    cp = ConfigurationProperties("configurations", [cp_time_between_probes, cp_time_between_pings])

    ds = DataSchema("url",
               value="https://raw.githubusercontent.com/jicarretero/DataModels/master/examples/openstack_compute_node/openstack_compute_node.json")
    return GuardAgent(id, type, cp, sp, ds)

def get_guard_security_agent_data_2():
    fooid = "urn:guard:agent:openstack:00000foo"
    type = "GuardAgent"
    name=fooid
    vendor="FIWARE Foundation e.V."
    patch=""
    version="0.0.3"
    callback_url="http://localhost:3044/guard-agent-2"
    sp_value = SecurityPropertiesValue(name, version, vendor, patch, callback_url)
    sp = SecurityProperties(type, sp_value)

    cp_time_between_probes = ConfigurationPropertiesValue("time_between_probes", "ConfigurationProperty", "", "25")
    cp_time_between_pings  = ConfigurationPropertiesValue("time_between_pings", "ConfigurationProperty", "", "25")
    foo_property  = ConfigurationPropertiesValue("third_property", "ConfigurationProperty", "", "nomatterwhat")
    cp = ConfigurationProperties("configurations", [cp_time_between_probes, cp_time_between_pings, foo_property])

    ds = DataSchema("url",
                    value="https://raw.githubusercontent.com/jicarretero/DataModels/master/examples/openstack_compute_node/openstack_compute_node.json")
    return GuardAgent(fooid, type, cp, sp, ds)

try:
    #t_server=threading.Thread(target=server_thread)
    #t_server.start()

    #t_ping=threading.Thread(target=ping_thread)
    #t_ping.start()

    agent = get_guard_security_agent_data()
    agent2 = get_guard_security_agent_data_2()

    print(agent.to_str())
    print()

    agent_d = {"agent": agent.to_dict() }
    try:
        api_response = api_instance.agents_register_post(**agent_d)
    except ApiException as e:
        print(e)

    agent_d = {"agent": agent2.to_dict() }
    try:
       api_response = api_instance.agents_register_post(**agent_d)
    except ApiException as e:
       print(e.__dict__)
except ApiException as e:
    print("-------------------------------------")
    print(e)
    # print("Exception when calling DefaultApi->agents_agent_urn_get: %s\n" % e)
