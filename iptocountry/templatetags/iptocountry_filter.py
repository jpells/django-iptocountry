from django import template
register = template.Library()

def ip2long(ip):
    ip_array = ip.split('.')
    ip_long = int(ip_array[0]) * 16777216 + int(ip_array[1]) * 65536 + int(ip_array[2]) * 256 + int(ip_array[3])
    return ip_long

def long2ip(long):
    import socket
    import struct
    return socket.inet_ntoa(struct.pack("!I", long))

def get_country2(value, arg):
    ''' arg is the location of the flag imgs, eg '/media/img/flag/' '''
    from django.conf import settings
    arg = settings.MEDIA_URL + arg
    from iptocountry.models import IpToCountry
    value = ip2long(value)
    try:
        # ip of comment has to be in a range of an ip-to-country object IP_FROM and IP_TO
        iptc = IpToCountry.objects.get(IP_FROM__lte=value, IP_TO__gte=value)
    except IpToCountry.DoesNotExist:
        return " "
    return "<img src='" + arg + (iptc.COUNTRY_CODE2).lower() + ".gif' alt='" + (iptc.COUNTRY_NAME).lower() + "' />"

register.filter('get_country2', get_country2)
