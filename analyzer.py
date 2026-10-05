#!/usr/bin/env python3

import sys


def analyze_log(filename):
    errors = 0
    warnings = 0
    info = 0
    failed_logins = 0

    with open(filename, "r", errors="ignore") as log_file:
        for line in log_file:
            line_lower = line.lower()

            if "error" in line_lower:
                errors += 1

            if "warning" in line_lower or "warn" in line_lower:
                warnings += 1

            if "info" in line_lower:
                info += 1

            if "failed password" in line_lower:
                failed_logins += 1

    print("\n===== Linux Log Analyzer =====")
    print(f"Errors:        {errors}")
    print(f"Warnings:      {warnings}")
    print(f"Info:          {info}")
    print(f"Failed logins: {failed_logins}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <log-file>")
        sys.exit(1)

    analyze_log(sys.argv[1])
