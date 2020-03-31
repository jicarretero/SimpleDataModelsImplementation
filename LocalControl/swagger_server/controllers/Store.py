import memcache

class Store(object):
    class __Store:
      def __init__(self):
          self.mc = memcache.Client(['127.0.0.1:11211'], debug=0)


      def set(self, key, value):
          self.mc.set(key, value)

      def get(self, key):
          return self.mc.get(key)

      def delete(self, key):
          return self.mc.delete(key)

    instance=None

    def __new__(cls, *args, **kwargs):
        if Store.instance is None:
            Store.instance = Store.__Store()
        return Store.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)