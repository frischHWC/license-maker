#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#import logging
import datetime
import os
import argparse


def main():
    parser = argparse.ArgumentParser(description='Set up an Apache LICENSE project for a non-licensed project',
                                     epilog="This program is intent to help developer's life." +
                                            "It comes with no warranty, always SAVE & BACKUP your files before")
    # Required arguments
    parser.add_argument('--folder', required=True, type=str,
                        help="Absolute path of the folder where to apply license")