# imports ________________________________________________________
# aiogram
from aiogram import Router


# setting up routers _____________________________________________

# function for setting up routers
def setup_routers() -> Router:
    # importing handlers
    import handlers
    import admins

    router = Router()

    router.include_routers(admins.router, handlers.router)

    return router
