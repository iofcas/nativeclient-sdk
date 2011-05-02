#!/usr/bin/python
#!/usr/bin/python
# Copyright 2008, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import errno
import os
import sys
sys.path.append("../../common")
import nacl_util

TESTDATA256 = "./testdata256"
TESTDATA_TXT = "./testdata.txt"
NOEXIST = "./noexist.abc"

NEXE = "file.nexe"
DEFAULT_ARGS = None

# function remove()
#   attempt to remove a test data file
#   and don't complain if it didn't exist.
def remove(name):
  try:
    os.remove(name)
  except OSError, e:
    if e.errno == errno.ENOENT:
      # silently pass if the file isn't there
      pass
    else:
      raise
  except:
    raise


def removeAllTestFiles():
  remove(TESTDATA256)
  remove(TESTDATA_TXT)
  remove(NOEXIST)


def runTestSuite():
  return nacl_util.LaunchSelLdr(nacl_util.GetExe(NEXE),
                                nacl_util.GetArgs(DEFAULT_ARGS))


if __name__ == '__main__':
  # erase (clean) test data files before running test suite
  # (currently we cannot remove files from NaCl, so have
  # to remove test data files from this python script)
  removeAllTestFiles()
  ret = runTestSuite()
  removeAllTestFiles()
  sys.exit(ret)
