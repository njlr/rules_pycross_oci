# rules_pycross_oci

This repo demonstrates how to use [rules_pycross](https://github.com/jvolkman/rules_pycross), [rules_py](https://github.com/aspect-build/rules_py) and [rules_oci](https://github.com/bazel-contrib/rules_oci) to create Docker images from Python apps.

First, setup your `.bazelrc`:

```bash
$ cp .bazelrc.example .bazelrc
```

To run the app outside of Docker:

```bash
$ bazel run //cowapp

  _________________
 /                 \
| [[ 0  1  2  3  4] |
| [ 5  6  7  8  9]  |
| [10 11 12 13 14]] |
 \                 /
  =================
                 \
                  \
                    ^__^
                    (oo)\_______
                    (__)\       )\/\
                        ||----w |
                        ||     ||
```

To build and register the Docker image:

```bash
$ bazel run //cowapp:tarball_linux_x86_64
```

To run the image:

```bash
$ docker run --rm bazel/cowapp_linux_x86_64:latest

  _________________
 /                 \
| [[ 0  1  2  3  4] |
| [ 5  6  7  8  9]  |
| [10 11 12 13 14]] |
 \                 /
  =================
                 \
                  \
                    ^__^
                    (oo)\_______
                    (__)\       )\/\
                        ||----w |
                        ||     ||
```
