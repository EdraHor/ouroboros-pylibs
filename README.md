# ouroboros-pylibs

A fork of [Ouroboros/PyLibs](https://github.com/Ouroboros/PyLibs): the helper library `ml` (package `ouroboros`)
used by the Falcom script decompiler ([ouroboros-falcom](https://github.com/EdraHor/ouroboros-falcom)).

* Branch `main` (this one): no third-party packages needed. `network`, `cipher`, `asynclib` and `tools` are removed
  (they need `aiohttp`, `rsa` and others and are not used by the decompiler); `xmltodict` and `hexdump` are optional.
* Branch `master`: the original repository, unchanged.

Use: put this folder on `PYTHONPATH` (it provides `ml.py` and `ouroboros/`). Python 3.10+.

The library is by [Ouroboros](https://github.com/Ouroboros).
