**Purpose**

This file gives concise, repo-specific guidance for AI coding agents working on this learning-oriented Python collection. Focus on small, isolated edits, avoid changing global behaviors, and prefer minimal, test-focused patches.

**Big Picture**

- This repository is a collection of small Python exercises grouped by topic (for example, the `assignment/`, `chapter_two/`, `chapter_three/` folders). Most modules are single-file scripts that implement small functions or interactive programs.
- Data flow is local and procedural: functions operate on simple Python types (tuples, lists, primitives) and often return lists or values for printing. State is occasionally stored in module-level globals (see `assignment/multi_fuel_dispenser_system.py`).

**Important files & examples**

- Interactive script example: [assignment/multi_fuel_dispenser_system.py](assignment/multi_fuel_dispenser_system.py#L1-L40) — contains an unguarded `main()` call and uses module-level global state. When changing this file, avoid introducing import-time side effects.
- Unit tests: many tests use `unittest` and live alongside source files, e.g. [assignment/multi_fuel_dispenser_system_test.py](assignment/multi_fuel_dispenser_system_test.py#L1-L40) and `test_*.py` files under folders like `python_classwork/`.
- Typical exercise file: [assignment/collection_night_fun.py](assignment/collection_night_fun.py#L1-L120) — demonstrates tuple unpacking, simple filter/map patterns, and prints on import.

**Project-specific conventions & patterns**

- Many files run code at import time (top-level `print()` calls or `main()` invoked directly). When editing, prefer adding an `if __name__ == "__main__":` guard so modules can be imported safely by tests or other scripts.
- Naming is inconsistent: both `snake_case` and `camelCase` appear (e.g., `calculate_litres` vs `saveTransaction`). When refactoring, keep changes local to a file and preserve public function names used by tests unless you also update tests.
- Tests use Python's `unittest` framework and a mix of filename patterns (`test_*.py` and `*_test.py`). Rely on explicit discovery patterns when running tests.

**Developer workflows (commands)**

- Run all unit tests from the repository root using unittest discovery:

```bash
python -m unittest discover -s . -p 'test*.py'    # matches test_*.py
python -m unittest discover -s . -p '*_test.py'  # matches *_test.py
```

- Run a single test file:

```bash
python -m unittest assignment.multi_fuel_dispenser_system_test
```

- Run an exercise script directly (beware import-time execution):

```bash
python assignment/multi_fuel_dispenser_system.py
```

**Agent coding guidelines (what to do and avoid)**

- Avoid changing code that executes on import. If you need to modify an interactive script, wrap the runner in `if __name__ == "__main__": main()` (see [assignment/multi_fuel_dispenser_system.py](assignment/multi_fuel_dispenser_system.py#L1-L120)).
- Make minimal, focused edits. These are learning exercises—prefer surgical fixes or small refactors that preserve original behavior and tests.
- When tests fail due to import-time prompts, fix by guarding the interactive runner rather than stubbing `input()` calls in tests.
- Preserve test names and behaviors. If you rename a function used by tests, update the test in the same change to keep PRs reviewable and atomic.

**Dependencies and environment**

- This project targets plain CPython with standard library only — there is no `requirements.txt` or virtualenv configuration in the repo. If adding dependencies, include a `requirements.txt` at the repo root.

**When creating PRs**

- Include a short description explaining why the change is safe (e.g., "guarded main to avoid import-time input prompts") and list any files that changed.
- Run local tests with the discovery commands above and include test results in PR description if they are not trivial.

**If uncertain**

- Ask: "Does this change need to be import-safe for other scripts/tests?" If yes, avoid import-time printing and side effects.

---

If you'd like, I can (1) scan a second set of representative files and add a few concrete inline examples showing how to apply `if __name__ == "__main__"` fixes, or (2) patch one interactive file as a model change — tell me which option you prefer.
