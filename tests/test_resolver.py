

test_strings = [
    'MySecret::SecretString::password::SecretString::EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE}}',
    'arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret-asd123}}',
    'arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret-asd123::SecretString::password}}',
    'arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecretName-asd123::SecretString::password::AWSPENDING}}'
]


class TestStackActions(object):
    def setup_method(self, test_method):
        pass

    def test_dummy_test(self):
        print("\n")
        for test_string in test_strings:
            print(test_string.split("::"))
