
# from sinch import Client
# import requests

# def send_message(msg,phn):
#     sinch_client = Client(
#         key_id="d5255600-1753-4942-821f-952c3689cf65",
#         key_secret="1i.PtFfbe9Qe_-c6U6v6UJnmRI",
#         project_id="c469d659-92b6-4761-a944-67565b3c0243")

#     send_batch_response = sinch_client.sms.batches.send(
#         body=msg,
#         to=[phn],
#         from_="+447520662372",
#         delivery_report="none"
#     )
#     print(send_batch_response)

# #This is for google maps location of enterd place
# from geopy.geocoders import GoogleV3
# import requests
# def coordinates_to_gmaps_url(latitude, longitude):
#     base_url = "https://www.google.com/maps/search/?api=1&query="
#     query = f"{latitude},{longitude}"
#     gmaps_url = base_url + query
#     return gmaps_url

# def get_location_by_name(place_name):
#     geolocator = GoogleV3(api_key="ENTER__THE__API___KEY")#####################********************#################3
#     location = geolocator.geocode(place_name)

#     if location:
#         return [location.address,coordinates_to_gmaps_url(location.latitude,location.longitude)]
#     else:
#         return ("Location not found for", place_name)
    


# def emergency_contact(email,phn,loc)