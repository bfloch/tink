# Copyright 2019 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Python wrapper of the CLIF-wrapped C++ Deterministic AEAD key manager."""

from __future__ import absolute_import
from __future__ import division
# Placeholder for import for type annotations
from __future__ import print_function

from typing import Text

from tink import core
from tink.cc.pybind import cc_key_manager
from tink.daead import deterministic_aead


class _DeterministicAeadCcToPyWrapper(deterministic_aead.DeterministicAead):
  """Transforms cliffed C++ DeterministicAead into a Python primitive."""

  def __init__(self, cc_deterministic_aead):
    self._deterministic_aead = cc_deterministic_aead

  @core.use_tink_errors
  def encrypt_deterministically(self, plaintext: bytes,
                                associated_data: bytes) -> bytes:
    return self._deterministic_aead.encrypt_deterministically(
        plaintext, associated_data)

  @core.use_tink_errors
  def decrypt_deterministically(self, ciphertext: bytes,
                                associated_data: bytes) -> bytes:
    return self._deterministic_aead.decrypt_deterministically(
        ciphertext, associated_data)


def from_cc_registry(
    type_url: Text
) -> core.KeyManager[deterministic_aead.DeterministicAead]:
  return core.KeyManagerCcToPyWrapper(
      cc_key_manager.DeterministicAeadKeyManager.from_cc_registry(type_url),
      deterministic_aead.DeterministicAead, _DeterministicAeadCcToPyWrapper)
