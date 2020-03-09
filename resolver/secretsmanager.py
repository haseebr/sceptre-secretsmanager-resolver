import logging

from botocore.exceptions import ClientError
from sceptre.resolvers import Resolver
import json


class SecretsManagerResolver(Resolver):
    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(__name__)
        super(SecretsManagerResolver, self).__init__(*args, **kwargs)

    def resolve(self):

        self.logger.debug(
            "GetSecretValue: {0}".format(self.argument['SecretId'])
        )

        value = None

        profile = self.stack.profile
        region = self.stack.region
        secret_params = self.argument

        json_key = None
        if 'JsonKey' in self.argument:
            json_key = secret_params['JsonKey']
            del secret_params['JsonKey']

        if self.argument:
            value = self._get_secret_value(secret_params, profile, region)

        if json_key:
            SecretString = json.loads(value['SecretString'])
            return SecretString[json_key]
        else:
            return value

    def _get_secret_value(self, secret, profile=None, region=None):

        connection_manager = self.stack.connection_manager

        try:
            response = connection_manager.call(
                service="secretsmanager",
                command="get_secret_value",
                kwargs=secret,
                profile=profile,
                region=region
            )
        except ClientError as e:
            raise e
        else:
            return response
