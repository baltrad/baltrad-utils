# Copyright (C) 2023- Swedish Meteorological and Hydrological Institute (SMHI)
#
# This file is part of baltrad-utils.
#
# baltrad-utils is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# baltrad-utils is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with baltrad-utils.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################

## Tests baltradutils.jprops

## @file
## @author Anders Henja, SMHI
## @date 2023-09-27
from __future__ import absolute_import

import unittest
import os

from baltradutils import jprops

FIXTURE_DIR = "%s/fixtures" % os.path.dirname(os.path.abspath(__file__))

class test_jprops(unittest.TestCase):
    FIXTURE_FILE = "%s/jprops.properties" % FIXTURE_DIR
    
    def test_load_and_read(self):
        with open(self.FIXTURE_FILE) as fp:
            props = jprops.load_properties(fp)
            self.assertEqual("HEJ", props["one.property.name"])
            self.assertEqual("10", props["two.property.name"])
