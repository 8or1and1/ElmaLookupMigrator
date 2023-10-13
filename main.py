# _system_catalogs ContactStatus tbl_ContactStatus
import time
import config
from lookup_migrator import LookupMigrator as migrator
sys_setting_names = ["NotificationTemplateToContractVisaNotification","NotificationTemplateToKmkContractorQuestionnaireVisaNotification"]
lookup_names = ['KmkSysSettings']
# lookup_names = ['KmkNotoficationTemplates']

for lookup_name in lookup_names:
    print(lookup_name)
    lookup_name_migrator = migrator('_system_catalogs', lookup_name, config.elma_from_config, config.elma_test_config)
    # lookup_name_migrator = migrator('KmkHR', lookup_name, config.elma_from_config, config.elma_test_config)
    lookup_name_migrator.get_data_from_source()
    lookup_name_migrator.filter_data('Code', sys_setting_names)
    lookup_name_migrator.clean_data('RoleValue')
    for x in sys_setting_names:
        if x not in lookup_name_migrator.filtered_codes:
            print(x)
    lookup_name_migrator.clean_data("RoleValue")
    lookup_name_migrator.put_data_in_destination()

