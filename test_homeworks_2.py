import pytest
import requests


class TestYandexDisk:
    def setup_method(self):
        self.headers = {
            'Authorization': 'OAuth y0_AgAAAAAY6IDtAADLWwAAAAEA3DVEAAAGuLLWBHVKvIgXYPfYxcwVbg_ZQA'
        }

    @pytest.mark.parametrize(
        'key, value, statuscode',
        (
                ['pat', 'Test', 400],
                ['path', 'Test', 201],
                ['path', 'Test', 409]

        )
    )
    def test_create_folders(self, key, value, statuscode):
        params = {key: value}
        response = requests.put(
            'https://cloud-api.yandex.net/v1/disk/resources',
            headers=self.headers, params=params)
        assert response.status_code == statuscode
