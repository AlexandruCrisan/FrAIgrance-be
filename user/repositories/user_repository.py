from user.models import User


class UserRepository:
    @staticmethod
    def get_user_by_email(email: str):
        return User.objects.filter(email=email).first()

    @staticmethod
    def get_user_by_auth0_id(auth0_id: str):
        return User.objects.filter(auth0_id=auth0_id).first()

    @staticmethod
    def create_user(auth0_id: str, email: str, username: str):
        user = User.objects.create(
            auth0_id=auth0_id, email=email, username=username)
        return user
