import sys
# This is needed so as to run on CLI
sys.path.append('/home/gfot/vvrmc_cucm_ms')

from modules import module_cdr_funcs


module_cdr_funcs.populate_db()
