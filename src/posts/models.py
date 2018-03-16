import random
import string
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

# Create your models here.
class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager ,self).filter(draft=False).filter(publish__lte=timezone.now())
        
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=None)
    title = models.CharField(max_length=120, default=" ")
    content = models.TextField()
    location = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    draft = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    objects = PostManager()

    def __str__(self):
        return str(self.user) + " --> " + str(self.title)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ["-timestamp", "-updated"]


# To create slug field
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)