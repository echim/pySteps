from enum import Enum


class TestOutcome(Enum):
    PASSED = 'passed'
    FAILED = 'failed'
    SKIPPED = 'skipped'
