# -*- coding: utf-8 -*-
from bottle import Bottle

from .controllers.index import cl_basic
from .controllers.concordance import cl_concordance
from .controllers.compare import cl_compare
from .controllers.counter import cl_counter
from .controllers.dispersion import cl_dispersion
from .controllers.db import cl_db
from .controllers.error import cl_error


Routes = Bottle(8080,True)
Routes.merge(cl_basic)
Routes.merge(cl_concordance)
Routes.merge(cl_compare)
Routes.merge(cl_counter)
Routes.merge(cl_dispersion)
Routes.merge(cl_db)
Routes.merge(cl_error)
