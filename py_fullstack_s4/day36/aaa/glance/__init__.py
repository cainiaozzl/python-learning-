print('glance包的init文件')

# from .api.policy import get
#
# from .api.versions import create_resource
#
# from .cmd.manage import main
#
# from .db.models import register_models

import sys,os
sys.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(sys.path)
from aaa import glance


glance.policy.main()
