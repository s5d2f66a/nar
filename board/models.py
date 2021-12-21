from django.db import models

class Post(models.Model):
    title       = models.CharField(max_length=200, verbose_name="제목")
    contents    = models.TextField(verbose_name="내용")
    photos = models.ImageField(blank=True, null=True ,upload_to="") 
    writer      = models.ForeignKey('member.BoardMember', on_delete=models.CASCADE, verbose_name="작성자", null=True)
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="작성일")

    def __str__(self):
        return self.title

    class Meta:
        db_table            = 'posts'
        verbose_name        = '게시판'
        verbose_name_plural = '게시판'
