# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import logging
import os
import requests
import re
from themis.finals.attack.result import Result


class AttackErrorBase(Exception):
    pass


class GenericError(AttackErrorBase):
    pass


class InvalidIdentityError(AttackErrorBase):
    pass


class ContestNotStartedError(AttackErrorBase):
    pass


class ContestPausedError(AttackErrorBase):
    pass


class ContestCompletedError(AttackErrorBase):
    pass


class InvalidFormatError(AttackErrorBase):
    pass


class Helper(object):
    def __init__(self, host, port=80, url_path='api/submit'):
        self._host = host
        self._port = port
        self._url_path = url_path

    @property
    def submit_url(self):
        return 'http://{0}:{1}/{2}'.format(self._host, self._port,
                                           self._url_path)

    def attack(self, *flags):
        payload = []
        for flag in flags:
            if re.match('^[\da-f]{32}=$', flag) is None:
                raise InvalidFormatError()
            else:
                payload.append(flag)

        try:
            r = requests.post(self.submit_url, json=payload)
            if r.status_code == 200:
                return list(map(lambda x: Result(x), r.json()))

            if r.status_code == 400:
                code = Result(r.json())
                if code == Result.ERROR_INVALID_IDENTITY:
                    raise InvalidIdentityError()
                elif code == Result.ERROR_CONTEST_NOT_STARTED:
                    raise ContestNotStartedError()
                elif code == Result.ERROR_CONTEST_PAUSED:
                    raise ContestPausedError()
                elif code == Result.ERROR_CONTEST_COMPLETED:
                    raise ContestCompletedError()
                elif code == Result.ERROR_INVALID_FORMAT:
                    raise InvalidFormatError()
                else:
                    raise GenericError()
            else:
                raise GenericError()
        except Exception:
            raise


def format_result(flags, results):
    s = []
    for ndx, flag in enumerate(flags):
        if ndx < len(results):
            s.append('{0}  {1}'.format(flag, results[ndx]))
    return '\n'.join(s)


def run():
    host = os.getenv('THEMIS_FINALS_HOST')
    port = int(os.getenv('THEMIS_FINALS_PORT', '80'))
    url = os.getenv('THEMIS_FINALS_URL', 'api/submit')

    helper = Helper(host, port, url)
    flags = sys.argv[1:]
    try:
        results = helper.attack(*flags)
        print(format_result(flags, results))
    except Exception:
        sys.exit(1)
