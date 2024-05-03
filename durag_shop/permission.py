from typing import Any
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

class command(BaseCommand):
    def handle(self, *args,**kwargs):
        branach_type=ContentType.objects.get(app_label='druag_shop',model='branch')
        branachmanager_type=ContentType.objects.get(app_label='druag_shop',model='branchmanager')
        branachemployer_type=ContentType.objects.get(app_label='druag_shop',model='branchemployer')

            #permission for the super admin
        Permission.objects.create(
            codename='can_creat_branch',
            name='can creat branch',
            Content_type=branach_type


        )
        Permission.objects.create(
            codename='can_delet_branch',
            name='can delet branch',
            Content_type=branach_type

        )
        Permission.objects.create(
            codename='can_creat_branchmanager',
            name='can delet branchmanager',
            Content_type=branachmanager_type

        )
        Permission.objects.create(
            codename='can_delet_branchmanager',
            name='can delet branchmanager',
            Content_type=branach_type
        )
        Permission.objects.create(
            codename='can_creat_brancempolyer',
            name='can creat brancemployer',
            Content_type=branachmanager_type)
        Permission.objects.create(
            codename='can_delete_branchmanager',
            name='can delet branchmanager',
            Content_type=branachemployer_type)
        
        Permission.objects.create(
            codename='can_creat_branchmanager',
            name='can delet branchmanager',
            Content_type=branachemployer_type)
        

        #Permission branchman
        Permission.objects.create(
            codename='can_data_branchmanager',
            name='can data branchmanager',
            Content_type=branach_type)
        
        Permission.objects.create(
            codename='can_creat_branchemployer',
            name='can creat branchemployer',
            Content_type=branachemployer_type)
        
        Permission.objects.create(
            codename='can_deelet_branchemplo',
            name='can delet branchmanager',
            Content_type=branachemployer_type)
        Permission.objects.create(

            codename='can_access_branchempoloye',
            name='can acces branchemployer',
            Content_type=branachemployer_type)
        
            #permission of the branch employer
        
        Permission.objects.create(

            codename='can_access_branchempoloye',
            name='can acces branchemployer',
            Content_type=branachemployer_type)
        
        Permission.objects.create(

            codename='can_enterdata_branchempoloye',
            name='can enterdata branchemployer',
            Content_type=branachemployer_type)

        