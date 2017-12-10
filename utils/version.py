"""
intervaltree: A mutable, self-balancing interval tree for Python 2 and 3.
Queries may be by point, by range overlap, or by range envelopment.

Version utilities

Copyright 2013-2017 Chaim-Leib Halbert

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os
import subprocess

def development_version_number():
    p = subprocess.Popen('git describe'.split(), stdout=subprocess.PIPE)
    git_describe = p.communicate()[0].strip()
    release, build, commitish = git_describe.split('-')
    result = "{0}b{1}".format(release, build)
    return result

def version_info(target_version):
    is_dev_version = 'PYPI' in os.environ and os.environ['PYPI'] == 'pypitest'
    if is_dev_version:
        version = development_version_number()
    else:  # This is a RELEASE version
        version = target_version
    return {
        'is_dev_version': is_dev_version,
        'version': version,
        'target_version': target_version
    }