from django.db import models

class Question(models.Model):
    number = models.IntegerField(primary_key=True, null=False)
    id = models.CharField(max_length=8)
    secret = models.CharField(max_length=8, unique=True, null=False)
    
    duration = models.IntegerField(default=120)  # in seconds
    
    statement = models.TextField()
    task = models.TextField()
    exp_output = models.TextField()  # expected output
    typical_answer = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'app_question_table'
        ordering = ['number']

    def __str__(self) -> str:
        return str(self.number)


class Team(models.Model):
    code = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=20)
    token = models.CharField(max_length=32, unique=True, blank=True, null=True, default="")    
    question = models.ForeignKey(
        Question,
        to_field='number',
        on_delete=models.DO_NOTHING,
        related_name='teams_got_question',
        default=1,
        db_constraint=False,
        null=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def is_authenticated(self):
        return True  # Since we validate in authentication class
    
    @property
    def is_anonymous(self):
        return False  # teams are not anonymous

    def get_username(self):
        return self.name  # username is team name
        
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'app_team_table'


class History(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, primary_key=True)
    team = models.ForeignKey(
        Team,
        to_field='code',
        on_delete=models.DO_NOTHING,
        related_name='team_history',
        db_constraint=False,
    )
    score = models.ForeignKey(
        Question,
        to_field='number',
        on_delete=models.DO_NOTHING,
        related_name='question_history',
        db_constraint=False
    )
    flag = models.CharField(max_length=32, unique=False)
    
    class Meta:
        db_table = 'app_history_table'
        ordering = ['timestamp']
        
    def __str__(self) -> str:
        return str(self.team.name) + " - " + str(self.score.number)