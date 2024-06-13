from dataclasses import dataclass
from hydra.core.config_store import ConfigStore
from configs.infrastructure.infrastructure_configs import InfrastructureConfig


@dataclass
class Config:
    infrastructure: InfrastructureConfig = InfrastructureConfig()
    docker_image: str = "ml_end_to_end"



def setup_config() -> None: 
    cs = ConfigStore.instance()
    cs.store(name='config',node=Config)