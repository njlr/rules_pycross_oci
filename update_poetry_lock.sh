#!/usr/bin/env bash

set -e

(
  cd "$(dirname "$0")"

  bazel build //cowapp:poetry
  cp -f bazel-bin/cowapp/poetry_lock.bzl cowapp/poetry_lock.bzl
)
