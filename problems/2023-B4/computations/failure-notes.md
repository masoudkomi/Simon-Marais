# Computation repairs

2026-10-16, constructor development, not an adversarial audit.

The first run of `resultant_checks.py` exited with code 1 at the assertion `values[6] == values[5]` inside the finite rational `(6,5)` branch search. Its source and partial stdout are preserved as `resultant_checks.failed-v0.1.py` and `resultant_checks.failed-v0.1.stdout.txt`.

The failing source had an incorrect hand-derived discriminant core for the quadratic

    (3D-1) P^2 + D^2(4D-3) P + D^4(D-1) = 0.

The correct discriminant is `D^4 * (4D^2-8D+5)`. The erroneous core was `-12D^3+32D^2-28D+9`. This bug affects that finite-search code and an abandoned exploratory hand calculation. It does not appear in the proposed general proof, which does not solve this quadratic or rely on the finite branch search. The earlier resultant identity and unit-resultant checks completed before the failure.

Failed command (repository-root working directory):

    .venv/bin/python problems/2023-B4/computations/resultant_checks.py > problems/2023-B4/computations/resultant_checks.stdout.txt

Stderr, with the absolute workspace prefix suppressed only for brevity:

    Traceback (most recent call last):
      File "problems/2023-B4/computations/resultant_checks.py", line 176, in <module>
        main()
      File "problems/2023-B4/computations/resultant_checks.py", line 161, in main
        assert values[6] == values[5]
    AssertionError

The corrected script retains the original recurrence check and adds the exact parameters to any future assertion failure. Its complete rerun output is saved separately as `resultant_checks.stdout.txt`.
