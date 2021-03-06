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
import json

import tests

from .async_query import main


class TestAsyncQuery(tests.CloudBaseTest):

    def test_async_query(self):
        query = (
            'SELECT corpus FROM publicdata:samples.shakespeare '
            'GROUP BY corpus;')

        with tests.capture_stdout() as stdout:
            main(
                project_id=self.project_id,
                query_string=query,
                batch=False,
                num_retries=5,
                interval=1)

        value = stdout.getvalue().strip().split('\n').pop()

        self.assertIsNotNone(
            json.loads(value))
