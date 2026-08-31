import importlib.util
import sys

from pathlib import Path

ROOT = Path(__file__).parent


def load_solution(case_dir: Path):
    solution_path = case_dir / "solution.py"

    if not solution_path.exists():
        raise FileNotFoundError(f"Missing {solution_path}")

    spec = importlib.util.spec_from_file_location("solution", solution_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Couldn't load {solution_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def load_tests(case_dir: Path):
    test_path = case_dir / "cases.py"

    if not test_path.exists():
        raise FileNotFoundError(f"Missing {test_path}")

    spec = importlib.util.spec_from_file_location("cases", test_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load {test_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def run(case_name: str):
    case_dir = ROOT / case_name

    if not case_dir.is_dir():
        print(f"Case not found: {case_name}")
        return 1

    solution = load_solution(case_dir)
    tests = load_tests(case_dir)

    if not hasattr(solution, "Solution"):
        print("solution.py must contain a Solution class")
        return 1

    if not hasattr(tests, "TEST_CASES"):
        print("test.py must contain TEST_CASES")
        return 1

    solver = solution.Solution()

    passed = 0
    failed = 0

    for index, test_case in enumerate(tests.TEST_CASES, start=1):
        args = test_case["args"]
        expected = test_case["expected"]

        try:
            actual = solver.__getattribute__(test_case["method"])(*args)

            if actual == expected:
                print(f"✓ Test {index}: passed")
                passed += 1
            else:
                print(f"✗ Test {index}: failed")
                print(f"  expected: {expected}")
                print(f"  actual:   {actual}")
                failed += 1

        except Exception as error:
            print(f"✗ Test {index}: error")
            print(f"  {type(error).__name__}: {error}")
            failed += 1

    print()
    print(f"{passed} passed, {failed} failed")

    return 0 if failed == 0 else 1


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <case>")
        print()
        print("Available cases:")

        for path in sorted(ROOT.iterdir()):
            if path.is_dir() and (path / "solution.py").exists():
                print(f"  {path.name}")

        return 1

    return run(sys.argv[1])


if __name__ == "__main__":
    sys.exit(main())
