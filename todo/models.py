from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=200)  # タスクのタイトルを格納するフィールド
    description = models.TextField(blank=True, null=True)  # タスクの詳細（省略可能）
    completed = models.BooleanField(default=False)  # タスクが完了しているかを示すフィールド
    created_at = models.DateTimeField(auto_now_add=True)  # タスクが作成された日時
    updated_at = models.DateTimeField(auto_now=True)  # タスクが最後に更新された日時

    def __str__(self):
        return self.title  # 管理画面やシェルでの表示に使用

    class Meta:
        ordering = ['-created_at']  # 作成日時で新しい順に並べる
        verbose_name = 'Todo Item'
        verbose_name_plural = 'Todo Items'
