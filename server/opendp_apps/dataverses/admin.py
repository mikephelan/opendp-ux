from django.contrib import admin
from opendp_apps.dataverses.models import ManifestTestParams, RegisteredDataverse


class RegisteredDataverseAdmin(admin.ModelAdmin):
    search_fields = ('name', 'dataverse_url', 'notes')
    list_display = ('name', 'dataverse_url', 'active', 'notes')
    save_on_top = True
    list_filter  = ('active', )



class ManifestTestParamsAdmin(admin.ModelAdmin):
    search_fields = ('name', 'fileId', 'siteUrl')
    list_display = ('name', 'fileId', 'siteUrl',
                    'dataverse_incoming_link_2', 'use_mock_dv_api',
                    'filePid', 'datasetPid')
    save_on_top = True
    list_filter  = ('siteUrl', )
    readonly_fields = ('dataverse_incoming_link_2',
                       'get_dataverse_user_info_link',
                       'get_dataverse_dataset_info_link',
                       'mock_user_info_link',
                       'ddi_info_link',
                       'schema_org_info_link')



admin.site.register(RegisteredDataverse, RegisteredDataverseAdmin)
admin.site.register(ManifestTestParams, ManifestTestParamsAdmin)
