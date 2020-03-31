# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.guard_agent import GuardAgent  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_agents_get(self):
        """Test case for agents_get

        Gets the information of an Agent
        """
        query_string = [('page_size', 100)]
        response = self.client.open(
            '/guard-api/agents',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_agents_id_delete(self):
        """Test case for agents_id_delete

        Deletes (unregisters) the Agent from the CB
        """
        response = self.client.open(
            '/guard-api/agents/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_agents_id_get(self):
        """Test case for agents_id_get

        Gets the properties of an agent.
        """
        response = self.client.open(
            '/guard-api/agents/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_agents_ping_id_put(self):
        """Test case for agents_ping_id_put

        Puts a ping to GUARD Agent
        """
        response = self.client.open(
            '/guard-api/agents/ping/{id}'.format(id='id_example'),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_agents_register_post(self):
        """Test case for agents_register_post

        Post a new GUARD Agent
        """
        agent = GuardAgent()
        response = self.client.open(
            '/guard-api/agents/register',
            method='POST',
            data=json.dumps(agent),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
