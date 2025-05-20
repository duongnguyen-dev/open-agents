import enum

class ModelType(enum.Enum):
    LOCAL = 'local'
    ONLINE = 'online'

class TeamArchitecture(enum.Enum):
    NETWORK = 'network'
    SUPERVISOR = 'supervisor'