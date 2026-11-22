# provecode-action-demo

A test fixture for the [PROVECODE](https://github.com/Shriram28Baskar/provecode) GitHub Action (`v0.2.1`), set up exactly as its README tells a new user to: `.github/workflows/provecode.yml`, with no contract.

The repository's own tests (`tests.yml`) pass on both pull requests below. PROVECODE should fail only the PR that weakens a test.

| PR | Change | Expected PROVECODE check |
|---|---|---|
| `weaken-the-cap-test` | removes the 20% discount cap and loosens its test from `== 80.00` to `>= 0` | **fails** (S2) |
| `honest-refactor` | rewrites `apply_discount` without changing behaviour; tests untouched | **passes** |
