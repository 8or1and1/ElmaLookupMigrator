# _system_catalogs ContactStatus tbl_ContactStatus
import time
import config
from lookup_migrator import LookupMigrator as migrator
#'ContractTypes', 'KmkProjecType', 'KmkAccountType', 'KmkClientStatus',
lookup_names = ['KmkSysSettings']

for lookup_name in lookup_names:
    print(lookup_name)
    lookup_name_migrator = migrator('_system_catalogs', lookup_name, config.elma_from_config, config.elma_client_config)
    lookup_name_migrator.get_data_from_source()
    lookup_name_migrator.filter_data("Code", "Notification")
    lookup_name_migrator.clean_data("StringValue", None)
    lookup_name_migrator.put_data_in_destination()
    time.sleep(3)