from ya_api import YaDiskApi


def test_ya_api_new_dir():
    ya_api = YaDiskApi()
    result = ya_api.new_dir('test_dir')
    assert result.status_code == 201


def test_ya_api_exist_dir():
    ya_api = YaDiskApi()
    result = ya_api.info_dir('test_dir')
    assert result.status_code == 200


def test_ya_api_delete_dir():
    ya_api = YaDiskApi()
    result = ya_api.delete_dir('test_dir')
    assert result.status_code == 204
