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
 
from foxyutils import FoxyData

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
      data = FoxyData.from_crypted_str(urllib.unquote_plus(request.POST['FoxyData']), settings.FOXYCART_DATAFEED_KEY)
      for transaction in data.transactions:
        
        new_user = User.objects.create_user(transaction.customer_email, transaction.customer_email)
        new_user.password = "{algorithm}${iterations}${salt}${password_hash}".format(
          algorithm="pbkdf2_sha256", 
          iterations="10000",
          salt=transaction.customer_password_salt,
          password_hash=transaction.customer_password)
        new_user.save()
        
        new_review_user = review_app.models.ReviewUser()
        new_review_user.user = new_user
        new_review_user.customer_id = transaction.customer_id
        new_review_user.save()

        # Your code goes here
        # Make sure we don't have a duplicate transaction id
        # Verify the pricing of the products
        # Add the order to the database
        pass
 
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

  logger = logging.getLogger('foxycart')
  logger.error(capture_dir)

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
