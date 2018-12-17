from allstars.models import *
from api.serializers import PersonRecordSerializer
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response


class PersonRecordViewSet(viewsets.ModelViewSet):
	"""
	This ViewSet provides both 'list' and 'detail' views.
	"""
	queryset = PersonRecord.objects.select_related('team_align', 'coach').order_by('last_name')
	serializer_class = PersonRecordSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def delete(self, request, pk, format=None):
		site = self.get_object(pk)
		self.perform_destroy(self, site)

		return Response(status=status.HTTP_204_NO_CONTENT)

	def perform_destroy(self, instance):
		instance.delete()
