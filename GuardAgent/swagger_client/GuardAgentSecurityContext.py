#from swagger_server.models.configurations import Configurations
#from swagger_server.models.configuration import Configuration

class GuardAgentSecurityContext(object):
    class __GuardAgentSecurityContext:
      def __init__(self):
 #         self._time_between_probes=Configuration("time_between_probes", "int", "Time consumed between probing in seconds", "60")
 #         self._time_between_pings=Configuration("time_between_pings","int", "time ellapsed between two pings in seconds", "60")
 #         self.configurations=Configurations([self._time_between_probes, self._time_between_pings])
          pass

      def to_dict(self):
          return self.configurations.to_dict()

      def to_str(self):
          return self.configurations.to_str()

      def time_between_probes(self,tbp: int=None):
          if tbp is None:
              return int(self._time_between_probes._value)
          else:
              self._time_between_probes._value = str(tbp)

      def time_between_pings(self,tbp: int=None):
          if tbp is None:
              return int(self._time_between_pings._value)
          else:
              self._time_between_pings._value = str(tbp)

    instance=None

    def __new__(cls, *args, **kwargs):
        if GuardAgentSecurityContext.instance is None:
            GuardAgentSecurityContext.instance = GuardAgentSecurityContext.__GuardAgentSecurityContext()
        return GuardAgentSecurityContext.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)