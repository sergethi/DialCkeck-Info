import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def numberInfo(phone_number):
    number = phonenumbers.parse(str(phone_number))
    timezone_res = timezone.time_zones_for_number(number)
    # print("Timezone: ", timezone_res[0])
    carrier_res = carrier.name_for_number(number, None)
    # print("Carrier: ", carrier_res)

    location_res = geocoder.description_for_number(number, None)
    # print("Location: ", location_res)

    is_valid = phonenumbers.is_valid_number(number)
    # print("Validity: ", is_valid)

    is_real = phonenumbers.is_possible_number(number)
    # print("Possible phone number?:", is_real)
    return {
        "number": phone_number.national_number,
        "is_valid": is_valid,
        "is_real": is_real,
        "timezone": timezone_res[0],
        "carrier": carrier_res,
        "location": location_res
    }
