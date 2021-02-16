#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python example script showing SecureX Cloud Analytics Alerts.

Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

import requests

def get_my_python_app_status(

):
    url = f"http://54.237.88.112:30677"

    response = requests.get(url)

    # If response code is 200, then return the response
    if response.status_code == 200:
        # Response
        web_response = response.status_code

        return f"TEST PASSED RESPONSE CODE {response.status_code}"
    else:
        print(f"An error has ocurred, while fetching alerts, with the following code {response.status_code}")

if __name__ == "__main__":
    response = get_my_python_app_status()
    print(response)

