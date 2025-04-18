from ..repositories.user_repository import UserRepository


class UserService:
    @staticmethod
    def register_user(auth0_id: str, email: str, username: str):
        existing_user = UserRepository.get_user_by_email(email)
        if existing_user:
            return existing_user
        return UserRepository.create_user(auth0_id, email, username)

    # @staticmethod
    # def update_user(user_id: int, **kwargs):
    #     user = UserRepository.get_user_by_id(user_id)
    #     if not user:
    #         return None
    #     return UserRepository.update_user(user, **kwargs)
