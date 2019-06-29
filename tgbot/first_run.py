import configure
from database import SQLighter

db_worker = SQLighter(configure.database)

db_worker.create()