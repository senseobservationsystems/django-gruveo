import hmac
import hashlib
import base64
from django.conf import settings
from rest_framework import serializers

class GruveoTokenSerializer(serializers.Serializer):

   unique_message = serializers.CharField(write_only=True)
   gruveo_token = serializers.SerializerMethodField(read_only=True)

   def get_gruveo_token(self, obj):
       secret = settings.GRUVEO_SECRET
       digest = hmac.new(secret, obj['unique_message'], hashlib.sha256).digest()

       return base64.b64encode(digest)