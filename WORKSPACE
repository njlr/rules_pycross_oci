load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")




# skylib
http_archive(
  name = "bazel_skylib",
  sha256 = "66ffd9315665bfaafc96b52278f57c7e2dd09f5ede279ea6d39b2be471e7e3aa",
  urls = [
    "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.4.2/bazel-skylib-1.4.2.tar.gz",
    "https://github.com/bazelbuild/bazel-skylib/releases/download/1.4.2/bazel-skylib-1.4.2.tar.gz",
  ],
)

load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")

bazel_skylib_workspace()




# rules_oci
http_archive(
  name = "rules_oci",
  sha256 = "46ce9edcff4d3d7b3a550774b82396c0fa619cc9ce9da00c1b09a08b45ea5a14",
  strip_prefix = "rules_oci-1.8.0",
  url = "https://github.com/bazel-contrib/rules_oci/releases/download/v1.8.0/rules_oci-v1.8.0.tar.gz",
)

load("@rules_oci//oci:dependencies.bzl", "rules_oci_dependencies")

rules_oci_dependencies()

load("@rules_oci//oci:repositories.bzl", "LATEST_CRANE_VERSION", "oci_register_toolchains")

oci_register_toolchains(
  name = "oci",
  crane_version = LATEST_CRANE_VERSION,
)

load("@rules_oci//oci:pull.bzl", "oci_pull")

oci_pull(
  name = "ubuntu_24_04",
  digest = "sha256:2e863c44b718727c860746568e1d54afd13b2fa71b160f5cd9058fc436217b30",
  image = "ubuntu:24.04",
  platforms = [
    "linux/amd64",
    "linux/arm64/v8",
  ],
)




# aspect_rules_py
http_archive(
  name = "aspect_rules_py",
  sha256 = "04278ce23cc5c91a24b62ea00ac04c553fe40ca390943acf6684d367a681a871",
  strip_prefix = "rules_py-0.7.4",
  url = "https://github.com/aspect-build/rules_py/releases/download/v0.7.4/rules_py-v0.7.4.tar.gz",
)

load("@aspect_rules_py//py:repositories.bzl", "rules_py_dependencies")

rules_py_dependencies()

load("@aspect_rules_py//py:toolchains.bzl", "rules_py_toolchains")

rules_py_toolchains()




# rules_python
http_archive(
  name = "rules_python",
  sha256 = "dc6e2756130fafb90273587003659cadd1a2dfef3f6464c227794cdc01ebf70e",
  strip_prefix = "rules_python-0.33.0",
  url = "https://github.com/bazelbuild/rules_python/releases/download/0.33.0/rules_python-0.33.0.tar.gz",
)

load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_multi_toolchains")

py_repositories()




python_register_multi_toolchains(
  name = "python",
  default_version = "3.10.11",
  python_versions = [
    "3.10.11",
    "3.11.6",
    "3.12.0",
  ],
  register_coverage_tool = True,
)

load("@python//3.10.11:defs.bzl", python_interpreter = "interpreter")




# rules_pkg
http_archive(
  name = "rules_pkg",
  urls = [
    "https://mirror.bazel.build/github.com/bazelbuild/rules_pkg/releases/download/1.0.1/rules_pkg-1.0.1.tar.gz",
    "https://github.com/bazelbuild/rules_pkg/releases/download/1.0.1/rules_pkg-1.0.1.tar.gz",
  ],
  sha256 = "d20c951960ed77cb7b341c2a59488534e494d5ad1d30c4818c736d57772a9fef",
)

load("@rules_pkg//:deps.bzl", "rules_pkg_dependencies")

rules_pkg_dependencies()




# rules_pycross
http_archive(
  name = "rules_pycross",
  sha256 = "cef7fd594645a72af17e6748cd0e47743720632ce5c0e9f6b640cce0d185eeb3",
  strip_prefix = "rules_pycross-0.6.1",
  url = "https://github.com/jvolkman/rules_pycross/releases/download/v0.6.1/rules_pycross-v0.6.1.tar.gz",
)

load("@rules_pycross//pycross:repositories.bzl", "rules_pycross_dependencies")

rules_pycross_dependencies(python_interpreter)

load("@rules_pycross//pycross:workspace.bzl", "lock_repo_model_poetry", "pycross_lock_repo", "pycross_register_for_python_toolchains")

pycross_register_for_python_toolchains(
  name = "pycross_environments",
  platforms = [
    "aarch64-apple-darwin",
    "aarch64-unknown-linux-gnu",
    "x86_64-unknown-linux-gnu",
  ],
  python_toolchains_repo = "@python",
)

load("@pycross_environments//:defs.bzl", pycross_environments = "environments")

pycross_lock_repo(
  name = "cowapp_lock_repo",
  lock_model = lock_repo_model_poetry(
    lock_file = "@//cowapp:poetry.lock",
    project_file = "@//cowapp:pyproject.toml",
  ),
  target_environments = pycross_environments,
)

load("@cowapp_lock_repo//:defs.bzl", cowapp_install_deps = "install_deps")

cowapp_install_deps()
