# provecode-action-demo

A test fixture for the [PROVECODE](https://github.com/Shriram28Baskar/provecode) GitHub Action (`v0.2.1`), set up exactly as its README describes. It runs two workflows:

- **`provecode.yml`**, with no contract. Any test-weakening finding fails the check.
- **`provecode-contract.yml`**, with the approved contract [`contracts/checkout.yaml`](contracts/checkout.yaml): C1 (the 20% cap), C2 (correct values) and C3 (invalid input raises), each guarded by a test. The contract is read from the PR's **base** commit, so a PR cannot edit the requirements that judge it.

The repository's own tests (`tests.yml`) pass on all three pull requests.

| PR | Change | `provecode` (no contract) | `provecode-contract` |
|---|---|---|---|
| `weaken-the-cap-test` | removes the cap and loosens its test from `== 80.00` to `>= 0` | **fails** (S2) | **fails**: FAILED, S2 blocking on C1 |
| `honest-refactor` | rewrites `apply_discount` without changing behaviour | passes | passes |
| `relax-the-contract` | deletes C1 from the contract, removes the cap, loosens its test | **fails** (S2) | **fails**: FAILED, CONTRACT_TOUCHED, and S2 still on C1 |
