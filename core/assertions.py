class Assert:
    @staticmethod
    def status_code(response, expected):
        assert response.status_code == expected, f"Expected {expected}, got {response.status_code}"

    @staticmethod
    def has_keys(json_object, keys: list):
        for key in keys:
            assert key in json_object, f"Missing key: {key}"

    @staticmethod
    def response_time(response, max_time=1.0):
        assert response.elapsed.total_seconds() < max_time, "API response too slow"
