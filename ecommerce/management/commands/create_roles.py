from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from ecommerce.models import Produit, Commande  # Nos modèles


class Command(BaseCommand):

    def handle(self, *args, **options):
        role_permissions = {
            'Validateur': {
                Commande: ['consulter', 'valider'],
            },
            'Confirmateur': {
                Commande: ['consulter', 'confirmer']
            }
        }

        for role_name, models_perms in role_permissions.items():
            group, _ = Group.objects.get_or_create(name=role_name)
            self.stdout.write(f"\n Traitement du rôle : {role_name}")

            for model, actions in models_perms.items():
                ct = ContentType.objects.get_for_model(model)

                for action in actions:
                    codename = f"{action}_{model._meta.model_name}"
                    name = f"Can {action} {model._meta.verbose_name}"

                    permission, created = Permission.objects.get_or_create(
                        codename=codename,
                        content_type=ct,
                        defaults={'name': name}
                    )

                    if created:
                        self.stdout.write(f"\n Permission créée : {codename}")
                    else:
                        self.stdout.write(f"Permission existante : {codename}")

                    group.permissions.add(permission)
                    self.stdout.write(f"Assignée à : {role_name}")

        self.stdout.write(self.style.SUCCESS("\n Attribution des permissions terminée."))
