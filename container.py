from config import Configs
from core.repository.user_repository import UserRepository
from core.services.auth_service import AuthService
from core.services.character_service import CharacterService
from core.services.user_service import UserService
from core.repository.character_repository import CharacterRepository
from dependency_injector import containers, providers
from db.database import Database

config = Configs()

class Container(containers.DeclarativeContainer):
    # config = providers.Configuration(pydantic_settings=[Configs()])

    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.endpoints.auth",
            "app.api.endpoints.user",
            "app.api.endpoints.character",
            "core.dependencies"
        ]
    )

    db = providers.Singleton(Database, db_url=config.database_url)

    user_repository = providers.Factory(UserRepository, session_factory=db.provided.session)
    character_repository = providers.Factory(CharacterRepository, session_factory=db.provided.session)

    auth_service = providers.Factory(AuthService, user_repository=user_repository)
    user_service = providers.Factory(UserService, user_repository=user_repository)
    character_service = providers.Factory(CharacterService, character_repository=character_repository)
