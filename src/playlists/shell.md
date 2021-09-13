### Python

```py
from playlists.models import Playlist
from videos.models import Video

video_a = Video.objects.create(title="My title", video_id="abc123")

playlist_a = Playlist.objects.create(title='Test Title', video=video_a)
```

### Shell

```sh
>>>(DjangoFlix) PS D:\PYTHON PROGRAMS\Django\DjangoFlix\src> python manage.py shell
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from playlists.models import Playlist
>>> from videos.models import Video
>>> video_a = Video.objects.create(title="My title", video_id="abc123")
>>> video_a
<Video: Video object (6)>
>>> dir(video_a)
['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_default_pk', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_expr_references', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', '_prepare_related_fields_for_save', '_save_parents', '_save_table', '_set_pk_val', '_state', 'active', 'check', 'clean', 'clean_fields', 'date_error_message', 'delete', 'description', 'from_db', 'full_clean', 'get_deferred_fields', 'get_next_by_timestamp', 'get_next_by_updated', 'get_playlist_ids', 'get_previous_by_timestamp', 'get_previous_by_updated', 'get_state_display',
'id', 'is_published', 'objects', 'pk', 'playlist_set', 'prepare_database_save', 'publish_timestamp', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'slug', 'state', 'timestamp', 'title', 'unique_error_message', 'updated', 'validate_unique', 'video_id']
>>> playlist_a = Playlist.objects.create(title='Test Title', video=video_a)
>>> dir(playlist_a)
['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_default_pk', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_expr_references', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', '_prepare_related_fields_for_save', '_save_parents', '_save_table', '_set_pk_val', '_state', 'active', 'check', 'clean', 'clean_fields', 'date_error_message', 'delete', 'description', 'from_db', 'full_clean', 'get_deferred_fields', 'get_next_by_timestamp', 'get_next_by_updated', 'get_previous_by_timestamp', 'get_previous_by_updated', 'get_state_display', 'id', 'is_published', 'objects', 'pk', 'prepare_database_save', 'publish_timestamp', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'slug', 'state', 'timestamp', 'title', 'unique_error_message', 'updated', 'validate_unique', 'video', 'video_id']
>>> playlist_a.video_id
6
>>> video_a.id
6
>>> plylist_a.video=None
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'plylist_a' is not defined
>>> playlist_a.video=None
>>> playlist_a.save()
>>> playlist_a.video_id
>>> video_a.playlist_set.all
<bound method BaseManager.all of <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x000001637211E730>>
>>> video_a.playlist_set.all()
<PlaylistQuerySet []>
>>> playlist_a.video=video_a
>>> playlist_a.save()
>>> video_a.playlist_set.all
<bound method BaseManager.all of <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x00000163720FC1F0>>
>>> video_a.playlist_set.all()
<PlaylistQuerySet [<Playlist: Playlist object (3)>]>
>>> playlist_a.id
3
>>> video_a.playlist_set.all().published()
<PlaylistQuerySet []>
>>> qs = Playlist.objects.all().published()
>>> qs
<PlaylistQuerySet [<Playlist: Playlist object (1)>]>
>>> qs
<PlaylistQuerySet [<Playlist: Playlist object (1)>]>
>>> Playlist.objects.filter(video=video_a).published()
<PlaylistQuerySet []>
>>>
```
