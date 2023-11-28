from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

class NoteList(APIView):
    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetail(APIView):
    def get_object(self, note_id):
        try:
            return Note.objects.get(id=note_id)
        except Note.DoesNotExist:
            raise Http404

    def get(self, request, note_id):
        note = self.get_object(note_id)
        serializer = NoteSerializer(note)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, note_id):
        note = self.get_object(note_id)
        note.delete()
        return Response({'message': 'Note deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    def get_object(self, note_id):
        try:
            return Note.objects.get(id=note_id)
        except Note.DoesNotExist:
            raise Http404

    def delete(self, request, note_id):
        note = self.get_object(note_id)
        note.delete()
        return Response({'message': 'Note deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
