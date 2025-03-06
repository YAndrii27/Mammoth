from enum import Enum


class ReportCategory(Enum):
    SPAM = "spam"
    VIOLATION = "violation"
    OTHER = "other"
