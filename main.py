from doordash_api import create_delivery_request, get_delivery_request

create_delivery_response = create_delivery_request() 

get_delivery_response = get_delivery_request()

print(create_delivery_response.text)

print(get_delivery_response.text)


# delivery_info = json.loads(get_delivery.text)

# organized_info = {
#     "external_delivery_id": delivery_info["external_delivery_id"],
#     "currency": delivery_info["currency"],
#     "delivery_status": delivery_info["delivery_status"],
#     "fee": delivery_info["fee"],
#     "pickup_info": {
#         "pickup_address": delivery_info["pickup_address"],
#         "pickup_business_name": delivery_info["pickup_business_name"],
#         "pickup_phone_number": delivery_info["pickup_phone_number"],
#         "pickup_instructions": delivery_info["pickup_instructions"],
#         # ... (other pickup-related fields)
#     },
#     "dropoff_info": {
#         "dropoff_address": delivery_info["dropoff_address"],
#         "dropoff_business_name": delivery_info["dropoff_business_name"],
#         "dropoff_phone_number": delivery_info["dropoff_phone_number"],
#         "dropoff_instructions": delivery_info["dropoff_instructions"],
#         # ... (other dropoff-related fields)
#     },
#     "order_value": delivery_info["order_value"],
#     "cancellation_reason": delivery_info["cancellation_reason"],
#     # ... (other fields)
# }


# print(organized_info["pickup_info"]["pickup_address"])