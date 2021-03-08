import json

from django.http import JsonResponse
from rest_framework import authentication, permissions, viewsets
from rest_framework.views import APIView

from opendp_apps.dataset.models import DataverseFileInfo, DataSetInfo
from opendp_apps.analysis.models import DepositorSetupInfo
from opendp_apps.dataset.redis import RedisClient
from opendp_apps.dataset.serializers import DataSetInfoSerializer


class DataSetInfoViewSet(viewsets.ModelViewSet):
    queryset = DataSetInfo.objects.all().order_by('-created')
    serializer_class = DataSetInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepositorSetup(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        """

        """
        mock_dataverse_request = {
            "dataverse_file_id": 1,
            "doi": "doi://123",
            "installation_name": "harvard",
            "dataverse_token": "token"
        }
        # request_body = json.loads(request.data)
        #depositor_setup_info = DepositorSetupInfo.objects.create(epsilon=request.data['epsilon'])

        ds_info = DataverseFileInfo.objects.create(name=request.data['name'],
                                                   creator=request.user,
                                                   data_profile=None,
                                                   #depositor_setup_info=depositor_setup_info,
                                                   dataverse_file_id=mock_dataverse_request['dataverse_file_id'],
                                                   doi=mock_dataverse_request['doi'],
                                                   installation_name=mock_dataverse_request['installation_name'])

        print(ds_info.id)
        return JsonResponse({'id': ds_info.id})
