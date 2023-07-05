from sqlalchemy import create_engine, MetaData, select
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
import os
import uuid
from datetime import datetime, timezone, timedelta
import random
import connection

def main():
    engine = create_engine(connection.get_url_string())
    metadata = MetaData()
    with engine.connect() as conn:
        metadata.reflect(conn)
        faker = Faker()
        events_table = metadata.tables["events"]
        record_count = os.environ.get('RECORD_COUNT', 1)
        generate_records(conn, events_table, record_count)
        conn.commit()

def generate_records(conn: any, events_table: any , record_count: int):
    for _ in range(record_count):
        stmt = events_table.insert().values(**generate())
        conn.execute(stmt)

def generate():
    fake = Faker('en_US')
    # TODO ID?
    current = datetime.now(timezone.utc),
    duration = fake.unique.random_int(min=300, max=20000)
    out = dict(
            createdon=current,
            updatedon=current,
            svrguid=guid(),
            dataacqguid=guid(),
            desthost=host(),
            desthosttype=host_type(),
            destid=fake.unique.random_int(min=111111, max=999999),
            destlocation=host(),
            direction=random.choice(['O', 'I', '-']),
            duration=duration,
            origrowid=fake.unique.random_int(min=111111, max=999999),
            handlertype=None,
            identity='shoveit.acme.net_user',
            identityid=fake.unique.random_int(min=111111, max=999999),
            initialid=fake.unique.random_int(min=111111, max=999999),
            initiator=None,
            objectdestbytes=fake.unique.random_int(max=99999999),
            objectdestname=filename(fake),
            objectid=fake.unique.random_int(min=111111, max=999999),
            objectname=None,
            operation=random.choice(['Upload', 'Process', 'Download', 'Delete']),
            operationtype=operation_type(),
            orgid=fake.unique.random_int(min=111111, max=999999),
            orgname='shoveit.acme.net_org',
            svrname='SHOVPATZ01.acme.net',
            svrsubtype='Central',
            svrtype='shoveit',
            sourcehost=host(),
            sourcehosttype=1,
            sourceid=fake.unique.random_int(min=111111, max=999999),
            sourcelocation=fake.file_path(absolute=True, depth=4, extension=''),
            status=random.choice([0, 5010, 3400]),
            workflowid=workflow_id(),
            createdby=1,
            updatedby=1,
            naturaluniquekey=None,
            custom=None
            )
    out['statusmsg']=status_msg(out['status'])
    out['objectsourcebytes'] = out['objectdestbytes']
    out['objectsourcename']= out['objectdestname']
    print(current)
    out['operationendts'] = current # + timedelta(milliseconds=duration)
    out['jsondata'] = fake_json(fake, out)
    return out

def status_msg(status):
    match status:
        case 5010:
            return 'No files to process'
        case 3400:
            return 'File exists and Overwrite is false'
        case _:
            return None

def host_type():
    return random.choice([0, 4, -1])

def filename(fake):
    return (fake.pystr_format('###-') + 
            fake.pystr(min_chars=4, max_chars=4, suffix='__') + 
            fake.pystr_format('1153#####') + 
            fake.date_this_month(before_today=True).strftime("%d_%m_%Y %H.%M.%S"))

def operation_type():
    return random.choice([
        'Upload',
        'PGP Decrypt',
        'Download',
        'Find Or Replace',
        'PGP Encrypt Only',
        'Delete',
        'Unzip Advanced',
        'Sleep',
        'Convert LF to CRLF',
        'NoOp',
        'Zip Advanced'
        ])

def guid():
    return str(uuid.uuid4())

