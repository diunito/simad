# -*- coding: utf-8 -*-
from enum import Enum


class Result(Enum):
    SUCCESS_FLAG_ACCEPTED = 0  # submitted flag has been accepted
    ERROR_GENERIC = 1  # generic error
    ERROR_INVALID_IDENTITY = 2  # the attacker does not appear to be a team
    ERROR_CONTEST_NOT_STARTED = 3  # contest has not been started yet
    ERROR_CONTEST_PAUSED = 4  # contest has been paused
    ERROR_CONTEST_COMPLETED = 5  # contest has been completed
    ERROR_INVALID_FORMAT = 6  # submitted data has invalid format
    ERROR_ATTEMPTS_LIMIT = 7  # attack attempts limit exceeded
    ERROR_FLAG_EXPIRED = 8  # submitted flag has expired
    ERROR_FLAG_YOURS = 9  # submitted flag belongs to the attacking team
    ERROR_FLAG_SUBMITTED = 10  # submitted flag has been accepted already
    ERROR_FLAG_NOT_FOUND = 11  # submitted flag has not been found
    ERROR_SERVICE_NOT_UP = 12  # the attacking team service is not up
