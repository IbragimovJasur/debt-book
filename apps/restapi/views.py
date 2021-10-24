from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from apps.users.models import Debt, User
from apps.users.serializers import UserSerializer, DebtSerializer, DebtPaidSerializer
from apps.contacts.serializers import ContactSerializer
from apps.contacts.models import Contact
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
        debt= Debt.objects.get(pk= view.kwargs.get('pk')) 
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
    permission_classes = [IsAuthenticated]
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


class DebtListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer

    def get_queryset(self):
        contact = Contact.objects.filter(owner=self.request.user)
        debts = Debt.objects.filter(contact__in=contact)
        return debts


class DebtDetailUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsDebtOwner]
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    lookup_url_kwarg = 'pk'


class DebtPaidView(UpdateAPIView):
    permission_classes = [IsDebtOwner]
    queryset = Debt.objects.all()
    serializer_class = DebtPaidSerializer
    lookup_url_kwarg = 'pk'


class CurrencyCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CurrencySerializer