def host():
    return random.choice([
        'Mainframe FTP',
        '100.34.252.122', 
        'BRUTUS',
        'SYSCOR_HA_HAAHGAZZ01', 
        'ACME Shoveit DMZ',
        'ALON_PROD',
        'Texas Infants Care Consortium',
        'Imperio ADT Prod',
        'Imperio_ACMECAREOB_Prod',
        'Imperio_Imaging',
        'ZWF BCT TIBCO server for Policy Exchange',
        'Heartsafe Insecure htg045',
        'YoYoDyne Health',
        'ZCO_ZTO886PROD', 
        'Heartsafe Insecure hok09876',
        'PiVOT LIFE',
        'HJMV LowMark [st4qo002jt0]', 
        'QuantRX Download', 
        'AmeriLife Gold',
        'Vertex (BAA) (Intra)',
        'YoYoDyne SFTP',
        '\\\\EHMGLOILSHARE\\ECMProd',
        '\\\\SASMEPMO1\\CareWrite\\Processing\\Prod', 
        '\\\\gnt1ssj2\\MoneySystems',
        '\\\\ibmspadp01.acme.net\\HRFeed',
        '\\\\ibmstadp01.hardworktest.net\\HRFeed',
        '\\\\frl4stx2\\CSWFileShare', 
        '\\\\frl4stx3\\Imaging\\Input',
        '\\\\frl4stx3\\QUANTCO Prod', 
        '\\\\frl4stx3\\Amerilife Membership Information\\Vendor Outbound Files',
        '\\\\frl4stx4\\megaftp',
        '\\\\frl4stx5\\SFTStage', 
        '\\\\frl4stx6\\chh_prod',
        '\\\\frl4stx8\\IndividualAccts',
        '\\\\sasmepedi\\Membership', 
        '\\\\sasmepmis12\\Government Programs\\File Transfer Folder',
        '\\\\sasmepmis15\\SHARE_INBOUND',
        '\\\\sasmephcis\\Enterprise Exchange Services',
        '\\\\sasmepmw1.acme.net', 
        '\\\\sasmepmis12\\RiskAdjustment\\File Transfer',
        '\\\\sasmepmis15\\BOGUSDATATECH'
        ])

def workflow_id():
    return random.choice([
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:482080674:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:174804878:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:833245456:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:277946007:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:487660259:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:228562945:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:990012795:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:120970476:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:401297152:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:685635769:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:795243329:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:807174438:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:650190592:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:288540357:1643675400000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:605558848:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:114559996:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:598514080:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:500529712:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:882762092:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:241105223:1643688000000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:490101874:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:398618484:1643673649690',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:694231981:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:382765824:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:885942656:1643673600000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:337331080:1643673660000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:396752203:1643673720000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:927096647:1643673720000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:312323612:1643673780000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:183851433:1643673840000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:214427704:1643673840000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:400505471:1643673900000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:526353431:1643673900000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:412159616:1643673900000',
        'f9fe9823-7245-4ded-9c9a-2cdb76c3a9fc:1:610533059:1643674500000'])

def fake_json(fake, rows):
    return {
            "com_ipswitch_moveit_ftoperations": {
                
                "agentGuid": rows['svrguid'],
                "destHost": rows['desthost'],
                "destHostType": rows['desthosttype'],
                "destId": rows['destid'],
                "destLocation": rows['destlocation'],
                "direction": rows['direction'],
                "duration": rows['duration'],
                "entityId": rows['origrowid'],
                "handlerType": rows['handlertype'],
                "identity": rows['identity'],
                "identityId": rows['identityid'],
                "initialId": rows['initialid'],
                "initiator": rows['initiator'],
                "objectDestBytes": rows['objectdestbytes'],
                "objectDestName": rows['objectdestname'],
                "objectSourceBytes": rows['objectsourcebytes'],
                "objectSourceName": rows['objectsourcename'],
                "operation": rows['operation'],
                "operationType": rows['operationtype'],
                "orgId": rows['orgid'],
                "orgName": rows['orgname'],
                "serverName": rows['svrname'],
                "serverSubType": rows['svrsubtype'],
                "serverType": rows['svrtype'],
                "sourceHost": rows['sourcehost'],
                "sourceHostType": rows['sourcehosttype'],
                "sourceId": rows['sourceid'],
                "sourceLocation": rows['sourcelocation'],
                "status": rows['status'],
                "statusMsg": rows['statusmsg'],
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "workflowId": rows['workflowid']
                }
            }

if __name__ == '__main__':
    main()
