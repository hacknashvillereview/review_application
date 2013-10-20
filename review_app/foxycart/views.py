"""
Example Django view for receiving and decrypting datafeed.
"""
 
import os
import sys
import codecs
import logging
 
import urllib
from django.http import *
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
import review_app
 
from django.core.exceptions import ObjectDoesNotExist
# from foxyutils import FoxyData
from foxyutils import *

PASSWORD_ALGORITHM = "sha1"
PRODUCT_NAME = "ReviewTN Registration"
PRODUCT_PRICE = "20.00"

@csrf_exempt
def foxyfeed(request):
  """
  This is what will get hit whenever someone creates an account, foxycart is
  hitting this from a webhook, we need to create a new user in our system. We
  look at customer id, email, hash, and verify correct product was bought.
  """
  if request.POST and 'FoxyData' in request.POST:
    try:
      # IMPORTANT: unquote_plus is necessary for the non-ASCII binary that
      # FoxyCart sends.
      valid_transaction = False
      data = FoxyData.from_crypted_str(urllib.unquote_plus(request.POST['FoxyData']), settings.FOXYCART_DATAFEED_KEY)
      for transaction in data.transactions:
        for item in transaction.items:
          if item['name'] == PRODUCT_NAME:
            valid_transaction = True

        if valid_transaction:
          # check if this user exists already. If not, create one.
          existing_user = User.objects.filter(username=transaction.customer_email)
          if (len(existing_user) > 0):
            existing_user[0].is_active = True # this doesn't work... :(
            existing_user[0].save()
          else:
            # create a new django user
            new_user = User.objects.create_user(transaction.customer_email, transaction.customer_email)
            new_user.password = "{algorithm}${salt}${password_hash}".format(
              algorithm=PASSWORD_ALGORITHM, 
              salt=transaction.customer_password_salt,
              password_hash=transaction.customer_password)
            new_user.save()

            # create a new review user
            new_review_user = review_app.models.ReviewUser()
            new_review_user.user = new_user
            new_review_user.customer_id = transaction.customer_id
            new_review_user.save()

            # @todo sanity checks etc bf actually saving everything

      return HttpResponse('foxy')

    except Exception, e:
    # Something went wrong, handle the error...
      raise
  return HttpResponseForbidden('Unauthorized request.')  # No FoxyData?  Not a POST?  We don't speak that.

@csrf_exempt
def capture_foxyfeed(request):
  capture_name = "test1"
  save_request_object = True
  allow_overwrite = False
  capture_dir =  os.path.join(os.path.dirname(__file__), "fixtures")

  #logger = logging.getLogger('foxycart')
  #logger.error(capture_dir)
  #print capture_dir

  if save_request_object:
    capture_file_path = os.path.join(capture_dir, capture_name + '.request')
    f = open(capture_file_path, 'w')
    f.write(request.__repr__())
    f.close()
  if request.method == 'POST' and 'FoxyData' in request.POST:
    encrypted_file_path = os.path.join(capture_dir, capture_name + '.encrypted')
    plaintext_file_path = os.path.join(capture_dir, capture_name + '.plaintext')
    if not allow_overwrite:
      if os.path.exists(encrypted_file_path):
          return HttpResponseForbidden('Error: data already captured.')

    f = codecs.open(encrypted_file_path, encoding='utf-8', mode="w")
    data = request.POST['FoxyData']
    f.write(data)
    f.close()
    f = codecs.open(plaintext_file_path, encoding='utf-8', mode="w")
    f.write(FoxyData.decrypt_str(urllib.unquote_plus(data), settings.FOXYCART_DATAFEED_KEY))
    return HttpResponse('foxy')
 
  return HttpResponseForbidden('Unauthorized request.')
