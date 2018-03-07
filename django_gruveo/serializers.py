import hmac
import hashlib
import base64
from django.conf import settings
from rest_framework import serializers

class GruveoTokenSerializer(serializers.Serializer):

   token = serializers.CharField(write_only=True)
   token_hmac = serializers.SerializerMethodField(read_only=True)

   def get_token_hmac(self, obj):
       secret = settings.GRUVEO_SECRET
       digest = hmac.new(secret, obj['token'], hashlib.sha256).digest()

       return base64.b64encode(digest)