from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserLink (models.Model):
  from_user = models.ForeignKey (User, related_name="fromuser")
  to_user = models.ForeignKey (User, related_name="touser")
  date_added = models.DateField()
  
  class Meta:
    unique_together = ("from_user", "to_user") #from_user and to_user is unique
        
  def __unicode__(self):
    return self.from_user.username + "isfollowing" + self.to_user.username
  
  def save(self, *args, **kwargs):
    if (self.from_user == self.to_user):
      raise ValidationError(("You're following yourself"), code='self_follow')
    else:
      super(UserLink, self).save(*args, **kwargs)
