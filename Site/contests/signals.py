from .models import Contests, PastContests, Winners, FutureContests
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Contests)
def FutureContestsCreated(sender, instance, created, **kwargs):
    contest = Contests.objects.get(title=instance.title)
    if created:
        FutureContests.objects.create(
            title=instance.title,
            text=contest.text,
            img=contest.img,
            date=contest.date,
            full_information_about_contest=contest.full_information_about_contest,
        )


@receiver(post_save, sender=Winners)
def PostContestCreated(sender, instance, created, **kwargs):
    contest = FutureContests.objects.get(title=instance.title_contest)
    if created:
        PastContests.objects.create(
            title=instance.title_contest,
            text=contest.text,
            img=contest.img,
            date=contest.date,
            winners=instance,
        )
        contest.delete()
