# sparkapp

To run the app:

```bash
bazel run //sparkapp
```

To register the Docker image:

```bash
bazel run //sparkapp:tarball_linux_x86_64
```

To run it:

```bash
docker run --rm bazel/sparkapp_linux_x86_64:latest
```

To run the tests:

```bash
bazel test //sparkapp/...
```
