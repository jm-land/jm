# MIT License
#
# Copyright (c) 2022 Venera Foundation
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# TODO: Rewrite
import rply
from ..ast import Print, Integer
from ..lexing import listed
from ..compile import Configurator

class Parser:
    def __init__(self, ir: Configurator):
        self._parser = rply.ParserGenerator(listed)
        self.ir = ir

    def start(self):
        @self._parser.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN')
        def print_(p):
            return Print(self.ir, p[2])
        @self._parser.production('expression : INTEGER')
        def integer(p):
            return Integer(self.ir, p[0].value)

    def build(self):
        return self._parser.build()
