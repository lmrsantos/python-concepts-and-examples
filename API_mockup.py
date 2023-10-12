import unittest.mock

class MockAPI:
    def get_users(self):
        return [{'name': 'John'}, {'name': 'Alex'}, {'name': 'Mary'}]

@unittest.mock.patch('api.API', MockAPI)
def test_get_users(mock_api):
    api = api.API()
    users = api.get_users()
    assert len(users) == 3
    assert users[0]['name'] == 'John'
    assert users[1]['name'] == 'Alex'
    assert users[2]['name'] == 'Mary'

if __name__ == '__main__':
    unittest.main()
