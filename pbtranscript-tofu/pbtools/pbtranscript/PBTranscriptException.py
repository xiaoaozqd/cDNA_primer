#!/usr/bin/env python
"""Define PBTranscript exceptions."""


class PBTranscriptException(Exception):
    """Define PBTranscript exception class."""
    def __init__(self, cmd, msg):
        Exception.__init__(self)
        self.cmd = cmd
        self.msg = msg

    def __repr__(self):
        return "command: " + self.cmd + " raised the following " + \
            "error: " + self.msg

    def __str__(self):
        return self.__repr__()
