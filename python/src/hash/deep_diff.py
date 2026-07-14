# Custom problem: Minimal Deep Diff (recursive tree/dict diff)
#
# You're given two nested dict structures, `base` and `override`, where
# values can be dicts, lists, or scalars, arbitrarily nested. Define
# `deep_merge(a, patch)` as: for every key in `patch`, if both `a[key]` and
# `patch[key]` are dicts, merge recursively; otherwise `patch[key]` replaces
# `a[key]` wholesale (lists and scalars are never merged element-by-element).
#
# Write `deep_diff(base, override)` that returns `(patch, undeletable)`
# where:
#   - `patch` is the *smallest* dict such that deep_merge(base, patch) == override.
#     Keys/subtrees that are already equal in base and override are omitted.
#   - `undeletable` is a list of dotted key paths that exist in `base` but are
#     missing from `override` — these can't be expressed in `patch`, since
#     deep_merge has no "delete" operation (a merge can only add or replace
#     keys, never remove them).
#
# Example 1 (no change):
#   base     = {"a": 1, "b": {"c": 2}}
#   override = {"a": 1, "b": {"c": 2}}
#   -> patch = {}, undeletable = []
#
# Example 2 (nested scalar change + new key):
#   base     = {"a": 1, "b": {"c": 2, "d": 3}}
#   override = {"a": 1, "b": {"c": 20, "d": 3}, "e": 5}
#   -> patch = {"b": {"c": 20}, "e": 5}, undeletable = []
#
# Example 3 (deletion — unrepresentable):
#   base     = {"a": 1, "b": 2}
#   override = {"a": 1}
#   -> patch = {}, undeletable = ["b"]
#
# Example 4 (dict wholesale-replaced by non-dict):
#   base     = {"a": {"x": 1}}
#   override = {"a": 5}
#   -> patch = {"a": 5}, undeletable = []
#
# This generalizes the diff logic in
# adf-schema-migration/differ.py:deep_diff — it's the inverse of a merge
# operation: find the minimal patch that, merged onto base, reproduces
# override, flagging anything a merge fundamentally can't express.
#
# Time:  O(n) where n is the total number of keys/values across both structures
#        — each key visited once.
# Space: O(d) recursion depth (d = nesting depth), plus O(n) for the output.

from typing import Any


def deep_diff(base: Any, override: Any) -> tuple[dict, list[str]]:
    """Return (patch, undeletable). `patch` is `{}` if base == override."""
    patch, undeletable = _diff(base, override)
    return patch or {}, undeletable


def _diff(base: Any, override: Any, _path: str = "") -> tuple[Any, list[str]]:
    """Return (sub_patch, undeletable). `sub_patch` is None if base == override,
    so the caller can tell "no change" (omit this key) apart from "changed to
    an empty dict" (keep the key with an empty-dict value)."""
    if base == override:
        return None, []

    if not isinstance(base, dict) or not isinstance(override, dict):
        return override, []

    patch: dict[str, Any] = {}
    undeletable: list[str] = []

    for key, override_value in override.items():
        path = f"{_path}.{key}" if _path else key
        if key not in base:
            patch[key] = override_value
            continue
        sub_patch, sub_undeletable = _diff(base[key], override_value, path)
        undeletable.extend(sub_undeletable)
        if sub_patch is not None:
            patch[key] = sub_patch

    for key in base:
        if key not in override:
            path = f"{_path}.{key}" if _path else key
            undeletable.append(path)

    return (patch if patch else None), undeletable


if __name__ == "__main__":
    assert deep_diff({"a": 1, "b": {"c": 2}}, {"a": 1, "b": {"c": 2}}) == ({}, []), "Example 1"

    assert deep_diff(
        {"a": 1, "b": {"c": 2, "d": 3}},
        {"a": 1, "b": {"c": 20, "d": 3}, "e": 5},
    ) == ({"b": {"c": 20}, "e": 5}, []), "Example 2"

    assert deep_diff({"a": 1, "b": 2}, {"a": 1}) == ({}, ["b"]), "Example 3"

    assert deep_diff({"a": {"x": 1}}, {"a": 5}) == ({"a": 5}, []), "Example 4"

    # Deletion nested inside an otherwise-unchanged subtree.
    assert deep_diff(
        {"a": {"x": 1, "y": 2}},
        {"a": {"x": 1}},
    ) == ({}, ["a.y"]), "Nested deletion"

    print("All tests passed.")
