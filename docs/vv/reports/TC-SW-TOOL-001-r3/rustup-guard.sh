#!/bin/sh
# Download guard for TC-SW-TOOL-001 run 3 (no install beyond SRR decision 109): refuses any rustup
# subcommand that installs or updates; forwards every other subcommand to the real rustup.
case "$1 $2" in
    "component add"*|"toolchain install"*|"toolchain add"*|"self update"*|"update"*|"install"*|"target add"*)
        echo "rustup-guard: refused 'rustup $*' (not an approved install, SRR decision 109)" >&2
        exit 1 ;;
esac
case "$1" in update|install) echo "rustup-guard: refused 'rustup $*'" >&2; exit 1 ;; esac
exec "$HOME/.cargo/bin/rustup" "$@"
