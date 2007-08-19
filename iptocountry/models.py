from django.db import models
import csv

class IpToCountry(models.Model):
    """
    A IpToCountry 

    >>> # Create a IpToCountry
    >>> i = IpToCountry.objects.create(IP_FROM='a', IP_TO='a', COUNTRY_CODE2='a',COUNTRY_CODE3='a', COUNTRY_NAME='a')
    """
    IP_FROM = models.CharField(maxlength=20)
    IP_TO = models.CharField(maxlength=20)
    COUNTRY_CODE2 = models.CharField(maxlength = 2)
    COUNTRY_CODE3 = models.CharField(maxlength = 3)
    COUNTRY_NAME = models.CharField(maxlength = 50)     

    def __str__(self):
        return "%s %s %s" % (self.IP_FROM ,self.IP_TO, self.COUNTRY_NAME) 

    def import_csv(self, file):
        # First delete all the objects before inserting
        IpToCountry.objects.all().delete()
        # create a reader to get the data from the file
        reader = csv.reader(open(file))
        count = 0    
        for ipf, ipt, cc2, cc3, cname in reader:
            count += 1          
            object = IpToCountry(count,ipf, ipt, cc2, cc3, cname)
            object.save()
            if count % 10000 == 0:
                print count
        print count , "inserted. :)"
        del reader

    class Admin:
        ordering = ['IP_FROM']
