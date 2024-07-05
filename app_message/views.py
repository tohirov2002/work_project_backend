from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from datetime import datetime
import requests
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from urllib.parse import quote_plus
from .serializers import ApplySerializer

BOT_TOKEN = "7398859359:AAGicm9V51qZ2JUkLtRRhzc0k49VrrsYpGY"
QUERY_URL = "https://api.telegram.org/bot" + BOT_TOKEN
SEND_MESSAGE = QUERY_URL + "/sendMessage"
ID_ASR = "5585608431"

class ApplyView(APIView):
    def post(self, request):
        serializer = ApplySerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Extract validated data from serializer
                who = serializer.validated_data['ism'].replace("'", "‘")
                familiya = serializer.validated_data['familiya']
                phone = serializer.validated_data['tel']
                date = serializer.validated_data['sana']
                msg = serializer.validated_data['sms'].replace("'", "‘")
                fayl = serializer.validated_data['fayl']
                ip = request.META.get('REMOTE_ADDR')

                file_path = default_storage.save(f'fayllar/{fayl.name}', ContentFile(fayl.read()))

                now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                msg_to_bot = (
                    "<b>|***********|\tYANGI XABAR\t|***********|\n\n{}\n\n|***********|\tYANGI XABAR\t|***********|</b>\n\n"
                    "<b>Ismi:</b> {}\n<b>Familiya:</b> {}\n<b>Telefoni:</b> {}\n<b>Tug'ilgan Sanasi:</b> {}\n<b>Vaqt:</b> {}\n<b>IP adres:</b> {}\n\n\n"
                    "<b>🏢<a href='https://standart.mc.uz'>Sog'lom hayot kilinikasi </a></b>"
                ).format(msg, who, familiya, phone, date, now, ip)

                # Correctly pass the parse_mode parameter
                requests.get(SEND_MESSAGE, params={
                    "chat_id": ID_ASR,
                    "text": msg_to_bot,
                    "parse_mode": "HTML"
                })

                # Save data to database
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO message (ism, familiya, tel, sana, sms, fayl) VALUES (%s, %s, %s, %s, %s, %s)",
                        [who, familiya, phone, date, msg, file_path]
                    )

                # Respond with success message
                return Response({
                    "message": f"Hurmatli {who}! Sizning murojaatingiz ma‘muriyatga yuborildi! Tez orada siz bilan bog‘lanishadi."
                }, status=status.HTTP_200_OK)

            except Exception as e:
                # Handle exceptions
                print(f"Error processing request: {e}")
                return Response({"error": f"Qandaydir xatolik bo‘ldi! {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
