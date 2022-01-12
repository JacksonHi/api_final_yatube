from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    def validate(self, attrs):

        # print(self, attrs)
        if self.context['request'].user == attrs['following']:
            raise serializers.ValidationError(
                {'name': 'нельзя подписаться на себя'}
            )
        if Follow.objects.filter(
            user=self.context['request'].user,
            following=attrs['following']
        ).exists():
            raise serializers.ValidationError(
                {'name': 'нельзя подписаться дважды'}
            )
        return attrs

    class Meta:
        fields = '__all__'
        model = Follow
