from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from apps.contacts.models import Contact
from apps.users.models import CustomUser
from apps.users.serializers import CustomUserSerializer
from apps.contacts.serializers import ContactSerializer

#built permissions
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        contact= Contact.objects.get(pk= view.kwargs['pk']) 
        return request.user == contact.owner

class CustomUserCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user

class ContactListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    def get_queryset(self):
        qs = Contact.objects.filter(owner = self.request.user)
        return qs

class ContactCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class ContactUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
