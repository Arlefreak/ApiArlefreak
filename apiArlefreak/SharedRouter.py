from rest_framework.routers import DefaultRouter, SimpleRouter

class SharedRootRouter(SimpleRouter):
    shared_router = DefaultRouter()

    def register(self, *args, **kwargs):
        self.shared_router.register(*args, **kwargs)
        super().register(*args, **kwargs)
