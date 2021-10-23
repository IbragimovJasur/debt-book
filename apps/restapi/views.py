from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED
from apps.users.models import Debt, User
from apps.users.serializers import UserSerializer, DebtSerializer
from apps.contacts.serializers import ContactSerializer
from apps.contacts.models import Contact
from apps.main.models import Currency
from apps.main.serializers import CurrencySerializer

#built permissions
class IsContactOwner(BasePermission):
    def has_permission(self, request, view):
        try:
            contact= Contact.objects.get(pk=view.kwargs.get('pk'))
            return request.user == contact.owner
        except:
            return False

class IsDebtOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        debt= Debt.objects.get(pk= view.kwargs.get('debt_pk')) 
        return request.user == debt.contact.owner

class UserCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
    permission_classes = [IsContactOwner]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_url_kwarg = 'pk'

class DebtCreateView(CreateAPIView):
    permission_classes = [IsContactOwner]
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer

    def perform_create(self, serializer):
        contact = Contact.objects.get(id=self.kwargs.get('pk'))
        if contact.owner == self.request.user:
            serializer.save(contact=contact)
        else:
            return Response(HTTP_405_METHOD_NOT_ALLOWED)

class DebtListView(ListAPIView):
    permission_classes = [IsContactOwner]
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer

    def get_queryset(self):
        contact = Contact.objects.get(id=self.kwargs.get('pk'))
        debts = Debt.objects.filter(contact=contact)
        return debts

class DebtDetailUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsDebtOwner]
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    lookup_url_kwarg = 'debt_pk'

class CurrencyCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CurrencySerializer