# cowapp

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
