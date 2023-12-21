from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from .models import Post, Comment

class PostBaseModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['id', 'writer', 'content', ]
        
class PostListModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):

        fields = [
            'id', 
            'image', 
            'content', 
            'created_at', 
            'view_count', 
            'writer',
            ]
        depth = 1
        # exclude = ['content', ]

class PostRetrieveModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        depth = 1
        

class PostCreateModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = [
            'image', 
            'content', 
            ]
    

class PostDeleteModelSerializer(PostBaseModelSerializer):
    pass

class CommentHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentListModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
