from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name = '제목', max_length=200)
    releasedate = models.CharField(verbose_name='개봉년도', max_length=15)
    romance='로맨스'
    horror='호러'
    action='액션'
    comedy='코미디'
    fantasy='판타지'
    SF="SF"
    sports="스포츠"
    musical="뮤지컬"
    choice_genre=(
        (romance,'로맨스'),(horror,'호러'),(action,'액션'),(comedy,'코미디'),(fantasy,'판타지'),(SF,'SF'),(sports,'스포츠'),(musical,'뮤지컬')
    )
    genre = models.CharField(choices=choice_genre, verbose_name='장르', max_length=20)
    score = models.CharField(verbose_name='별점', max_length=15)
    runtime = models.CharField(verbose_name='러닝타임', max_length=15)
    review = models.TextField(verbose_name='리뷰')
    director = models.CharField(verbose_name='감독', max_length=50)
    cast = models.CharField(verbose_name='배우', max_length=200)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # Post 모델의 제목 텍스트(string) 얻음
    def __str__(self):
        return self.title