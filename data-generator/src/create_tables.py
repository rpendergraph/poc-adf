from sqlalchemy import create_engine, MetaData, Column, Integer, String, Table, JSON, DateTime
import connection

engine = create_engine(
    connection.get_url_string()
)

metadata = MetaData()
event_table = Table(
    "events",
    metadata,
    Column("id",                Integer, primary_key=True),
    Column("createdon",         DateTime(timezone=False), nullable=False),
    Column("updatedon",         DateTime(timezone=False), nullable=False),
    Column('jsondata',          JSON(), nullable=False),
    Column('svrguid',           String(), nullable=False),
    Column('dataacqguid',       String(), nullable=False),
    Column('desthost',          String()),
    Column("desthosttype",      Integer()),
    Column("destid",            Integer()),
    Column('destlocation',      String(), nullable=True),
    Column('direction',         String(length=1), nullable=True),
    Column("duration",          Integer(), nullable=False),
    Column("origrowid",         Integer(), nullable=False),
    Column('handlertype',       String(), nullable=True),
    Column('identity',          String(), nullable=False),
    Column("identityid",        Integer(), nullable=True),
    Column("initialid",         Integer(), nullable=True),
    Column('initiator',         String(), nullable=True),
    Column("objectdestbytes",   Integer(), nullable=False),
    Column('objectdestname',    String(), nullable=True),
    Column("objectid",          Integer(), nullable=True), #?
    Column('objectname',        Integer(), nullable=True), #?
    Column("objectsourcebytes",   Integer(), nullable=False),
    Column('objectsourcename',    String(), nullable=True),
    Column('operation',         String(), nullable=False),
    Column('operationtype',     String(), nullable=False),
    Column('orgid',             Integer(), nullable=False, default=0),
    Column('orgname',           String(), nullable=False),
    Column('svrname',           String(), nullable=False),
    Column('svrsubtype',        String(), nullable=False),
    Column('svrtype',           String(), nullable=False),
    Column('sourcehost',        String(), nullable=False),
    Column('sourcehosttype',    Integer(), nullable=False, default=0),
    Column("sourceid",          Integer()),
    Column('sourcelocation',    String(), nullable=True),
    Column('status',            Integer(), nullable=False, default=0),
    Column('statusmsg',         String(), nullable=True),
    Column("operationendts",    DateTime(timezone=False), nullable=False),
    Column('workflowid',        String(), nullable=False),
    Column('createdby',         Integer(), nullable=False, default=0),
    Column('updatedby',         Integer(), nullable=False, default=0),
    Column('naturaluniquekey',  String(), nullable=True),
    Column('custom',            String(),  nullable=True),
)

#e Start transaction to commit DDL to postgres database
with engine.begin() as conn:
    metadata.create_all(conn)
    # Log the tables as they are created
    for table in metadata.tables.keys():
        print(f"{table} successfully created")
