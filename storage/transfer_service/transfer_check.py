# Copyright 2015, Google, Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# [START all]
import argparse
import json
import logging

from apiclient import discovery
from oauth2client.client import GoogleCredentials


logging.basicConfig(level=logging.DEBUG)


# [START main]
def main(project_id, job_name):
    """Review the transfer operations associated with a transfer job."""
    credentials = GoogleCredentials.get_application_default()
    storagetransfer = discovery.build(
        'storagetransfer', 'v1', credentials=credentials)

    filterString = (
        '{{"project_id": "{project_id}", '
        '"job_names": ["{job_name}"]}}'
    ).format(project_id=project_id, job_name=job_name)

    result = storagetransfer.transferOperations().list(
        name="transferOperations",
        filter=filterString).execute()
    logging.info('Result of transferOperations/list: %s',
                 json.dumps(result, indent=4, sort_keys=True))
# [END main]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Review the transfer operations associated with a '
                    'transfer job.')
    parser.add_argument('project_id', help='Your Google Cloud project ID.')
    parser.add_argument('job_name', help='Your job name.')

    args = parser.parse_args()

    main(args.project_id, args.job_name)

# [END all]