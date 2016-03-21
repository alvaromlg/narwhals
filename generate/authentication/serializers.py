from rest_framework import serializers
from rest_framework.authtoken.models import Token

from models import User

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'last_login', 'email', 'date_of_birth', 'position',
                  'meters', 'minutes', 'strokes', 'metersAverage',
                  'minutesAverage', 'city_id', 'name', 'surname', 'trend',
                  'bio', 'avatar', 'token')
        write_only_fields = ('password',)
        read_only_fields = ('is_admin', 'is_active',)

    def restore_object(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user

    def get_token(self, user):
        token = Token.objects.get(user=user.id)
        return token.key
